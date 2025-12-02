line = ""
with open("input.txt") as f:
    line = f.readlines()[0].strip()

ids = line.split(",")

def is_pattern_contained_in_string_at_least_twice(pattern, s):
		pattern_length = len(pattern)
		n = len(s)

		if (n < pattern_length * 2):
				return False

		if (n % pattern_length) != 0:
				return False
		
		for i in range(0, n, pattern_length):
				if s[i : i + pattern_length] != pattern:
						return False
		return True


def is_repeating_sequence(s):
    n = len(s)

    for i in range(1, n):
        substring = s[:i]
        if (is_pattern_contained_in_string_at_least_twice(substring, s)):
            return True
        
    return False


if __name__ == "__main__":
    invalid_ids_total = 0

    for i in range(len(ids)):
        (first, last) = ids[i].split("-")

        first_num = int(first)
        last_num = int(last)

        current_num = first_num
        while current_num <= last_num:
            s = str(current_num)
            if is_repeating_sequence(s):
                invalid_ids_total += current_num
            current_num += 1

    print(f"Total of invalid IDs: {invalid_ids_total}")
