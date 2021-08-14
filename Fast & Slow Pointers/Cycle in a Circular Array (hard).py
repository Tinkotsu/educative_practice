"""

We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a
particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’
indices. You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the
movement. Write a method to determine if the array has a cycle. The cycle should have more than one element and
should follow one direction which means the cycle should not contain both forward and backward movements.

"""

non_cycle_indexes = set()


def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        if is_cycle_from_current_index(arr, i):
            return True
    return False


def is_cycle_from_current_index(arr, i):
    global non_cycle_indexes
    positive_direction = arr[i] > 0
    slow = fast = i
    while True:
        if slow in non_cycle_indexes or fast in non_cycle_indexes:
            break
        prev_slow = slow
        slow = calculate_next_index(arr, slow)
        if prev_slow == slow:
            break
        fast = calculate_next_index(arr, calculate_next_index(arr, fast))
        if arr[slow] < 0 and positive_direction is True or arr[slow] > 0 and positive_direction is False:
            break
        if slow == fast:
            return True

    non_cycle_indexes.add(i)
    return False


def calculate_next_index(arr, curr_i):
    return (curr_i + arr[curr_i]) % len(arr)


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
