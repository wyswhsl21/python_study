import pandas as pd

data = [ ['영희', 2004, 1.2], ['라미', 2019, 8.4] , ['뎅이', 2012, 4.5]]
df = pd.DataFrame(data, columns=['이름','년도','점수'], index=['A', 'B', 'C'])
print(df)
print()


#07DataFrame.py문서
'''
해결1] 열제목  
해결2] 0 1 2 숫자인덱스  대신 A, B, C

   이름    년도   점수
A  영희  2004  1.2
B  라미  2019  8.4
C  뎅이  2012  4.5

쥬피터 !pip install  pandas
쥬피터 !pip install  numpy
쥬피터 !pip install  scikit-learn 
'''







print()
print()
