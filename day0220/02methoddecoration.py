class MyEST:
    count=3700

    @staticmethod #static이면 클래스 자신 접근 인자 기술하면 에러 self 
    def isSquare(w, h):
        print('isSquare(w,h)함수')
        # print('갯수 =', self.count)
        #정적메소드는 self파라미터사용안함
        area = w * h
        return area
    
    @classmethod # class 메서드는 self 에 접근할 수 있음.
    def printCount(self):
        print('printCount함수')
        print('갯수 =', self.count)
        print()
    
 
MyEST.printCount()
hap=MyEST.isSquare(7,7)
print('합계 =', hap)
