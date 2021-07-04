# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
# find the length of the longest substring having the same letters after replacement.

def length_of_longest_substring(str1: str, k: int) -> int:
    left, result, max_repeat_letter_count = 0, 0, 0
    chars_freq = {}

    for right in range(len(str1)):
        right_char = str1[right]
        if right_char not in chars_freq:
            chars_freq[right_char] = 0
        chars_freq[right_char] += 1
        max_repeat_letter_count = max(max_repeat_letter_count, chars_freq[right_char])

        if right - left + 1 - max_repeat_letter_count > k:
            left_char = str1[left]
            chars_freq[left_char] -= 1
            if chars_freq[left_char] == 0:
                del chars_freq[left_char]
            left += 1

        result = max(result, right - left + 1)

    return result


print(length_of_longest_substring("abcz", k=2))
print(length_of_longest_substring("abbcb", k=1))
print(length_of_longest_substring("abccde", k=1))
