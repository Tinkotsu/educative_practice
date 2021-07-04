# Given a string and a pattern, find all anagrams of the pattern in the given string.
#
# Every anagram is a permutation of a string.
# As we know, when we are not allowed to repeat characters while finding permutations of a string,
# we get N! permutations (or anagrams) of a string having NN characters.
# For example, here are the six anagrams of the string “abc”:
#
# 1. abc
# 2. acb
# 3. bac
# 4. bca
# 5. cab
# 6. cba
# "ad[bcbe]fe" "feed"
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.


def find_string_anagrams(str1: str, pattern: str) -> []:
    result_indexes = []
    left, matched = 0, 0
    chars_freq = {}

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
            result_indexes.append(left)

        if right >= len(pattern) - 1:
            left_char = str1[left]
            left += 1
            if left_char in chars_freq:
                if chars_freq[left_char] == 0:
                    matched -= 1
                chars_freq[left_char] += 1

    return result_indexes


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
