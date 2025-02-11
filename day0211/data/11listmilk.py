# 11listmilk.py

apart = [[101,102,103,104],[201,202,203,204],[301,302,303,304],[401,402,403,404]]

unpaid = [102,204,303,405]
for row in range(0,len(apart),1):
    for col in range(0,len(apart[row]),1):
        if apart[row][col] in unpaid:
            print(f'{0:^3}',end='\t')
      
        else:
            print(apart[row][col],end = '\t')
    print()



# 문제 해결 중첩 for 반복문
# 문제해결 행 층이고 열이 호수 

data = [[1,2,3,4,],[5,6,7,8],[9,10,11,12]]

for row in range(len(data)):
    for col in range(len(data[row])):
        print(data[row][col], end= '\t')
    print()