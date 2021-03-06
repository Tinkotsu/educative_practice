"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
"""

def pair_with_targetsum(arr: [], target_sum: int) -> []:
    left, right = 0, len(arr) - 1
    while left != right:
        cur_sum = arr[left] + arr[right]
        if cur_sum == target_sum:
            return [left, right]
        elif cur_sum < target_sum:
            left += 1
        elif cur_sum > target_sum:
            right -= 1

    return [-1, -1]