import numpy as np
import timeit
import time

# start = timeit.default_timer()

# print('넘피 이용한 * 2 연산')
# my_arr = np.arange(1_000_000)
# my_arr2 = my_arr * 2
# print(my_arr2)
# print()

# start = timeit.default_timer()
# start2 = time.time()

print('일반 list를 이용한 * 2 연산')
my_list = list(range(1, 1_000_001))
my_list2 = [x * 2 for x in my_list]
print(my_list2)

# end = timeit.default_timer()
# end2 = time.time()

# cal = start + end
# cal2 = start2 - end2

# print(f'\n시간차 = {cal}')
print()
