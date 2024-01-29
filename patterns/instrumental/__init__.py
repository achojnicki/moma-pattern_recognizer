patterns=[
	{
		"name": "double_bottom",
		"simple_patterns":
			{
				
				"flat_entry_point_fall_by_1": {"pattern_name": "flat_entry_point_fall_by_1", "pattern": [0,0,0,0,0,0,0,0,0,-1]},
				"flat_entry_point_fall_by_2": {"pattern_name": "flat_entry_point_fall_by_2", "pattern": [0,0,0,0,0,0,0,0,0,-2]},
				"flat_entry_point_fall_by_3":{"pattern_name": "flat_entry_point_fall_by_3", "pattern": [0,0,0,0,0,0,0,0,0,-3]},
				"flat_entry_point_fall_by_4":{"pattern_name": "flat_entry_point_fall_by_4", "pattern": [0,0,0,0,0,0,0,0,0,-4]},
				"flat_entry_point_fall_by_5":{"pattern_name": "flat_entry_point_fall_by_5", "pattern": [0,0,0,0,0,0,0,0,0,-5]},
				"flat_entry_point_fall_by_6":{"pattern_name": "flat_entry_point_fall_by_6", "pattern": [0,0,0,0,0,0,0,0,0,-6]},
				"flat_entry_point_fall_by_7":{"pattern_name": "flat_entry_point_fall_by_7", "pattern": [0,0,0,0,0,0,0,0,0,-7]},
				"flat_entry_point_fall_by_8":{"pattern_name": "flat_entry_point_fall_by_8", "pattern": [0,0,0,0,0,0,0,0,0,-8]},
				"flat_entry_point_fall_by_9":{"pattern_name": "flat_entry_point_fall_by_9", "pattern": [0,0,0,0,0,0,0,0,0,-9]},
				"flat_entry_point_fall_by_10":{"pattern_name": "flat_entry_point_fall_by_10", "pattern": [0,0,0,0,0,0,0,0,0,-10]},
	
			},
		"instrumental_patterns": 
			{
				"entry_point": 
					{
						"name":"entry_point",
						"event": "start_point",
						"matching_min": 6,
						"patterns": [
							{"pattern_name": "flat_entry_point_fall_by_1", "match_value_min": 99, "match_value_max": 100.50, "must_match_indexes": [1,2,9]},
							{"pattern_name": "flat_entry_point_fall_by_2", "match_value_min": 99, "match_value_max": 100.50, "must_match_indexes": [1,2,9]},
							{"pattern_name": "flat_entry_point_fall_by_3", "match_value_min": 99, "match_value_max": 100.50, "must_match_indexes": [1,2,9]},
							{"pattern_name": "flat_entry_point_fall_by_4", "match_value_min": 99, "match_value_max": 100.50, "must_match_indexes": [1,2,9]},
							{"pattern_name": "flat_entry_point_fall_by_5", "match_value_min": 99, "match_value_max": 100.50, "must_match_indexes": [1,2,9]},
							{"pattern_name": "flat_entry_point_fall_by_6", "match_value_min": 99, "match_value_max": 101.50, "must_match_indexes": [1,2,9]},
							{"pattern_name": "flat_entry_point_fall_by_7", "match_value_min": 99, "match_value_max": 101.50, "must_match_indexes": [1,2,9]},
							{"pattern_name": "flat_entry_point_fall_by_8", "match_value_min": 99, "match_value_max": 101.50, "must_match_indexes": [1,2,9]},
							{"pattern_name": "flat_entry_point_fall_by_9", "match_value_min": 99, "match_value_max": 101.50, "must_match_indexes": [1,2,9]},
							{"pattern_name": "flat_entry_point_fall_by_10", "match_value_min": 99, "match_value_max": 101.50, "must_match_indexes": [1,2,9]},						

						]
					},
				"first_period":
					{
						"name": "first_period",
						"event": "first_period",
						"match_value_min": 80,
						"match_value_max": 150,
						"matching_min": 6,
						"patterns": [
							{"pattern_type": "rising_integer_linear"},
							{"pattern_type": "rising_integer_by_2"},
							{"pattern_type": "rising_integer_by_4"},
							{"pattern_type": "rising_integer_by_8"},
							{"pattern_type": "rising_integer_by_16"},
							{"pattern_type": "rising_integer_by_32"}
						]

					},
				"second_period":
					{
						"name": "second_period",
						"event": "second_period",
						"match_value_min": 80,
						"match_value_max": 150,
						"matching_min": 6,
						"patterns": [
							{"pattern_type": "falling_integer_linear"},
							{"pattern_type": "falling_integer_by_2"},
							{"pattern_type": "falling_integer_by_4"},
							{"pattern_type": "falling_integer_by_8"},
							{"pattern_type": "falling_integer_by_16"},
							{"pattern_type": "falling_integer_by_32"}
						]
					},

				"final_rise":
					{
						"name": "final_rise",
						"event": "final_rise",
						"match_value_min": 96,
						"match_value_max": 150,
						"matching_min": 6,
						"patterns": [
							{"pattern_type": "falling_integer_linear"},
							{"pattern_type": "falling_integer_by_2"},
							{"pattern_type": "falling_integer_by_4"},
							{"pattern_type": "falling_integer_by_8"},
							{"pattern_type": "falling_integer_by_16"},
							{"pattern_type": "falling_integer_by_32"}
						]
					}
			}
	}
]