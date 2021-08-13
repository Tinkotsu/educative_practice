"""
Given an array with positive numbers and a positive target number,
find all of its contiguous subarrays whose product is less than the target number.
"""


def find_subarrays(arr: [], target: int) -> []:
    result = []

    for left in range(len(arr)):
        curr_product = 1
        for right in range(left, len(arr)):
            curr_product *= arr[right]
            if curr_product < target:
                result.append(arr[left:right + 1])
            else:
                break

    return result


print(find_subarrays([2, 5, 3, 10], 30))
print(find_subarrays([8, 2, 6, 5], 50))