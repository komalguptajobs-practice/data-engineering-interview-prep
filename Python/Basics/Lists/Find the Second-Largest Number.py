numbers = [10, 50, 20, 80, 40, 30]

largest = numbers[0]

for i in numbers:
    if largest < i:
        largest = i

numbers.remove(largest)

largest = numbers[0]

for i in numbers:
    if largest < i:
        largest = i

print(largest)
