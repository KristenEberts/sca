"""
Rap Lexicon
Spencer L Tiberi
CS50 at HSA, July 2018
"""

import os

def main():
    rappertexts = []

    # Directory where lyrics are stored
    directory = os.fsencode("lyrics/")

    # Fill list of rappers with txt filenames
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith(".txt"):
            rappertexts.append(filename)
            continue
        else:
            continue

    # Create a dict that has a rapper name and then set of words
    rappers = dict()

    # Fill dict of words with value of frequency and prints name, wordcount, etc. to screen
    for rappertext in rappertexts:
        words = fill_words(rappertext)
        # Create rapper name from filefame (remove .txt and capitalize)
        rapper_name = rappertext[:-4].capitalize()

        # TODO: Add comment
        rappers[rapper_name] = words

        # Create a dotted line for formating based on length of the rapper's name
        line = "." * (40 - len(rapper_name))

        print("%s%s\n\tWord Count: %s\n\tLargest Word: %s\n\tMost Used Word: %s" % \
              (rapper_name, line, len(rappers[rapper_name]), \
              max(rappers[rapper_name], key=len), max(rappers[rapper_name], \
              key=rappers[rapper_name].get)))

    while True:
        rapper = input("Choose a rapper to further examine (or type 'quit'): ")

        if rapper == 'quit':
            break
        elif rapper in rappers:
            examine_rapper(rappers[rapper], rapper)
        else:
            print("Invalid rapper!")

# Fills and returns a set of words for a given rapper file
def fill_words(rapper):
    words = []

    with open("lyrics/" + rapper, "r") as f:
        words = f.read().split()

    word_usage = {word: words.count(word) for word in set(words)}

    return word_usage

# Examines the number of times the rapper uses a user-inputted word
def examine_rapper(rapper_dict, name):
    word = input("Type a word the rapper uses: ")
    if word in rapper_dict:
        print("%s: %s uses by %s" % (word, rapper_dict[word], name))
    else:
        print("No uses of %s!" % word)

if __name__ == '__main__':
    main()
