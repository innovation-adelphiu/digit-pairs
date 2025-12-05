import itertools
import random

digits = list(range(10))

# Generate all pairings
def generate_pairings(nums):
    if not nums:
        yield []
        return
    a = nums[0]
    for i in range(1, len(nums)):
        b = nums[i]
        rest = nums[1:i] + nums[i+1:]
        for pairs in generate_pairings(rest):
            yield [(a, b)] + pairs

valid_tuples = set()

for pairing in generate_pairings(digits):
    sums = sorted(a + b for (a, b) in pairing)

    # Filters
    if any(s < 3 for s in sums):
        continue
    if any(s > 15 for s in sums):
        continue
    if len(set(sums)) != 5:
        continue

    valid_tuples.add(tuple(sums))

# Convert to list and shuffle
valid_list = list(valid_tuples)
random.shuffle(valid_list)

# Print results in numbered list
print("Number of puzzles: ", len(valid_list))
for i, t in enumerate(valid_list, start=1):
    print(f"{i}. {t}")
