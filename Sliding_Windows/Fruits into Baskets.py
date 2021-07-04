# Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal
# is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type
# of fruit. You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit
# from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type. Write a
# function to return the maximum number of fruits in both baskets.

def fruits_into_baskets(fruits: []) -> int:
    result = 0
    fruits_freq = {}
    left = 0

    for right in range(len(fruits)):
        right_fruit = fruits[right]
        if right_fruit not in fruits_freq:
            fruits_freq[right_fruit] = 0
        fruits_freq[right_fruit] += 1

        while len(fruits_freq) > 2:
            left_fruit = fruits[left]
            fruits_freq[left_fruit] -= 1
            if fruits_freq[left_fruit] == 0:
                del fruits_freq[left_fruit]
            left += 1

        result = max(result, right - left + 1)

    return result


print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
