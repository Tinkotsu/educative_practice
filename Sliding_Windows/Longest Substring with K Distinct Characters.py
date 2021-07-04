# Given a string, find the length of the longest substring in it with no more than K distinct characters.
# You can assume that K is less than or equal to the length of the given string.

import math


def longest_substring_with_k_distinct(str1: str, k: int) -> int:
    result, left = -math.inf, 0
    char_frequency = {}

    for right in range(len(str1)):
        if str1[right] not in char_frequency:
            char_frequency[str1[right]] = 0
        char_frequency[str1[right]] += 1

        while len(char_frequency) > k:
            char_frequency[str1[left]] -= 1
            if char_frequency[str1[left]] == 0:
                del char_frequency[str1[left]]
            left += 1

        result = max(result, right - left + 1)

    return result
