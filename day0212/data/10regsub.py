import re

# 10regsub.py

old_text = 'The color is blue'
new_text = re.sub('blue', 'red', old_text)
print(old_text)
print(new_text)

print(old_text.replace('blue', 'red'))

data = "Python Good best Python"

pattern = "Python"

my = re.match(pattern, data)
print(my)
if my:
    print('패턴의 일치 ~~~ ok',my.group())
else:
    print('패턴의 불일치')
