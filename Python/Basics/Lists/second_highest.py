# Problem:
# Find the second-highest unique number without using
# max(), sort(), sorted(), or set().

numbers = [10, 50, 20, 80, 40, 80, 30]

seen = []

# Remove duplicates
for i in numbers:
    if i not in seen:
        seen.append(i)

# Find highest
highest = seen[0]

for i in seen:
    if highest < i:
        highest = i

print(highest)

# Remove highest
seen.remove(highest)

# Find second highest
highest = seen[0]

for i in seen:
    if highest < i:
        highest = i

print(highest)

# Output:
# 80
# 50
