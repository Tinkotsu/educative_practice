"""
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.
"""


def backspace_compare(str1, str2):
    i1, i2 = len(str1) - 1, len(str2) - 1
    while i1 >= 0 or i2 >= 0:
        valid_i1 = get_valid_index(str1, i1)
        valid_i2 = get_valid_index(str2, i2)
        if valid_i1 < 0 and valid_i2 < 0:
            return True
        if valid_i1 < 0 or valid_i2 < 0:
            return False
        if str1[valid_i1] != str2[valid_i2]:
            return False

        i1, i2 = valid_i1 - 1, valid_i2 - 1

    return True

def get_valid_index(str1, index):
    backspace_count = 0
    while index >= 0:
        if str1[index] == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        index -= 1
    return index

print(backspace_compare('xywrrmp', 'xywrrmu#p'))