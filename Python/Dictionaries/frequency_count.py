# Problem:
# Count how many times each number occurs in a list.

numbers = [1, 2, 3, 2, 4, 1, 2, 5, 3]

dic = {}

for i in numbers:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1

print(dic)

# Output:
# {1: 2, 2: 3, 3: 2, 4: 1, 5: 1}
