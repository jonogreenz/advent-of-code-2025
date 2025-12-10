import re

# Linear algebra solver to the rescue
from pulp import LpMinimize, LpProblem, LpVariable, LpInteger, lpSum


def configure_machine(machine):
    # Goal is to minimise the total presses of buttons to reach the joltage requirements
    #
    # Linear equation since effectively button1 * x + button2 * y + ... = joltage_requirement
    #
    # We want to minimise: x + y + ...
    # And requirement[i] = sum of button presses affecting position i

    light_configuration, buttons, joltage_requirements = machine

    problem = LpProblem("JoltageSolver", LpMinimize)

    independent_vars = []
    for i, button in enumerate(buttons):
        independent_var = LpVariable(f"button{i}", lowBound=0, cat=LpInteger)
        independent_vars.append(independent_var)

    # Okay but wtf is this overloaded syntax

    # Objective
    problem += lpSum(independent_vars), "TotalButtonPresses"

    # Constraints
    for joltage_idx in range(len(joltage_requirements)):
        joltage_contribution = []
        for i, button in enumerate(buttons):
            dependent_var = button.count(joltage_idx)
            joltage_contribution.append(dependent_var * independent_vars[i])

        problem += (
            lpSum(joltage_contribution) == joltage_requirements[joltage_idx],
            f"Requirement{joltage_idx}",
        )

    problem.solve()

    total_presses = sum(int(var.varValue) for var in independent_vars)
    print(f"Button presses: {[int(var.varValue) for var in independent_vars]}")
    return total_presses


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
