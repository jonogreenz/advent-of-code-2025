
def get_all_ranges(id_range1, id_range2):
    if id_range1[1] < id_range2[0] or id_range2[1] < id_range1[0]:
      return [id_range1, id_range2]
    
    new_range = (min(id_range1[0], id_range2[0]), max(id_range1[1], id_range2[1]))
    return [new_range]

def get_all_ranges_merged(id_ranges, id_range):
    # Need to recheck all ranges until no more merges can be made
    merged = True
    current_ranges = id_ranges + [id_range]

    while merged:
      merged = False
      new_ranges = []

      while current_ranges:
          curr_range = current_ranges.pop(0)
          has_merged = False

          for i in range(len(new_ranges)):
              existing_range = new_ranges[i]
              merged_ranges = get_all_ranges(curr_range, existing_range)

              if len(merged_ranges) == 1:
                  new_ranges[i] = merged_ranges[0]
                  has_merged = True
                  merged = True
                  break
              
          if not has_merged:
              new_ranges.append(curr_range)
      current_ranges = new_ranges

    return current_ranges

def total_ids_in_ranges(id_ranges):
    total = 0
    for id_range in id_ranges:
        total += (id_range[1] - id_range[0] + 1)
    return total

if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    id_ranges = []

    collecting_ids = False
    for line in lines:
        line = line.strip()
        if line == "":
            collecting_ids = True
            continue

        if not collecting_ids:
            parts = line.split("-")
            id_ranges.append((int(parts[0]), int(parts[1])))

    all_merged_ranges = []
    for i in range(0, len(id_ranges)):
        all_merged_ranges = get_all_ranges_merged(all_merged_ranges, id_ranges[i])
            
    print (f"Current merged ranges: {all_merged_ranges}")
    print(f"Total of fresh IDs: {total_ids_in_ranges(all_merged_ranges)}")
