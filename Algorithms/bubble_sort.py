def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swap = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True

        if swap == False:
            break

        print('Res:', arr)


arr = [5, 1, 4, 2, 8, 9, 10, 11]
bubbleSort(arr)
