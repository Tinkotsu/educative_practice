"""
Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space;
after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
"""


def remove_duplicates(arr):
    if len(arr) == 0:
        return 0
    left = 1

    for right in range(1, len(arr)):
        if arr[left - 1] != arr[right]:
            arr[left] = arr[right]
            left += 1

    return left

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))