import re
x = input("ievadi teksts")
text = re.sub(r'\{[^}]*\}', '', x)
print(text)
