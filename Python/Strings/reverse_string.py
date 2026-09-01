# Problem:
# Reverse a string without using [::-1] or reversed().

text = "PYSPARK"
rev = ""

for i in text:
    rev = i + rev

print(rev)

# Output:
# KRAPSYP
