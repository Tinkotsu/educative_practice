# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray
# whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

import math


def smallest_subarray_with_given_sum(s: int, arr: []) -> int:
    result = math.inf
    left, right, curr_sum = 0, 0, 0

    for right in range(len(arr)):
        curr_sum += arr[right]
        while curr_sum >= s:
            result = min(right - left + 1, result)
            curr_sum -= arr[left]
            left += 1

    return 0 if result == math.inf else result


res = smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])
print(f'my: {res} | actual: 3')
