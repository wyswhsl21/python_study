# 함수의 decoration
import time

def check_time(function):
	def measure(*mlist, **mtuple):
		start_time = time.time()
		result = function(*mlist, **mtuple)
		end_time = time.time()
		print(f"시간측정: {function.__name__}함수에서  {round( end_time - start_time ,5)}")
		return result
	return measure

@check_time 
def myTotal(n):
    total = 0
    for k in range(1, n+1):
        total =  total + k
    return total

myTotal(1000000)
print()
