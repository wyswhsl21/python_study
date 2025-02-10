#03testdict.py
mysite = {
    'naver': 'www.naver.org',
    'kakao': 'www.kakao.org',
    'python': 'www.python.com'
}
# mysite['naver'] = 'www.naver.org'
# mysite['kakao'] = 'www.kakao.org'
# mysite['python'] = 'www.python.com'
# print(mysite)
for key in mysite:
    print(key, ':', mysite[key])

print("-" * 30)
print(mysite.keys())  #dict_keys(['naver', 'kakao', 'python'])
print()
print(mysite.values()
      )  #dict_values(['www.naver.org', 'www.kakao.org', 'www.python.com'])

for i, e in enumerate(mysite):
    print(i, e, ':', mysite[e])

for k, v in mysite.items():
    print(
        k,
        ':',
        v,
    )
