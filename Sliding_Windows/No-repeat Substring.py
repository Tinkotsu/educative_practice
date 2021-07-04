# Given a string, find the length of the longest substring, which has no repeating characters.

def non_repeat_substring(str1: str) -> int:
    result = 0
    left = 0
    chars_index_map = {}

    for right in range(len(str1)):
        right_char = str1[right]

        if right_char in chars_index_map:
            left = max(left, chars_index_map[right_char] + 1)

        chars_index_map[right_char] = right
        result = max(result, right - left + 1)

    return result


print(non_repeat_substring("aabccbb"))
print(non_repeat_substring("abbbb"))
print(non_repeat_substring("abccde"))
