from part2 import (
    largest_number_and_idx_in_line,
    get_final_value_from_largest_arr,
    get_largest_numbers,
)


assert largest_number_and_idx_in_line("1234567890", 0, [8]) == (8, 7)
assert largest_number_and_idx_in_line("9876543210", 5, [0, 1, 2, 6]) == (4, 5)

assert get_largest_numbers("23423423423478", 8) == [
    (8, 13),
    (7, 12),
    (4, 2),
    (4, 5),
    (4, 8),
    (4, 11),
    (3, 10),
    (2, 9),
]

assert get_final_value_from_largest_arr([(9, 8), (8, 7), (7, 6)]) == "789"
assert get_final_value_from_largest_arr([(4, 8), (8, 2), (9, 3)]) == "894"
