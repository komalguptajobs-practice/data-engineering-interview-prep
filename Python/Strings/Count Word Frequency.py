#Count Word Frequency
text = "python is easy and python is powerful"
x=[]
x= text.split(' ')
dic ={}

for i in x:
    if i in dic : dic[i] = dic[i]+1
    else : dic[i] = 1

print(dic)
