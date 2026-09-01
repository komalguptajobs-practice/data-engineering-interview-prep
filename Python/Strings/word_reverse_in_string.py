#We need the words in reverse order
text = "I LOVE PYTHON"
words = text.split(' ')
rev = ""
for i in words:
    rev= i+ " " +rev

print(rev)
