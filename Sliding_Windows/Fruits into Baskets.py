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
