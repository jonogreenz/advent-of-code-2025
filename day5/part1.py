def is_id_valid_for_any_range(id, id_ranges):
    for id_range in id_ranges:
        if id_range[0] <= id <= id_range[1]:
            return True
    return False

if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    id_ranges = []
    ids = []

    collecting_ids = False
    for line in lines:
        line = line.strip()
        if line == "":
            collecting_ids = True
            continue

        if collecting_ids:
            ids.append(int(line))
        else:
            parts = line.split("-")
            id_ranges.append((int(parts[0]), int(parts[1])))

    total = 0
    for num in ids:
        if is_id_valid_for_any_range(num, id_ranges):
            total += 1
            print (f"Valid ID: {num}")

    print (f"Total of valid IDs: {total}")