def firstBadVersion(n):

    left, right = 1, n

    while left < right:

        mid = left + (right - left) // 2

        if isBadVersion(mid) is False:
            left = mid + 1

        else:
            right = mid

    return left
