from part2 import does_area_intersect_edges, do_edges_intersect, point_in_or_on_polygon

assert do_edges_intersect((0, 5), (10, 5), (5, 0), (5, 10)) == True  # Cross
assert (
    do_edges_intersect((0, 5), (5, 5), (5, 0), (5, 10)) == False
)  # Touching at endpoint
assert do_edges_intersect((0, 5), (10, 5), (3, 5), (7, 5)) == False  # B0th horizontal
assert do_edges_intersect((5, 0), (5, 10), (5, 3), (5, 7)) == False  # Both vertical


assert do_edges_intersect((0, 2), (5, 2), (4, 2), (4, 4)) == False
assert do_edges_intersect((2, 0), (2, 5), (0, 5), (5, 5)) == False

assert (
    does_area_intersect_edges(
        (0, 5),
        (5, 2),
        [
            ((0, 5), (5, 5)),
            ((5, 5), (5, 0)),
            ((5, 0), (0, 0)),
            ((0, 0), (0, 5)),
        ],
    )
    == False
)

assert (
    does_area_intersect_edges(
        (0, 5),
        (5, 2),
        [
            ((1, 5), (5, 5)),
            ((5, 5), (5, 0)),
            ((5, 0), (1, 0)),
            ((1, 0), (1, 5)),
        ],
    )
    == True
)

assert (
    does_area_intersect_edges(
        (9, 5),
        (2, 3),
        [((9, 5), (2, 5)), ((2, 5), (2, 3)), ((2, 3), (7, 3)), ((7, 3), (7, 1))],
    )
    == False
)

# Special case with edges outside of direct line
assert (
    does_area_intersect_edges(
        (7, 1),
        (11, 7),
        [
            ((9, 5), (2, 5)),
            ((2, 5), (2, 2)),
            ((2, 2), (3, 2)),
            ((3, 2), (3, 5)),
            ((3, 5), (9, 5)),
        ],
    )
    == True
)


assert (
    point_in_or_on_polygon(
        (3, 3), [((0, 0), (5, 0)), ((5, 0), (5, 5)), ((5, 5), (0, 5)), ((0, 5), (0, 0))]
    )
    == True
)  # In the middle

assert (
    point_in_or_on_polygon(
        (0, 0), [((0, 0), (5, 0)), ((5, 0), (5, 5)), ((5, 5), (0, 5)), ((0, 5), (0, 0))]
    )
    == True
)  # On the corner
assert (
    point_in_or_on_polygon(
        (4, 5), [((0, 0), (5, 0)), ((5, 0), (5, 5)), ((5, 5), (0, 5)), ((0, 5), (0, 0))]
    )
    == True
)  # On edge
assert (
    point_in_or_on_polygon(
        (4, 6), [((0, 0), (5, 0)), ((5, 0), (5, 5)), ((5, 5), (0, 5)), ((0, 5), (0, 0))]
    )
    == False
)  # Outside
