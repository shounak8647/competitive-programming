# def insertionSort(arr):

#     for i in range(1, len(arr)):

#         j = i
#         if arr[i] < arr[i-1]:
#             while j >= 1:
#                 if arr[j] < arr[j-1]:
#                     arr[j], arr[j-1] = arr[j-1], arr[j]
#                     j -= 1
#                 if arr[j] >= arr[j-1]:
#                     break


arr = [10, 50, 30, 20, 40, 90, 70]
# insertionSort(arr)
# print(arr)


def insertS(arr):

    for i in range(1, len(arr)):

        j = i

        if arr[i] < arr[i-1]:
            while j >= 1:
                if arr[j] >= arr[j-1]:
                    break
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1


insertS(arr)
print(arr)
