def find_by_input_label(all_inputs, label):
    for i, (input_label, output_labels) in enumerate(all_inputs):
        if input_label == label:
            return (i, output_labels)
    raise ValueError(f"Could not find input with label {label}")

if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    us_idx = -1

    all_inputs = []
    for i, line in enumerate(lines):
        input_label, output_labels = line.split(':')
        output_labels = output_labels.strip().split(' ')

        inputs = (input_label, output_labels)
        all_inputs.append(inputs)

        if input_label == "you":
            us_idx = i

    queue = [us_idx]

    path_count = 0
    while queue:
        current_idx = queue.pop(0)
        input_label, output_labels = all_inputs[current_idx]

        for output_label in output_labels:
            new_input_idx, new_input_outputs = find_by_input_label(all_inputs, output_label)
            if new_input_outputs[0] != "out":
                queue.append(new_input_idx)
            else:
                path_count += 1

    print(f"Total paths to 'out': {path_count}")
