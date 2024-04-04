import re

def is_consonant(ch):
    """
    Checks if a character is a consonant.
    Input: single character
    Output: boolean value indicating if the character is a consonant
    """
    return ch not in ('a', 'o', 'u', 'e', 'i', 'y')


def count_consonant_start_words(string):
    """
    Calculates the number of words in a string that begin with a consonant.
    Input: string
    Output: number of words that start with a consonant
    """
    return len([item for item in string.split() if is_consonant(item[0])])


def find_words_with_duplicates(string):
    """
    Finds words in a string that contain two identical letters in a row
    and returns their serial numbers.
    Input: string
    Output: list of tuples (word, index)
    """
    result = {}
    for word_index, word in enumerate(string.split()):
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                result[word] = (word_index + 1, i + 1)
                i +=1
    return result


def sort_words_alphabetically(string):
    """
    Sorts the words in a string in alphabetical order.
    Input: string
    Output: sorted string
    """
    return ' '.join(sorted(string.split(), key=lambda x: x.lower()))


def executable_function():
    """
    User interface function.
    Performs data input and output.
    """
    str = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    print(f"\nNumber of words that begin with a consonant: \n{count_consonant_start_words(str)}\n" +
          f"\nWords with duplicates and their index: \n{find_words_with_duplicates(str)}\n" +
          f"\nSorted string: \n{sort_words_alphabetically(str)}")