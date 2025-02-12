import re

print()

print('*' * 30)

s = 'Apple is big company and apple is very delicious Apple my Apple'

c = re.compile('apple', re.I)

print(c.findall(s))
c = re.compile('apple')
print(c.findall(s))
