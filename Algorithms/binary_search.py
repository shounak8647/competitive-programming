def search(nums, target):

    left, right = 0, len(nums) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        elif target > nums[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return -1


nums = [2, 3, 4, 10, 40]
target = 10

result = search(nums, target)


if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
