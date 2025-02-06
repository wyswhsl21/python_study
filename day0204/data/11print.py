# 11print.py

city = '서울'
avg = 67.56921
grade = 'B'
a , b , mok = 0, 0, 0 
a=19
b = 3
mok = int(a/b)
print('도시 =', city, '\t' , '학점 =', grade)
print('도시 = %s \t 학점 = %s'%(city,grade)) # %d정수  %s문자열  %c한글자
print('도시 = %s \t 학점 = %c'%(city,grade))
print(f'도시 = {city}\t 학점 = {grade}')
print(mok)

print('%d ' %(mok))
print('%.2f' %(mok))

print()