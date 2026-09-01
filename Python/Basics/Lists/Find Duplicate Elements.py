#Find all duplicate numbers, but each duplicate should appear only once.
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
seen =[]
dup =[]
filtered = []

for i in numbers:
    if i in seen and i not in dup : dup.append(i)
    else : seen.append(i)

print(dup)
