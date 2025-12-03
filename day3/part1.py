lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()


def largest_number_and_idx_in_line(line):
    curr_largest_digit_and_idx = (0, -1)
    for i in range(0, len(line)):
        d = int(line[i])
        if d > curr_largest_digit_and_idx[0]:
            curr_largest_digit_and_idx = (d, i)
    return curr_largest_digit_and_idx


def get_two_largest(line):
    largest = largest_number_and_idx_in_line(line)

    right_largest = largest_number_and_idx_in_line(line[largest[1] + 1 :])

    if right_largest[1] != -1:
        two_largest = (largest, right_largest)
    else:
        left_largest = largest_number_and_idx_in_line(line[0 : largest[1]])
        two_largest = (left_largest, largest)

    return str(two_largest[0][0]) + str(two_largest[1][0])


if __name__ == "__main__":
    total = 0
    for line in lines:
        line = line.strip()

        line_total = int(get_two_largest(line))

        print(f"Line total for line '{line}': {line_total}")
        total += line_total

    print(f"Total for all lines: {total}")
