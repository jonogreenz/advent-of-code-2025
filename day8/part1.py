import math


def compute_xyz_distance(pos1, pos2):
    return math.sqrt(
        (pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2 + (pos2[2] - pos1[2]) ** 2
    )


def get_sorted_distances(all_xyz_positions):
    pairwise_distances = []
    for i in range(0, len(all_xyz_positions)):
        pos1 = all_xyz_positions[i]
        for j in range(i + 1, len(all_xyz_positions)):
            pos2 = all_xyz_positions[j]
            distance = compute_xyz_distance(pos1, pos2)
            pairwise_distances.append((distance, (i, j)))

    pairwise_distances = sorted(pairwise_distances, key=lambda x: x[0])

    return pairwise_distances


def merge_circuits_if_needed(current_circuits, pos1_idx, pos2_idx):
    circuit1 = None
    circuit2 = None
    for circuit in current_circuits:
        if pos1_idx in circuit:
            circuit1 = circuit
        if pos2_idx in circuit:
            circuit2 = circuit

    if circuit1 is not None and circuit2 is not None and circuit1 != circuit2:
        # Merge circuits
        circuit1.extend(circuit2)
        current_circuits.remove(circuit2)

    return current_circuits


if __name__ == "__main__":
    lines = []
    total_iterations = 1000
    with open("input.txt", "r") as f:
        lines = f.readlines()

    all_xyz_positions = []
    for line in lines:
        pos_list = [int(v) for v in line.strip().split(",")]
        xyz_pos = (pos_list[0], pos_list[1], pos_list[2])
        all_xyz_positions.append(xyz_pos)

    current_circuits = [[i] for i, _ in enumerate(all_xyz_positions)]
    closest_positions = get_sorted_distances(all_xyz_positions)

    for i in range(0, total_iterations):
        closest_pair = closest_positions[i]
        closest_distance = closest_pair[0]
        closest_position = closest_pair[1]

        current_circuits = merge_circuits_if_needed(
            current_circuits, closest_position[0], closest_position[1]
        )

        # print(
        #     f"Current circuits: {current_circuits}, closest pair: {closest_pair}"
        # )

    # 3 largest circuits
    sorted_circuits = sorted(current_circuits, key=lambda x: len(x), reverse=True)
    print(f"Largest circuits: {sorted_circuits[:3]}")
    lens = [len(circuit) for circuit in sorted_circuits[:3]]
    print(f"Largest circuit multiplication: {math.prod(lens)}")
