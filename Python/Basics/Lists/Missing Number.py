#The numbers should contain 1 through 7, but one number is missing.
numbers = [1, 2, 3, 5, 6, 7]
sum1=0
sum2=0
for i in range(1,8):
    sum1 = i+sum1

for i in numbers :
    sum2 = i+sum2

if sum1 != sum2:
    diff = sum1-sum2

print(diff)
