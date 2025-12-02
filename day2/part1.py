line = ""
with open("input.txt") as f:
    line = f.readlines()[0].strip()

ids = line.split(",")


def is_repeating_pattern(s):
    n = len(s)

    if (n % 2) != 0:
        return False

    first_half = s[: n // 2]
    second_half = s[n // 2 :]

    return first_half == second_half


if __name__ == "__main__":
    invalid_ids_total = 0

    for i in range(len(ids)):
        (first, last) = ids[i].split("-")

        first_num = int(first)
        last_num = int(last)

        current_num = first_num     
        while current_num <= last_num:
            s = str(current_num)
            if is_repeating_pattern(s):
                invalid_ids_total += current_num
            current_num += 1
            
    print(f"Total of invalid IDs: {invalid_ids_total}")
	