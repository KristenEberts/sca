"""
Speller in Python
Maria V Zlatkova
CS50 at HSA, July 2018
"""

from dictionary import Dictionary
import string

def main():
    dict_file = "large.txt"
    text_file = "ralph.txt"

    # Create instance of dictionary
    dictionary = Dictionary()

    # Use class method to load dictionary
    loaded = dictionary.load(dict_file)
    if not loaded:
        print("Could not load dictionary.")

    # Open text file that needs to be spellchecked
    text = open(text_file, "r")
    words = []
    misspelled = []

    # Go through all words in given file, check spelling one by one
    for line in text:
        # line.split() creates list of words from the file,
        # separating them based on spaces
        for word in line.split():

            # Remove punctuation from each word (i.e. commas)
            word = word.translate(None, string.punctuation)

            # ensure there are no non-alphabetical characters in word (i.e. numbers)
            if word.isalpha():
                words.append(word)
                # Check word spelling against word in dictionary
                if not dictionary.check(word):
                    misspelled.append(word)
    text.close()

    print("Total number of words in text: " + str(len(words)))
    print("Number of misspelled words: " + str(len(misspelled)))
    print("Misspelled words:")
    print(misspelled)

if __name__ == '__main__':
    main()
