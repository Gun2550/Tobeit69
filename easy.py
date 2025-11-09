text = input()

text = text.lower()

x = "aeiou"

count = 0

for i in text:
    if i in x:
        count += 1

print(count)