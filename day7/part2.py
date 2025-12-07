def walk_back_to_find_possibilities(all_splitter_lines, current_splitter_pos):
    (index, y) = current_splitter_pos

    curr_y = y
    current_possibilities = 0
    while curr_y > 0:
        curr_y -= 1

        up_val = all_splitter_lines[curr_y][index]

        if up_val is not None:
            # Blocked by another splitter directly above
            break

        up_right_val = (
            all_splitter_lines[curr_y][index + 1]
            if index + 1 < len(all_splitter_lines[curr_y])
            else None
        )
        up_left_val = all_splitter_lines[curr_y][index - 1] if index - 1 >= 0 else None

        if up_right_val is not None:
            current_possibilities += all_splitter_lines[curr_y][index + 1]
        if up_left_val is not None:
            current_possibilities += all_splitter_lines[curr_y][index - 1]

    return current_possibilities


if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    start_index = [i for i, c in enumerate(lines[0]) if c == "S"][0]

    splitter_possibilities = []
    for line in lines:
        line = line.strip()
        indices = [0 if c == "^" else None for i, c in enumerate(line)]
        if any(i is not None for i in indices):
            splitter_possibilities.append(indices)

    # Ensure first index has 1 possibility
    splitter_possibilities[0][start_index] = 1

    # Insert fake last line full of splitters
    x_length = len(splitter_possibilities[0])
    splitter_possibilities.append([0 for _ in range(x_length)])
    y_length = len(splitter_possibilities)

    # Go through each splitter, updating its possibilities based on splitters above it (skipping first line)
    for y in range(1, y_length):
        for x in range(x_length):
            if splitter_possibilities[y][x] is not None:
                possibilities = walk_back_to_find_possibilities(
                    splitter_possibilities, (x, y)
                )
                splitter_possibilities[y][x] = possibilities

    splitter_possibilities_at_end = splitter_possibilities[-1]
    total_split_count = sum(splitter_possibilities_at_end)
    print(f"Total splits: {total_split_count}")
