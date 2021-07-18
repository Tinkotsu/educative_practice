"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order
"""


def make_squares(arr):
    squares = []
    left, right = 0, len(arr) - 1

    while left <= right:
        left_sq = arr[left] * arr[left]
        right_sq = arr[right] * arr[right]
        if left_sq > right_sq:
            squares.insert(0, left_sq)
            left += 1
        else:
            squares.insert(0, right_sq)
            right -= 1

    return squares


print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))