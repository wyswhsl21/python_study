# 딕셔너리 생성 방법 1
mysite = { }
mysite['naver'] = 'www.naver.org'
mysite['kakao'] = 'www.kakao.org'
mysite['python'] = 'www.python.org'
# 딕셔너리 생성 방법 2
mysite_a = {'naver':'www.naver.com','kakao':'www.kakao.com','python':'www.python.com'}
print(mysite)
print(mysite_a)
print('- '*25)
# 문제 1
# 카카오 사이트만 출력해보기
print(f'문제 1 결과 : {mysite['kakao']}')
# 문제 2
# 딕션에 구글 사이트 추가해보기
mysite['google'] = 'www.google.com'
print(f'문제 2 결과 : {mysite['google']}')
# 문제 3
# 기존 키값에 새로운 값을 대입하면, 어떻게 될까
mysite['naver'] = 'www.nanunnugu.com'
print(f'문제 3 결과 : {mysite['naver']}') # 결과 : 덮어씌워진다
print('='*50)
#문제4 카카오 다시 가져오기 get() 키값 검색시 없으면 None출력
print(mysite.get('kakao'))
print(mysite.get('kakao'))
# 문제5 naver키값 있는지 없는지 확인
print('naver'in mysite) # True , False