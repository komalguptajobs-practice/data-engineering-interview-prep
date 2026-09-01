#Remove Duplicates While Preserving Order
text = "aabbcde"
seen = []
dup = []
result = ""
for i in text :
    if i in seen : dup.append(i)
    else :
        seen.append(i)
    if i in seen and i not in dup:
        result = result +i


print(result)
