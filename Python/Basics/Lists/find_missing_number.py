# Problem:
# Find the missing number from 1 to 6.

numbers = [1, 2, 3, 5, 6]

given = sum(numbers)

expected = sum([1, 2, 3, 4, 5, 6])

missing = expected - given

print(missing)

# Output:
# 4
