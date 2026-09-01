numbers = [10, 50, 20, 80, 40, 30]
seen =[]
dup =[]
for i in numbers:
    if i in seen: dup.append(i)
    else : seen.append(i)

print(seen)
largest = seen[0]
for i in seen:
    if largest< i: largest=i

seen.remove(largest)
largest = seen[0]

for i in seen:
    if largest<i : largest =i

print(largest)
