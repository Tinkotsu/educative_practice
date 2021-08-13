"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
"""
import math


def shortest_window_sort(arr):
    left, right = 0, len(arr) - 1
    for left in range(len(arr) - 1):
        if arr[left + 1] < arr[left]:
            break

    if left == len(arr):
        return 0

    while right >= 0:
        if arr[right - 1] > arr[right]:
            break
        right -= 1

    sub_min = math.inf
    sub_max = -math.inf
    for i in range(left, right + 1):
        sub_min = min(sub_min, arr[i])
        sub_max = max(sub_max, arr[i])

    while left > 0 and arr[left - 1] > sub_min:
        left -= 1

    while right < len(arr) - 1 and arr[right + 1] < sub_max:
        right += 1

    return right - left + 1


print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
print(shortest_window_sort([1, 2, 3]))
print(shortest_window_sort([3, 2, 1]))