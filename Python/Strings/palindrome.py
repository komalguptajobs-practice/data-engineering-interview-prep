# Problem:
# Check whether a string is a palindrome without using
# [::-1] or reversed().

text = "madam"
string = ""

for i in text:
    string = i + string

if text == string:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output:
# Palindrome
