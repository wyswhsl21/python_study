""""
work시리즈]] 문자열에서 암호화  workpassword.py 클래스x,함수x
 문자함수 index(), count(), len(), replace()
 문자열 추출 [시작:끝]
 권장변수  domain, index, pw1,pw2,pw3, password 
# strUrl = "http://kakao.com"   kak50!
# strUrl = "http://geegle.com"  goo63!   
# strurl = "http://naver.com"   nav51!
# strurl = "http://estesoft.com"   est72!
해결1] http:// https://  제외시키고, 도메인이름시작 3글자 접두사 가져오기
해결2] 도메인이름 글자수 ,  e글자포함갯수,  마지막!강제성 

"""


class Secure:

    def __init__(self, email):
        self.email = email
        pass

    def create_password(self):
        remove_domain = self.email.replace('https://', '')
        split_email = (remove_domain.split('.'))
        return (split_email[0][0:3])

    def count_chr(self):
        num = (str(self.email).count('e'))
        print(num)
        return num

    def atob_password(self):
        head = sec.create_password()
        mid = str(sec.count_chr())
        end = '!'
        print(f'생성 된 비밀번호는 {head + (mid) + end}')


email = input('이메일을 입력하시오 >>>')
sec = Secure(email)

sec.atob_password()
