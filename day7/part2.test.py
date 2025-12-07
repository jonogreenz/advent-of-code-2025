from part2 import walk_back_to_find_possibilities

assert (
    walk_back_to_find_possibilities(
        [
            [None, 1, None, 1, None, None, None],
            [None, 0, None, None, 1, None, None],
            [None, None, 2, None, 0, None, None],
            [None, None, None, None, None, None, 0],
        ],
        (3, 3),
    )
) == 3

assert (
    walk_back_to_find_possibilities(
        [
            [None, 1, None, 1, None, None, None],
            [None, 0, None, None, 1, None, None],
            [None, None, 2, None, 0, None, None],
            [None, None, None, None, None, None, 0],
        ],
        (2, 3),
    )
) == 0

assert (
    walk_back_to_find_possibilities(
        [
            [None, 1, None, 1, None, None, None],
            [None, 0, None, None, 1, None, None],
            [None, None, 2, None, 0, None, None],
            [None, None, None, None, None, None, 0],
        ],
        (0, 2),
    )
) == 1
