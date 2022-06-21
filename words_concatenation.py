"""
Given a string and a list of words, find all the starting indices of substring
in the given string that are a concatenation of all the given words exactly
once without any overlapping of words. It is given that all words are of the
same length.

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: Thw two substring containing both the words are "catfox" & "foxcat"
"""

def find_word_concatenation(str1, words):
    if len(words) == 0 or len(words[0]) ==0:
        return []
    
    words_frequency = {}

    for word in words:
        if word not in words_frequency:
            words_frequency[word] = 0
        words_frequency[word] += 1
    
    result_indices = []
    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(str1) - words_count * word_length ) + 1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_length
            word = str1[next_word_index: next_word_index + word_length]
            if word not in words_frequency:
                break
            
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            if words_seen[word] > words_frequency.get(word, 0):
                break
            
            if j + 1 == words_count:
                result_indices.append(i)

    return result_indices


def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()

