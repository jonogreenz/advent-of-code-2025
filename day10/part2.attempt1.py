import re


def perform_button_press(joltages, button):
    new_joltages = joltages.copy()
    for index in button:
        new_joltages[index] += 1
    return new_joltages


def invalid_joltage(joltages, requirement):
    for i in range(len(joltages)):
        if joltages[i] > requirement[i]:
            return True
    return False


def configure_machine(machine):
    light_configuration, buttons, joltage_requirements = machine

    initial_joltages = [0] * len(joltage_requirements)

    queue = []
    for button in buttons:
        queue.append((button, initial_joltages, [button]))

    seen_joltages = set()

    while queue:
        current_button, current_joltage, existing_buttons = queue.pop(0)

        new_joltage = perform_button_press(current_joltage, current_button)

        if tuple(new_joltage) in seen_joltages:
            continue
        seen_joltages.add(tuple(new_joltage))

        if invalid_joltage(new_joltage, joltage_requirements):
            # print(f"Invalid joltage reached: {new_joltage}")
            continue

        for button in buttons:
            queue.append((button, new_joltage, existing_buttons + [button]))

        # print(
        #     f"Current joltage: {current_joltage}, new joltage: {new_joltage}, presses: {presses}"
        # )

        if new_joltage == joltage_requirements:
            # print(f"Found configuration with {presses} presses")
            return len(existing_buttons)

    return -1


if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    machines = []
    for line in lines:
        match1 = re.search(r"\[(.+)\]", line)
        match2 = re.search(r"\((.*)\)", line)
        match3 = re.search(r"{(.+)}", line)

        light_configurations = [True if c == "#" else False for c in match1.group(1)]

        button_groups = match2.group(0).split(" ")
        buttons = []
        for bg in button_groups:
            b = bg.removeprefix("(").removesuffix(")")
            button_indices = [int(v) for v in b.split(",")]
            buttons.append(button_indices)

        joltage = [int(v) for v in match3.group(1).split(",")]

        machines.append((light_configurations, buttons, joltage))

    total_presses = 0
    for i, machine in enumerate(machines):
        # Find lowest amount of button presses to make joltage go to requirements
        lowest_presses = configure_machine(machine)
        print(f"Lowest presses for machine {i}: {lowest_presses}")
        total_presses += lowest_presses

    print(f"Total presses for all machines: {total_presses}")
