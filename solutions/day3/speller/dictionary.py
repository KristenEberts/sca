"""
Speller in Python
Maria V Zlatkova
CS50 at HSA, July 2018
"""

class Dictionary:
    # Initialize dictionary and create empty set of words
    def __init__(self):
        self.words = set()

    # Check whether given word is present in dictionary
    def check(self, word):
        return word.lower() in self.words

    # Load words from dictionary file
    def load(self, dictionary):
        file = open(dictionary, "r")
        for line in file:
            self.words.add(line.rstrip("\n"))
        file.close()
        return True

    # Return size of dictionary
    def size(self):
        return len(self.words)
