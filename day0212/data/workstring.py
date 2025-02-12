# workstring.py

msg = '   this is a python    '

a = msg.strip()  # 공백제거
b = msg.replace(' ', '')  # 모든 공백제거
print(''.join(msg))

print('앞 뒤 공백제거= ', a, '모든 공백제거 = ', b, msg, end=' ')
