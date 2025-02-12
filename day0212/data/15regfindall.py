import re

msg = 'my best blue Fluit my is blue my'

result1 = re.findall('[a-zA-Z0-9]{3,7}',msg)
result2 = re.findall('blue',msg)

print(result1)
print(result2)

print('- ' * 30)

# 특수문자제외
# 특수문자 추출



pattern = '[^a-zA-Z0-9가-힣\s]' #특수문자만 뽑는 함수 ^ 부정
pattern1 = '[\d]'
msg = 'my best $#@ 오렌지  color @#&%# 345 is orange 쀍뛣혫읅'

result3 = re.findall(pattern,msg)
result4 = re.findall(pattern1,msg)
result5 =re.findall(pattern3,msg)
print('특수문자 제외 결과 =',result3,'\n숫자 추출 결과 =',result4)
print(result5)