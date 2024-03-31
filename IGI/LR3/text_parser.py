import re

#This program allows you to
#Calculate number of words that begin with a consonant in the string
#Find words containing two identical letters in a row and their serial numbers in the string
#Sort words in string in alphabetical order in string

def count_consonant_start_words(string):
    """
    Calculates number of words that begin with a consonant
    """
    pattern = r'\b[^aeiouAEIOU\W]\w*\b'
    matches = re.findall(pattern, string)
    return len(matches)

def find_words_with_duplicates(string):
    """
    Finds words containing two identical letters in a row and their serial numbers
    Rerturns List[Tuple(word, it's index)]
    """
    answer = []
    words = string.split()
    for word in words:
        pattern = r"(.)\1"
        match = re.search(pattern, word)
        if(bool(match)):
            answer.append((word, words.index(word) + 1))


    #pattern = r'\b((\w)\1+\b'
    #matches = re.finditer(pattern, string)
    #result = [(match.group(0), string[:match.start()].count(' ') + 1) for match in matches]
    return answer

def sort_words_alphabetically(string):
    """
    Sorts words in string in alphabetical order
    """
    pattern = r'\b\w+\b'
    matches = re.findall(pattern, string)
    sorted_words = sorted(matches)
    return sorted_words
    
def executable_function():
    str = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    print(f"\nNumber of words that begin with a consonant: \n{count_consonant_start_words(str)}\n" +
          f"\nWords with duplicates and their index: \n{find_words_with_duplicates(str)}\n" +
          f"\nSorted string: \n{sort_words_alphabetically(str)}")
