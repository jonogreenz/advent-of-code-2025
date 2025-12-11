import datetime

# lols - from the time where I forgot about dynamic programming :(
it = 0
start_time = datetime.datetime.now()


def search_dfs(
    all_inputs,
    start_label,
    target_label,
    required_labels,
):
    # memoize based on node and visited required labels
    memo = {}

    def dfs_labels(current_label, current_path, required_seen):
        global it, start_time
        it += 1
        if it % 100000 == 0:
            elapsed = datetime.datetime.now() - start_time
            print(f"Elapsed time: {elapsed}, iterations: {it}")

        # base case
        if current_label == target_label:
            if len(required_labels) > 0:
                if required_seen == required_labels:
                    return 1
                return 0
            return 1

        # check if we already have current state
        key = str(current_label) + "_" + str(required_seen)
        if key in memo:
            return memo[key]

        # check if current_label is already in the path
        if current_label in current_path:
            return 0

        # recursive case
        total_count = 0
        output_labels = all_inputs[current_label][1]

        new_required_seen = required_seen
        if current_label in required_labels:
            new_required_seen = required_seen + [current_label]

        for output_label in output_labels:
            count = dfs_labels(
                output_label, current_path + [current_label], new_required_seen
            )
            total_count += count

        memo[str(current_label) + "_" + str(required_seen)] = total_count
        return total_count

    return dfs_labels(start_label, [], [])


if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    all_input_labels = []
    all_inputs_with_outputs = []
    for i, line in enumerate(lines):
        input_label, output_labels = line.split(":")
        output_labels = output_labels.strip().split(" ")

        inputs_with_outputs = (input_label, output_labels)
        all_inputs_with_outputs.append(inputs_with_outputs)
        all_input_labels.append(input_label)

    # special for out node
    all_inputs_with_outputs.append(("out", []))
    all_input_labels.append("out")

    all_inputs_with_outputs_nums = []
    for i, (input_label, output_labels) in enumerate(all_inputs_with_outputs):
        output_idxs = []
        for lbl in output_labels:
            output_idxs.append(all_input_labels.index(lbl))

        all_inputs_with_outputs_nums.append((i, output_idxs))

    total_count = search_dfs(
        all_inputs_with_outputs_nums,
        all_input_labels.index("svr"),
        all_input_labels.index("out"),
        [all_input_labels.index("fft"), all_input_labels.index("dac")],
    )

    print(f"Total paths to 'out' that contain fft and dac: {total_count}")
