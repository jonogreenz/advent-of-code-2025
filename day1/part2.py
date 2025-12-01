lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

current = 50

wrap_around = 100

count = 0

def run_step(current, direction, distance):
    if direction == "L":
        new_position_without_wrap = current - distance
        new_position = new_position_without_wrap % wrap_around
        
        if current != 0 and new_position_without_wrap <= 0:
            passes = (-new_position_without_wrap) // wrap_around + 1
        elif current == 0:
            passes = distance // wrap_around
        else:
            passes = 0
        return new_position, passes
    elif direction == "R":
        new_position_without_wrap = current + distance
        new_position = new_position_without_wrap % wrap_around
        
        if new_position_without_wrap >= wrap_around:
            passes = new_position_without_wrap // wrap_around
        else:
            passes = 0
        return new_position, passes
    raise ValueError("Direction must be 'L' or 'R'")


if __name__ == "__main__":
    for i in range(len(lines)):
        direction = lines[i][0]
        distance = int(lines[i][1:])

        run_step_result = run_step(current, direction, distance)
        print(
            f"Direction: {direction}, Distance: {distance}, Current: {current} -> New Current: {run_step_result[0]}, Passes: {run_step_result[1]}"
        )

        current = run_step_result[0]
        count += run_step_result[1]

    print(f"Total times at position 0: {count}")
