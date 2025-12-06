import math

if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    all_line_values = []
    for i in range(len(lines) - 1):
        line = lines[i]
        line_values = [int(x) for x in line.strip().split(" ") if x != ""]
        all_line_values.append(line_values)

    operations = [x for x in lines[-1].strip().split(" ") if x != ""]

    largest_digits_per_operation = []
    for i in range(len(operations)):
        values = [item[i] for item in all_line_values]
        largest_num_digits = max([len(str(v)) for v in values])
        largest_digits_per_operation.append(largest_num_digits)

    all_split_line_values = []
    for i in range(len(lines) - 1):
        curr_idx = 0
        split_line_value = []
        current_line = lines[i]
        for j in range(len(operations)):
            largest_digit = largest_digits_per_operation[j]
            vals = current_line[curr_idx : curr_idx + largest_digit]
            curr_idx += largest_digit + 1  # +1 for space

            split_vals = []
            for i in range(len(vals)):
                if vals[i] != ' ':
                    split_vals.append(int(vals[i]))
                else:
                    split_vals.append(None)

            split_line_value.append(split_vals)

        all_split_line_values.append(split_line_value)

    complete_sum = 0
    for i in range(len(operations)):
        op = operations[i]
        split_values = [item[i] for item in all_split_line_values]

        transposed_split_values = [list(row) for row in zip(*split_values)]

        # Lazy
        final_transposed_values = []
        for transposed in transposed_split_values:
            digits = [str(d) for d in transposed if d != None]
            val = int("".join(digits))
            final_transposed_values.append(val)

        if op == "*":
            total = math.prod(final_transposed_values)
        elif op == "+":
            total = sum(final_transposed_values)

        complete_sum += total

        print(f"Operation {op} on values {final_transposed_values} gives total {total}")

    print(f"Complete sum: {complete_sum}")