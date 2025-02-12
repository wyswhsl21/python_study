# phone 정규식
import re

data = """
lee 940911-1049118
kim 920711-1059119
goo 980909-1567234
"""

pat = re.compile(r"(\d{6})[-]\d{7}")
print(pat.sub(r"\g<1>-*******",data))



phone = '010-1533-3545 이미니'
call = re.compile(r"(\d{3})-(\d{4})-(\d{4})") # 컴파일로 객체로 만들어 관리

modela = call.sub(r"\g<1>-****-\g<3>",phone) # \g<1> 컴파일 객체의 첫번째꺼를 가져오는거.
print(modela,call)