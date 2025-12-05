from part2 import get_all_ranges, get_all_ranges_merged, total_ids_in_ranges

assert get_all_ranges((5, 10), (8, 12)) == [(5, 12)]
assert get_all_ranges((8, 12), (5, 10)) == [(5, 12)]
assert get_all_ranges((1, 3), (5, 7)) == [(1, 3), (5, 7)]
assert get_all_ranges((5, 7), (1, 3)) == [(5, 7), (1, 3)]

assert get_all_ranges_merged([(10, 18)], (16, 20)) == [(10, 20)]
assert get_all_ranges_merged([(10, 18), (20, 22)], (16, 20)) == [(10, 22)]

assert total_ids_in_ranges([(5, 10), (15, 20)]) == 12
