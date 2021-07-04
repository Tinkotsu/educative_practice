# Given a string and a pattern,
# find the smallest substring in the given string which has all the characters of the given pattern.


def find_substring(str1: str, pattern: str) -> str:
    matched, left, min_len, sub_str_start = 0, 0, len(str1) + 1, 0
    result = ""
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

        while matched == len(pattern):
            if min_len > right - left + 1:
                min_len = right - left + 1
                sub_str_start = left

            left_char = str1[left]
            left += 1
            if left_char in chars_freq:
                if chars_freq[left_char] == 0:
                    matched -= 1
                chars_freq[left_char] += 1

    return "" if min_len > len(str1) else str1[sub_str_start:sub_str_start + min_len + 1]


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))


main()
