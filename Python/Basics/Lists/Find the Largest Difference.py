#Find the difference between the largest and smallest number.
num = [10, 5, 8, 20, 3]
largest = num[0]
smallest = num[0]

for i in num:
    if i>largest :
        largest =i
    elif i<smallest :
        smallest=i

diff = largest - smallest
print(diff)
