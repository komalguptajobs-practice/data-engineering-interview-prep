# Problem:
# Find the maximum number in a list without using max().

numbers = [5, 20, 28, 4, 93, 11]

highest = numbers[0]

for i in numbers:
    if i > highest:
        highest = i

print(highest)

# Output:
# 93
