import datetime
import time

dt = datetime.datetime.now()
print(dt)
# time.sleep(1) #1초 지연
print()
year = dt.year
month = dt.month
day = dt.day
hour = dt.hour
minute = dt.minute
second = dt.second
ymd = f'{year} 년  {month} 월  {day}일'
hms = f'{hour} 시  {minute} 분  {second} 초'
print(ymd)

print(hms)

print(' -' * 40)
print(dt.strftime('현재날짜 %Y년 %m월 %d일'))
print(dt.strftime('현재시간 %H시 %M분 %S초'))
