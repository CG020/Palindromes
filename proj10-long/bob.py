'''
File: bob.py
Author: Camila Grubb
Course: CSC 120
Purpose: This program goes through data sets and prints out the palindromes
from the data list itself and the palindromes that can be formed when
combining words from the data set.
'''


def read_file(file):
    """
    This function reads the inputted file. It breaks the file up by lines,
    checks if each character in the file is a letter, checks that the words
    being collected are greater than two characters, and sets the characters
    to lowercase letters. All the valid items are added to a set to avoid
    duplication.
    :param file: a txt file
    :return: a set of strings
    """
    read_file, word_set = open(file, "r").readlines(), set()
    for item in read_file:
        # splits each file line by spaces to create list of words
        temp = item.split(" ")
        for word in temp:
            temp_word = ""
            # goes through each character in the word to check is letter
            for index in word:
                if index.isalpha():
                    # if it is a letter adds it as a lowercase
                    temp_word += index.lower()
            # checks if the word length is more than 2
            if len(temp_word) < 2:
                temp_word = ""
            if temp_word:
                word_set.add(temp_word)
    return word_set


def dump(word_set):
    """
    This function prints out all the words in the orginal data set in
    alphabetical order.
    :param word_set: a set of strings
    """
    sorted_list = sorted(word_set)
    print("WORD LIST:")
    for word in sorted_list:
        print(" " + word)


def simple_palindromes(text):
    '''
    This function prints out the palindromes from the data set sorted.
    :param text: a set of strings
    '''
    print("1-WORD PALINDROMES:")
    palins = set()
    for word in text:
        # checks if the word in the set is a palindrome
        if word == word[::-1]:
            palins.add(word)
    # sorts palins (for sanity sake) and prints out the sorted palindromes
    palins = sorted(palins)
    for word1 in palins:
        print("  " + word1)
    print("")

def t_word_palindromes(words_set):
    '''
    This function prints out all the palindromes formed by combining 2 and 3
    words to the original word.
    :param words_set: a set of strings
    '''
    print("2-WORD AND 3-WORD PALINDROMES:")
    palins = set()
    # iterates through the words
    for word in words_set:
        # iterates a second time
        for word2 in words_set:
            # checks the words against themselves to add existing palindromes
            if word == word2[::-1]:
                palins.add(word + word2)
            # adds the words together to check if them combined are palindromes
            if word + word2 == (word + word2)[::-1]:
                palins.add(word+word2)
            # adds three words together to check if a palindrome can be formed
            for word3 in words_set:
                temp = word + word2 + word3
                if temp == temp[::-1]:
                    palins.add(word+word2+word3)
    # sorts through the new palindromes for sanity sake
    palins = sorted(palins)
    for word in palins:
        print("  " + word)
    print("")


def palindrome(num, words):
    '''
    This function iterates through the set of words for how many times the
    user inputs and prints out the palindromes that form from combining
    words in the set.
    :param num: an integer
    :param words: a set of strings
    '''
    # creates a dictionary
    words_dict = dict()

    # makes a key for all the numbers within the range of the number the user
    # inputs
    for x in range(1, num+1):
        words_dict[x] = set()

    # adds the set words to teh dictionary in their proper places
    for word in words:
        if len(word) in words_dict:
            words_dict[len(word)].add(word)

    # iterates for the integer number inputted
    for x in range(1, num+1):
        # prints the header
        print(f"PALINDROMES OF LENGTH {x}    - length of "
              f"candidate list: {len(words_dict[x])}")
        # iterates through the sorted item in the current dictionary index
        for item in sorted(words_dict.get(x)):
            # if it is a palindrome, the word is printed
            if item == item[::-1]:
                print("  " + item)
            else:
                # otherwise, iterates through each word in the set of og words
                for word in words:
                    # checks if the word is not a palindrome
                    if word != word[::-1]:
                        # combines the current word and the set word
                        new_word = item + word
                        # adds the word to the dictionary of a key exists for
                        # that length of word
                        if len(new_word) in words_dict.keys():
                            words_dict[len(new_word)].add(new_word)
        print("")

def main():
    try:
        file = read_file(input())
        command = input()
        if command == "dump":
            dump(file)
        else:
            simple_palindromes(file)
            t_word_palindromes(file)
            palindrome(int(command), file)
    except FileNotFoundError:
        print("ERROR: Could not open the input file: BAD_FILENAME")

if __name__ == "__main__":
    main()