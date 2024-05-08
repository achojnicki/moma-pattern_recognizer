from adistools.adisconfig import adisconfig
from adistools.log import Log

from json import loads, dumps
from redis import Redis
from pika import BlockingConnection, PlainCredentials, ConnectionParameters
from pprint import pprint, pformat
from time import sleep

from moma.pattern_recognizer.simple import Simple
from moma.pattern_recognizer.instrumental import Instrumental

from patterns.simple import patterns as patterns_simple
from patterns.instrumental import patterns as patterns_instrumental


class pattern_recognizer:
    project_name = "moma-pattern_recognizer"

    def __init__(self):
        self.active=True

        self.config = adisconfig('/opt/adistools/configs/moma-pattern_recognizer.yaml')
        self.log = Log(
            parent=self,
            rabbitmq_host=self.config.rabbitmq.host,
            rabbitmq_port=self.config.rabbitmq.port,
            rabbitmq_user=self.config.rabbitmq.user,
            rabbitmq_passwd=self.config.rabbitmq.password,
            debug=self.config.log.debug,
        )

        self.rabbitmq_conn = BlockingConnection(
            ConnectionParameters(
                host=self.config.rabbitmq.host,
                port=self.config.rabbitmq.port,
                credentials=PlainCredentials(
                    self.config.rabbitmq.user,
                    self.config.rabbitmq.password
                )
            )
        )

        self.rabbitmq_channel = self.rabbitmq_conn.channel()
    
        self.redis_conn=Redis(
            host=self.config.redis.host,
            port=self.config.redis.port
        )

        self.simple_pattern_recogn=Simple()
        self.instrumental_pattern_recogn=Instrumental(
            patterns_instrumental,
            self.simple_pattern_recogn,
        )


    def get_chunk(self, start_offset, chunk_size):
        out=[]
        data=self.redis_conn.lrange('moma:BTC/USD:indexes', start_offset, (start_offset+chunk_size)-1)

        for timestamp in data:
            item_name=f"moma:BTC/USD:{timestamp.decode('utf-8')}"
            item=self.redis_conn.hgetall(item_name)

            d={}
            for x in item:
                d[x.decode('utf-8')]=float(item[x])
            out.append(d)
        
        return out

    def scan(self):
        chunk_size=self.config.pattern_recognizer.chunk_size
        indexes_count=self.redis_conn.llen("moma:BTC/USD:indexes")


        for offset in range(0,int(indexes_count+1/chunk_size)):
            chunk=self.get_chunk(offset, chunk_size)
            result=self.instrumental_pattern_recogn.find_pattern(chunk)

            if result and len(result)==2 and result[0]:
                self.rabbitmq_channel.basic_publish(exchange="", routing_key="moma-events", body=dumps(result[1]))




    def loop(self):
        while self.active:
            self.scan()
            sleep(0.1)

    def start(self):
        self.loop()

if __name__=="__main__":
    worker=pattern_recognizer()
    worker.start()