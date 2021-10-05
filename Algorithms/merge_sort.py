# def mergeSort(arr):
#     if len(arr) > 1:

#         mid = len(arr) // 2
#         L = arr[:mid]
#         R = arr[mid:]

#         mergeSort(L)
#         mergeSort(R)

#         i = j = k = 0

#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1

#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

#     print(arr)


array = [12, 11, 13, 5, 7, 6]
# mergeSort(array)


def merge(arr1, arr2, cpy):

    i = j = k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            cpy[k] = arr1[i]
            i += 1
        else:
            cpy[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        cpy[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        cpy[k] = arr2[j]
        j += 1
        k += 1

    return cpy


def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)
        merge(L, R, arr)


mergeSort(array)
print(array)
