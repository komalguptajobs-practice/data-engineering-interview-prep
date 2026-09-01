list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

lis3 = []

for i in lis1:
    if i in lis2:
        lis3.append(i)

print(lis3)
