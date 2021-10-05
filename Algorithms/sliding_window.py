def sliding_window(arr, k):

    max_sum = 0

    if len(arr) < k:
        print('Invalid input array')

    for i in range(0, len(arr) - k + 1):
        window_sum = 0
        for idx in range(i, i+k):
            window_sum += arr[idx]
        max_sum = max(window_sum, max_sum)

    print(max_sum)


array = [1, 2, 3, 4, 5, 6, 7, 8]

sliding_window(array, 3)
