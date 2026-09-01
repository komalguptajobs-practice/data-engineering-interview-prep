# Problem:
# Find duplicate numbers in a list without using set().

numbers = [1, 2, 3, 2, 4, 1, 5, 3]

seen = []
duplicates = []

for i in numbers:
    if i in seen:
        duplicates.append(i)
    else:
        seen.append(i)

print(duplicates)

# Output:
# [2, 1, 3]
