def two_pointer(a, n, val):

    for i in range(n):
        for j in range(n):

            if i == j:
                continue

            if a[i] + a[j] == val:
                print(a[i], a[j])
                return True

            elif a[i] + a[j] > val:
                break

    return 0


arr = [3, 5, 9, 2, 8, 10, 11]
val = 17

# two_pointer(arr, len(arr), val)


def two_pointer_n(a, n, val):
    i = 0
    j = n - 1

    for k in range(n):

        if i > j:
            break

        if a[i] + a[j] == val:
            print(a[i], a[j])
            return True

        elif a[i] + a[j] < val:
            i += 1

        elif a[i] + a[j] > val:
            j -= 1

    return 0


arr = [3, 5, 9, 2, 8, 10, 11]
val = 17

two_pointer_n(arr, len(arr), val)
