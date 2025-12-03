from part1 import largest_number_and_idx_in_line, get_two_largest


assert largest_number_and_idx_in_line("1234567890") == (9, 8)
assert largest_number_and_idx_in_line("9876543210") == (9, 0)
assert largest_number_and_idx_in_line("1111111111") == (1, 0)
assert largest_number_and_idx_in_line("0010080008") == (8, 5)

assert get_two_largest("1234567890") == "89"
