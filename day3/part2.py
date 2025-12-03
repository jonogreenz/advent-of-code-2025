lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()


def largest_number_and_idx_in_line(line, start_idx, excluded_indices=[]):
    curr_largest_digit_and_idx = (0, -1)

    for i in range(start_idx, len(line)):
        d = int(line[i])
        if d > curr_largest_digit_and_idx[0] and i not in excluded_indices:
            curr_largest_digit_and_idx = (d, i)
    return curr_largest_digit_and_idx


def get_largest_numbers(line, total_numbers):
    curr_number_index = -1

    largest_numbers = []

    while len(largest_numbers) < total_numbers:
        largest_numbers_idx = [num[1] for num in largest_numbers]
        curr_index = (
            largest_numbers[curr_number_index][1] if curr_number_index != -1 else 0
        )

        largest = largest_number_and_idx_in_line(line, curr_index, largest_numbers_idx)

        # print (f"Current largest numbers: {largest_numbers}, checking for next largest from index {curr_index}, found {largest}")

        if largest[1] == -1:
            # Couldn't find any more numbers on right, backtrack to previous index
            curr_number_index -= 1
            continue
        else:
            # Reset index back to current length
            largest_numbers.append(largest)
            curr_number_index = len(largest_numbers) - 1

    # print (f"Final largest numbers: {largest_numbers}")
    return largest_numbers


def get_final_value_from_largest_arr(largest_arr):
    ordered_by_idx = sorted(largest_arr, key=lambda x: x[1])
    result = ""
    for val in ordered_by_idx:
        result += str(val[0])
    return result


if __name__ == "__main__":
    total = 0
    for line in lines:
        line = line.strip()

        largest_numbers = get_largest_numbers(line, 12)

        line_total = int(get_final_value_from_largest_arr(largest_numbers))

        print(f"Line total for line '{line}': {line_total}")
        total += line_total

    print(f"Total for all lines: {total}")
