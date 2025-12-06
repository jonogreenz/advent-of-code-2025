import math

if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    all_line_values = []
    for i in range(len(lines)-1):
        line = lines[i]
        line_values = [int(x) for x in line.strip().split(' ') if x != '']
        all_line_values.append(line_values)

    operations = [x for x in lines[-1].strip().split(' ') if x != '']

    complete_sum = 0
    for i in range(len(operations)):
        op = operations[i]
        values = [item[i] for item in all_line_values]
        if op == "*":
            total = math.prod(values)
        elif op == "+":
            total = sum(values)
        complete_sum += total

        # print(f"Operation {op} on values {values} gives total {total}")

    print(f"Complete sum: {complete_sum}")