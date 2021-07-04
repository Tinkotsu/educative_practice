# Given a string and a pattern, find out if the string contains any permutation of the pattern.
#
# Permutation is defined as the re-arranging of the characters of the string.
# For example, “abc” has the following six permutations:
#
# 1. abc
# 2. acb
# 3. bac
# 4. bca
# 5. cab
# 6. cba
#
# If a string has ‘n’ distinct characters, it will have n!n! permutations.


def find_permutation(str1: str, pattern: str) -> bool:
    left, matched = 0, 0
    chars_freq = {}

    # create a map of chars frequencies in pattern
    for char in pattern:
        if char not in chars_freq:
            chars_freq[char] = 0
        chars_freq[char] += 1

    for right in range(len(str1)):
        right_char = str1[right]
        if right_char in chars_freq:
            chars_freq[right_char] -= 1
            if chars_freq[right_char] == 0:
                matched += 1

        if matched == len(chars_freq):
            return True

        if right >= len(pattern) - 1:
            left_char = str1[left]
            left += 1
            if left_char in chars_freq:
                if chars_freq[left_char] == 0:
                    matched -= 1
                chars_freq[left_char] += 1

    return False


find_permutation('odicf', 'dc')