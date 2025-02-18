import numpy as np
import timeit

start = timeit.default_timer()

print('넘피 이용한 * 2 연산')
my_arr = np.arange(1_000_000)
my_arr2 = my_arr * 2
print(my_arr2)
print()

# start = timeit.default_timer()
# print('일반 list를 이용한 * 2 연산')
# my_list = list(range(1_000_000))
# my_list2 = [x * 2 for x in my_list]
# print(my_list2)
print()
