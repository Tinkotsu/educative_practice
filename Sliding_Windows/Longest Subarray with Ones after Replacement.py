# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
# find the length of the longest contiguous subarray having all 1s.


def length_of_longest_substring(arr: [], k: int) -> int:
    left, result, zeros_count = 0, 0, 0

    for right in range(len(arr)):
        right_char = arr[right]
        if right_char == 0:
            zeros_count += 1

        if zeros_count > k:
            left_dig = arr[left]
            if left_dig == 0:
                zeros_count -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2))
print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3))
