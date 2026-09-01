# Given two strings:str1 = "listen" str2 = "silent" Check whether they are anagrams.
#Two strings are anagrams if they contain the same characters with the same frequencies, regardless of order.
str1 = "listen"
str2 = "silent"

dic1 = {}
dic2 ={}

for i in str1 :
    if i in dic1 : dic1[i]= dic1[i]+1
    else : dic1[i] = 1

for i in str2 :
    if i in dic2 : dic2[i] = dic2[i]+1
    else : dic2[i] = 1

if dic1 ==dic2:
    print ("anagrams")
else :
    print("not anagrams")
