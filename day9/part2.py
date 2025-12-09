def point_on_edge(point, edge):
    point1, point2 = edge

    if point1[0] == point2[0]:
        # Vertical edge
        return point[0] == point1[0] and min(point1[1], point2[1]) <= point[1] <= max(
            point1[1], point2[1]
        )
    else:
        # Horizontal edge
        return point[1] == point2[1] and min(point1[0], point2[0]) <= point[0] <= max(
            point1[0], point2[0]
        )


def point_in_polygon(point, edges):
    # I'll admit, this is from the Google AI because I can't remember how to do axis-aligned ray
    # casting :(
    x, y = point
    inside = False

    # Cast a ray from the point to the right (increasing x)
    # Count how many edges it crosses
    for edge in edges:
        p1, p2 = edge
        x1, y1 = p1
        x2, y2 = p2

        # Check if edge is vertical and crosses our horizontal ray
        if x1 == x2:
            # Vertical edge
            edge_x = x1
            min_y = min(y1, y2)
            max_y = max(y1, y2)

            # Check if ray crosses this edge
            if edge_x > x and min_y <= y < max_y:
                inside = not inside
        # Horizontal edges don't affect the ray

    return inside


def point_in_or_on_polygon(point, edges):
    # Need to check edges first
    for edge in edges:
        if point_on_edge(point, edge):
            return True

    # Then can check interior with ray casting
    return point_in_polygon(point, edges)


def compute_xy_area(corner1, corner2):
    area = abs(corner2[0] - corner1[0]) + 1
    area *= abs((corner2[1]) - corner1[1]) + 1

    return area


def get_sorted_areas(all_xy_positions):
    pairwise_areas = []
    for i in range(0, len(all_xy_positions)):
        pos1 = all_xy_positions[i]
        for j in range(i + 1, len(all_xy_positions)):
            pos2 = all_xy_positions[j]
            area = compute_xy_area(pos1, pos2)
            pairwise_areas.append((area, (pos1, pos2)))

    pairwise_areas = sorted(pairwise_areas, key=lambda x: x[0], reverse=True)

    return pairwise_areas


def do_edges_intersect(edge1_point1, edge1_point2, edge2_point1, edge2_point2):
    # Note: axis-aligned lines only
    # Note: only true if they cross, not just touch at endpoints or share edges

    p1x1 = min(edge1_point1[0], edge1_point2[0])
    p1y1 = min(edge1_point1[1], edge1_point2[1])
    p1x2 = max(edge1_point1[0], edge1_point2[0])
    p1y2 = max(edge1_point1[1], edge1_point2[1])
    p2x1 = min(edge2_point1[0], edge2_point2[0])
    p2y1 = min(edge2_point1[1], edge2_point2[1])
    p2x2 = max(edge2_point1[0], edge2_point2[0])
    p2y2 = max(edge2_point1[1], edge2_point2[1])

    if p1y1 == p1y2:  # edge1 is horizontal
        if p2y1 == p2y2:  # edge is also horizontal, therefore cannot intersect
            return False
        else:
            # edge2 is vertical, but only intersects if within bounds
            if p2x1 <= p1x1 or p2x1 >= p1x2:
                return False
            if p1y2 <= p2y1 or p1y1 >= p2y2:
                return False
            return True
    else:  # edge1 is vertical
        if p2x1 == p2x2:  # edge2 is also vertical, therefore cannot intersect
            return False
        else:
            # edge2 is horizontal, but only intersects if within bounds
            if p1x2 <= p2x1 or p1x1 >= p2x2:
                return False
            if p2y2 <= p1y1 or p2y1 >= p1y2:
                return False
            return True


def does_area_intersect_edges(corner1, corner2, edges):
    rect_edges = [
        [(corner1[0], corner1[1]), (corner2[0], corner1[1])],
        [(corner2[0], corner1[1]), (corner2[0], corner2[1])],
        [(corner2[0], corner2[1]), (corner1[0], corner2[1])],
        [(corner1[0], corner2[1]), (corner1[0], corner1[1])],
    ]

    for rect_edge in rect_edges:
        for poly_edge in edges:
            if do_edges_intersect(
                rect_edge[0], rect_edge[1], poly_edge[0], poly_edge[1]
            ):
                return True
    return False


def is_rectangle_valid(corner1, corner2, edges):
    if does_area_intersect_edges(corner1, corner2, edges):
        return False

    # Check if all four corners of the rectangle are inside or on the polygon
    min_x = min(corner1[0], corner2[0])
    min_y = min(corner1[1], corner2[1])
    max_x = max(corner1[0], corner2[0])
    max_y = max(corner1[1], corner2[1])

    corners = [
        (min_x, min_y),
        (max_x, min_y),
        (max_x, max_y),
        (min_x, max_y),
    ]

    for corner in corners:
        if not point_in_or_on_polygon(corner, edges):
            return False

    return True


if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    all_xy_positions = []
    for line in lines:
        pos_list = [int(v) for v in line.strip().split(",")]
        xyz_pos = (pos_list[0], pos_list[1])
        all_xy_positions.append(xyz_pos)

    edges = []
    for i, _ in enumerate(all_xy_positions):
        edge = (
            all_xy_positions[i],
            all_xy_positions[i + 1 if i + 1 < len(all_xy_positions) else 0],
        )
        edges.append(edge)

    largest_areas = get_sorted_areas(all_xy_positions)

    for area, (corner1, corner2) in largest_areas:
        if is_rectangle_valid(corner1, corner2, edges):
            print(f"Largest valid area: {area} between {corner1} and {corner2}")
            break
