# Words Concatenation (hard) # Given a string and a list of words, find all the starting indices of substrings in the
# given string that are a concatenation of all the given words exactly once without any overlapping of words.
# It is given that all words are of the same length.


def find_word_concatenation(str1: str, words: []) -> []:
    if len(words) == 0:
        return []

    word_frequency = {}
    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_to_match, word_len = len(words), len(words[0])

    for i in range(len(str1)):
        words_seen = {}
        for j in range(words_to_match):
            start_word_index = i + j * word_len
            word = str1[start_word_index: start_word_index + word_len]

            if word not in words:
                break

            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == words_to_match:
                result_indices.append(i)

    return result_indices
