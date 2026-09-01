#removing duplicate characters while keeping the original order.
text = "programming"
result =  ""
seen = []

for i in text :
    if i not in seen:
        seen.append(i)
        result = result+i

print(result)
