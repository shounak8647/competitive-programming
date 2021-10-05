import math
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def find_max_cubic_time(arr, i=0):
    n = len(arr)
    loopCount = 0
    max_sum = -199999
    for left in range(0, n):

        for right in range(left, n):
            window_sum = 0
            for k in range(left, right+1):
                window_sum += arr[k]
                loopCount += 1
            max_sum = max(window_sum, max_sum)
    print('Max sum Cubic Time', max_sum, 'Loops', loopCount, 'Array length', n)


find_max_cubic_time(arr=array)


def find_max_quadratic_time(arr, i=0):
    n = len(arr)
    loopCount = 0
    max_sum = None
    for left in range(0, n):
        window_sum = 0
        for right in range(left, n):
            window_sum += arr[right]
            loopCount += 1
            max_sum = window_sum if max_sum is None else max(
                window_sum, max_sum)

    print('Max sum Quadratic Time', max_sum,
          'Loops', loopCount, 'Array length', n)


find_max_quadratic_time(arr=array)


def kadanes_algorith(arr):
    max_sum = -10000
    sum = -10000
    loop_count = 0
    for num in arr:
        sum = max(num, sum+num)
        max_sum = max(sum, max_sum)
        loop_count += 1

    print('Kadanes algorihtm', max_sum, 'Loops',
          loop_count, 'Arraay Length', len(arr))


kadanes_algorith(arr=array)
