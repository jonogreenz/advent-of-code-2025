from part1 import fewer_than_in_adjacent

test_grid = [
		[None, 1, None],
		[None, None, None],
		[1, None, 1],
	]

assert fewer_than_in_adjacent(test_grid, 0, 0, 2) == True
assert fewer_than_in_adjacent(test_grid, 1, 1, 2) == False
assert fewer_than_in_adjacent(test_grid, 2, 0, 2) == True
assert fewer_than_in_adjacent(test_grid, 1, 2, 2) == False
