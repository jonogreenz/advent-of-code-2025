lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

current = 50

wrap_around = 100

count = 0

for i in range(len(lines)):
    direction = lines[i][0]
    distance = int(lines[i][1:])

    if direction == "L":
        current = (current - distance) % wrap_around
    elif direction == "R":
        current = (current + distance) % wrap_around

    print(f"Direction: {direction}, Distance: {distance}, Current: {current}")

    if current == 0:
        print("At position 0, found the exit!")
        count += 1

print(f"Total times at position 0: {count}")
