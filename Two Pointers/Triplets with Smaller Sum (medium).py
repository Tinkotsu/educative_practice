"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that
arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
Write a function to return the count of such triplets.
"""


def triplet_with_smaller_sum(arr, target):
    count = 0
    arr.sort()

    for i in range(len(arr) - 2):
        j = i + 1
        k = len(arr) - 1
        while j < k:
            if arr[i] + arr[j] + arr[k] < target:
                count += k - j  # arr[k] can be replaced with any arr[j:k]
                j += 1
            else:
                k -= 1
    return count
