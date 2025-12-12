import re

if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    all_regions = []
    all_shapes = []

    # Wow this is messy from before lol
    currently_getting_shapes = False
    current_shape_index = -1
    current_shape = []
    for line in lines:
        if line.strip() == "":
            if currently_getting_shapes:
                all_shapes.append(current_shape)
                current_shape = []
            currently_getting_shapes = False
            continue

        index = re.search(r"\d:", line)
        region = re.search(r"(\d+)x(\d+): (.*)", line)

        if region:
            width = int(region.group(1))
            height = int(region.group(2))
            required_counts = [int(v) for v in region.group(3).split(" ")]
            all_regions.append((width, height, required_counts))

        if index:
            current_shape_index += 1
            currently_getting_shapes = True
            continue

        if currently_getting_shapes:
            shape_line = [c == "#" for c in line.strip()]
            current_shape.append(shape_line)
            continue

    total_count_per_shape = [0 for _ in all_shapes]
    for i, shape in enumerate(all_shapes):
        for row in shape:
            total_count_per_shape[i] += sum(1 for cell in row if cell)

    regions_that_might_allow_packing = []
    for i, region in enumerate(all_regions):
        region_width, region_height, required_counts = region
        region_size = region_width * region_height

        total_region_filled = 0
        for j, count in enumerate(required_counts):
            total_region_filled += total_count_per_shape[j] * count

        if total_region_filled < region_size:
            regions_that_might_allow_packing.append(region)

    print(f"\nRegions that might allow packing: {len(regions_that_might_allow_packing)} out of {len(all_regions)}")