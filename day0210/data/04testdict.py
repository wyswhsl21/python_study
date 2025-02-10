#03testdict.py
mysite = {}
mysite['naver'] = 'www.naver.org'
mysite['kakao'] = 'www.kakao.org'
mysite['python'] = 'www.python.com'
print('\nㄴfor k in mysite연습')
for k in mysite:
    print(k, '사이트', mysite[k])
print('\nㄴfor i,e in enumerate(mysite)연습')
for i, e in enumerate(mysite):
    print(i, e, ':', mysite[e])
print('\nㄴfor k,v in mysite.items()연습')
for k, v in mysite.items():
    print(k, ':', v)

print()
print(mysite['kakao'])
print(mysite.get('kakao'))
