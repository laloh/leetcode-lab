"""
Given a string with lowercase letters only, if you are
allowed to replace no more than k letters with any letter
find the length of the longest substring having the same
letter after replacement.

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have the longest
repeating substring 'bbbbb'.
"""

def length_of_longest_substring(str1, k):
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0
    frequency_map = {}

    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
    
        # we don't need to place the mapRepeatLetterCount under the below 'if'
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])

        # current window size is from window_start to window_end, overall we have a letter
        # which is repeating 'max_repeating_letter_count' times, this means we can have
        # a window which has one letter repeating 'max_repeat_letter_count' times and the
        # remaining letter we should replace.
        # if the remaing letter are more than 'k', it is time to shrink the window as we are
        # not allowed to replace more than 'k' letters
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            print("time to shrink the window")
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
        print(f"max_length: {max_length} -- Windows {window_start}, {window_end} -- {str1[window_start:window_end+1]}" )
    return max_length


def main():
  print(length_of_longest_substring("aabccbb", 2))
#   print(length_of_longest_substring("abbcb", 1))
#   print(length_of_longest_substring("abccde", 1))


main() 