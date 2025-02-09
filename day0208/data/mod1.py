# 모듈 만들어보기
'''
모듈이란 함수나 변수 또는 클래스를 모아놓은 파이썬 파일인데, 다른 사람이 만들어놓은 모듈을 사용할 수 있고 
내가 직접 만든 모듈을 사용할수도 있다.
'''  

def add(a,b):
    return a+b

def sub(a,b):
    return a-b



if __name__ == " __main__":
    print(add(1,4))
    print(sub(4,2))