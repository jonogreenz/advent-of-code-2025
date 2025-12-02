from part2 import is_pattern_contained_in_string_at_least_twice, is_repeating_sequence

assert is_repeating_sequence("1212") == True
assert is_repeating_sequence("1213") == False
assert is_repeating_sequence("111") == True

assert is_pattern_contained_in_string_at_least_twice("12", "1212") == True
assert is_pattern_contained_in_string_at_least_twice("123", "123123") == True
assert is_pattern_contained_in_string_at_least_twice("123", "123123123") == True
assert is_pattern_contained_in_string_at_least_twice("11", "11") == False
assert is_pattern_contained_in_string_at_least_twice("1", "11") == True
assert is_pattern_contained_in_string_at_least_twice("113", "113112") == False
