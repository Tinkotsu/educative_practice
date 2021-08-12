"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
"""


def search_triplets(arr: []) -> [[]]:
    triplets = []
    arr.sort()

    for start in range(len(arr) - 2):
        if start > 0 and arr[start] == arr[start - 1]:
            continue
        pair_with_target_sum(arr, -arr[start], start + 1, triplets)
    return triplets


def pair_with_target_sum(arr: [], target_sum: int, left: int, triplets: [[]]):
    right = len(arr) - 1
    while left < right:
        cur_sum = arr[left] + arr[right]
        if cur_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while right > left and arr[right] == arr[right + 1]:
                right -= 1
        elif cur_sum < target_sum:
            left += 1
        elif cur_sum > target_sum:
            right -= 1


def main():
    print(search_triplets([-5, 2, -1, -2, 3]))
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))


main()
