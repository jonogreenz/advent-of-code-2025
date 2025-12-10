import re


def perform_button_press(configuration, button):
    new_configuration = configuration.copy()
    for index in button:
        new_configuration[index] = not new_configuration[index]
    return new_configuration


def configure_machine(machine):
    light_configuration, buttons, joltage = machine

    initial_configuration = [False] * len(light_configuration)

    queue = []
    for button in buttons:
        queue.append((button, initial_configuration, 1))

    seen_configurations = set()

    while queue:
        current_button, current_configuration, presses = queue.pop(0)

        new_configuration = perform_button_press(current_configuration, current_button)

        if tuple(new_configuration) in seen_configurations:
            continue
        seen_configurations.add(tuple(new_configuration))

        for button in buttons:
            if (
                button != current_button
            ):  # Avoid pressing the same button twice in a row as that's redundant
                queue.append((button, new_configuration, presses + 1))

        # print(
        #     f"Current configuration: {current_configuration}, new configuration: {new_configuration}, presses: {presses}"
        # )

        if new_configuration == light_configuration:
            # print(f"Found configuration with {presses} presses")
            return presses

    return 0


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
        # Find lowest amount of button presses to make lights go to configuration
        lowest_presses = configure_machine(machine)
        print(f"Lowest presses for machine {i}: {lowest_presses}")
        total_presses += lowest_presses

    print(f"Total presses for all machines: {total_presses}")
