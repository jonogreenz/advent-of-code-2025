

def fewer_than_in_adjacent(grid, x, y, threshold=4):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    count = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] == 1:
                count += 1

    return count < threshold


if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    columns = []

    for line in lines:
        row = [1 if x == '@' else None for x in line.strip()]
        columns.append(row)

    total_count = 0
    for y in range(len(columns)):
        for x in range(len(columns[0])):
            if columns[y][x] == 1:
                if fewer_than_in_adjacent(columns, x, y):
                    total_count += 1

    print(f"Total valid positions: {total_count}")