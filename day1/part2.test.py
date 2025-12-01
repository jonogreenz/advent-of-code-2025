from part2 import run_step

# Ughhh, took me awhile huh...

assert(run_step(50, "L", 49) == (1, 0))
assert(run_step(50, "R", 49) == (99, 0))

assert(run_step(50, "L", 60) == (90, 1))
assert(run_step(50, "R", 60) == (10, 1))

assert(run_step(50, "R", 1000) == (50, 10))
assert(run_step(50, "L", 1000) == (50, 10))

assert(run_step(99, "R", 200) == (99, 2))
assert(run_step(99, "R", 201) == (0, 3))
assert(run_step(1, "L", 200) == (1, 2))
assert(run_step(1, "L", 201) == (0, 3))

assert(run_step(0, "R", 100) == (0, 1))
assert(run_step(0, "L", 100) == (0, 1))

assert(run_step(0, "R", 200) == (0, 2))
assert(run_step(0, "L", 200) == (0, 2))

assert(run_step(0, "L", 199) == (1, 1))
assert(run_step(0, "R", 199) == (99, 1))

assert(run_step(1, "L", 2) == (99, 1))
assert(run_step(99, "R", 2) == (1, 1))

assert(run_step(0, "R", 756) == (56, 7))
assert(run_step(0, "L", 756) == (44, 7))

assert(run_step(55, "L", 55) == (0, 1))
assert(run_step(45, "R", 55) == (0, 1))

assert(run_step(0, "L", 0) == (0, 0))
assert(run_step(0, "R", 0) == (0, 0))

assert(run_step(0, "R", 339) == (39, 3))
assert(run_step(74, "R", 26) == (0, 1))

assert(run_step(0, "R", 101) == (1, 1))
assert(run_step(1, "L", 101) == (0, 2))

assert(run_step(0, "L", 10) == (90, 0))

assert run_step(59, "L", 358) == (1, 3)
