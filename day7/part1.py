def simulate_split(max_length, current_splits, splitter_indices):
    new_splits = []

    total_split_count = 0

    for v in current_splits:
        if v in splitter_indices:
            if v - 1 >= 0:
                new_splits.append(v - 1)
            if v + 1 < max_length:
                new_splits.append(v + 1)

            if v - 1 > 0 or v + 1 < max_length:
                total_split_count += 1

        else:
            new_splits.append(v)

    new_splits = list(set(new_splits))

    return (new_splits, total_split_count)


if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    start_index = [i for i, c in enumerate(lines[0]) if c == "S"][0]

    splitter_indices_per_line = []
    for line in lines:
        line = line.strip()
        indices = [i for i, c in enumerate(line) if c == "^"]
        if len(indices) > 0:
            splitter_indices_per_line.append(indices)

    current_splits = [start_index]
    max_length = len(lines[0].strip())
    total_split_count = 0
    for splitter_indices in splitter_indices_per_line:
        (new_splits, split_count) = simulate_split(
            max_length, current_splits, splitter_indices
        )
        current_splits = new_splits
        total_split_count += split_count

    print(f"Total splits: {total_split_count}")
