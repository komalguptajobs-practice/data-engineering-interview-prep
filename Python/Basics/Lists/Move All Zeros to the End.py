numbers = [0, 1, 0, 3, 12]
new =[]
zeros = 0


for i in numbers :
    if i!=0 :
        new.append(i)
    else :
        zeros = zeros + 1

for i in range(zeros):
    new.append(0)

print(new)
