"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the
square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead,
they will be stuck in a cycle of numbers which does not include ‘1’.
"""


def find_happy_number(num):
    slow = fast = num
    while True:
        slow = get_square_sum(slow)
        fast = get_square_sum(get_square_sum(fast))
        if slow == fast:
            break
    return slow == 1


def get_square_sum(num):
    _sum = 0
    while num > 0:
        _sum += (num % 10) ** 2
        num //= 10
    return _sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()

"""
Space complexity is O(logN)
Time complexity is O(1)
"""
