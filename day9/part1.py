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
            pairwise_areas.append((area, (i, j)))

    pairwise_areas = sorted(pairwise_areas, key=lambda x: x[0], reverse=True)

    return pairwise_areas


if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    all_xy_positions = []
    for line in lines:
        pos_list = [int(v) for v in line.strip().split(",")]
        xyz_pos = (pos_list[0], pos_list[1])
        all_xy_positions.append(xyz_pos)

    largest_areas = get_sorted_areas(all_xy_positions)

    largest_area_pair = largest_areas[0]

    area = largest_area_pair[0]
    print(f"Largest area: {area}")
