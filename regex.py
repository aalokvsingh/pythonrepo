import re

line = "pet:cat ilove cats"
line1 = "i love cats pet:cat"
line2 = "pet:cat i love cats pet:cow i love cows"


m = re.match(r"pet:\w\w\w", line2)
print(m.group(0))

k = re.search(r"pet:\w\w\w", line2)
print(k.group(0))

t = re.findall(r"pet:\w\w\w", line2)
print(t.group(0))

x = re.finditer(r"pet:\w\w\w", line2)
print(x.group(0))

