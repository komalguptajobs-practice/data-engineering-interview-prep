#Find the first character that appears only once.
text = "aabbcde"
seen =[]
dup = []
for i in text:
    if i in seen : dup.append(i)
    else : seen.append(i)

for i in seen:
    if i not in dup :
        value = i
        break

print(value)
