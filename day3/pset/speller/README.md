# Speller

## TL;DR

Implement a program that spell-checks a file, per the below.

## Background

### Learning goals

Let's build ourselves a very simple spellchecker and actually use it to check the spelling of a number of texts! We're going to do so using Python to implement our spellchecked, but first we're going to take a look at **classes**, **methods** and **file input/output**.

### Classes

In the real world, there are often entities that we want to represent that aren't fully covered by simple data types like integers and strings or by data structures like lists and dictionaries. Turns out, it's really useful to have a way to represent more complex entities, especially if you have many of them! For example, in the case of products like Facebook or Google, when people use their services, there is a lot of information associated with each person, and it's not enough to just keep track of their name and/or email address. This is where classes come in. Classes in Python allow us to create new data structures and you can think of them kind of like super variables in the sense that it's up to you what kind of information you can store for each class and what kind of capabilities each class will have.

According to the Python [documentation](https://docs.python.org/3/tutorial/classes.html), Python classes allow us to package data and functionality together and "Creating a new class creates a new *type* of object, allowing new *instances* of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state."

So we can see that a `class` is essentially a fundamental building block in Python. Consider the example below, in which we look at a potential implementation of a class for a customer at a bank:

```
class Customer():

def __init__(self, name, balance=0.0)
	self.name = name
	self.balance = balance

def withdraw(self, amount):
	if amount > self.balance:
		print("Insufficient funds.")
	self.balance -= amount
	return self.balance

def deposit(self, amount):
	self.balance += amount
	return self.balance
```

Here, we have defined the customer class, which is a blueprint for any future instances of customers we may want to create. Using the above blueprint, we can create one or more specific customers like so:

```
maria = Customer("Maria Zlatkova", 3000.0)
print(maria.balance) # Prints 3000
```

Here, we created a new specific instance of the customer class and we placed it in the variable called `maria` and from now on, we will refer to this specific instance of the customer as `maria`.  Maria can also withdraw or deposit money from her bank account:

```
maria.deposit(1500)
print(maria.balance) # Prints 4500
maria.withdraw(2000)
print(maria.balance) # Prints 2500
```

### File I/O

A file is a named location on disk that stores information. Files can be documents, images, tex files, and many more.

When we want to work with a file in our Python scripts, we have the option to read the content of the file or write content to the file. However, before we can read from or write to a file we need to open it first. When we are done, the file needs to be closed, so that the file can be otherwise used and the resources that are tied with the file are freed.

#### Open a file

Python has a built-in function `open()` to open a file. This function returns a file object, which we can use throughout our code
```
f = open("test.txt")    # open file in current directory
f = open("~/Desktop/python/test.txt")  # specifying full path
```

#### Read or write (perform operation)

When opening the file, we have the option to either read 'r', write 'w' or append 'a' to the file. The default mode in which a file is opened is the read mode. which allows us to extract strings from the file.

You can also open a file in write mode, which allows you to write to the file:

```
file = open(“test.txt”,”w”)

file.write(“Hello, world!”)
file.write(“This is a new text file”)
file.write(“and this is another line.”)
file.write(“Goodbye, world!”)

file.close()
```

When we want to read all the lines from a file we can use a for loop:
```
file = open(“test.txt”, “r”)
for line in file:
	print(line)
```
For the above `test.txt` file that we just created and wrote to, the above loop and print statements would output:
```
Hello, world!
This is a new text file
and this is another line.
Goodbye, world!
```

#### Close the file

After you've opened a file and after you've performed some operations on it or using its contents, you should remember to always close the file you're working with:

```
f = open("test.txt")
# perform file operations
f.close()
```

For more details on File I/O, you can read [here](https://docs.python.org/3/tutorial/inputoutput.html), [here](https://www.programiz.com/python-programming/file-operation), and [here](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python).

## Your Mission

We're going to create a program that can spellcheck bodies of text when given a dictionary against which to reference the correct spelling of worlds.

You're going to tackle a few `TODO`'s in `speller.py`.

### 0. `def __init__(self)`
In the init method we'll want to initializa the dictionary, and in order to do so, you should create the `words` instance variable and assign it to an empty set, where you will store the words contained in the dictionary.

Don't forget to remove the `return None` line after you've created the instance variable and assigned it to the empty set!

### 1. `def check(self, word)`
In this method, you'll want to check whether a given word is present in the dictionary. In order to do so, you are passed the `word` argument, which itself is a string coming from the text that is being spellchecked. You should return `True` if `word` is contained in the set of words in the dictionary, accessible through the `words` instance variable which you should've create in the `__init__` method.

Hint: Open up `dictionary.txt` and take a look at all the words contained in the dictionary. All of the words should be lowercase, which means that you'll want to manipulate the `word` variable passed into this method to make it all lowercase as well before you check whether it is contained in the set of words.

### 2. `def load(self, dictionary)`
In this method, you'll want to load the words from the dictionary file. You'll want to accomplish to following things:

1. Open the dictionary file
2. Go through all the lines of the file and for each line in the file, add the word in the set of words in the `words` instance variable

   Hint: a `for` loop might be useful here to go through all the lines of the file. For each line, you'll want to add it to the `words` instance variable in order to make sure that our set contains all the words in the file. However, if you simple add the line to the set, that will add the string itself and the newline at the end of the string (since in `dictionary.txt`, there is one word per line followed by a newline). How can you get rid of this newline ( `\n` ) character? Take a look at Python's `rtstrip()` method [here](https://www.tutorialspoint.com/python/string_rstrip.htm) and [here](http://python-reference.readthedocs.io/en/latest/docs/str/rstrip.html)

3. Close the file and return `True` when you are done working with the file



### 3. `def size(self)`
In this method, you'll want to return the total size of the dictionary.

Hint: Given that all the words in the dictionary should we stored in the `words` instance variable, how might you get the total number of words in that set?

## Testing your program

To run and test your program, you'll want to execute:

```
python speller.py <text>
```

Where `<text>` stands for the path to a text you might want to spellcheck. You have a few options to choose from:

```
texts/aca.txt
texts/birdman.txt
texts/constitution.txt
texts/frankenstein.txt
texts/her.txt
texts/lalaland.txt
texts/shakespeare.txt
```

So, a sample command might be:

```
python speller.py texts/her.txt
```

For `aca.txt`, the expected output should be:
```
Total number of words in text: 362942
Number of misspelled words: 16143
```

For `birdman.txt`, the expected output should be:
```
Total number of words in text: 21714
Number of misspelled words: 1568
```

For `constitution.txt`, the expected output should be:
```
Total number of words in text: 7543
Number of misspelled words: 50
```

For `frankenstein.txt`, the expected output should be:
```
Total number of words in text: 79602
Number of misspelled words: 2430
```

For `her.txt`, the expected output should be:

```
Total number of words in text: 18356
Number of misspelled words: 1218
```

For `lalaland.txt`, the expected output should be:
```
Total number of words in text: 17526
Number of misspelled words: 1303
```

For `shakespeare.txt`, the expected output should be:
```
Total number of words in text: 899787
Number of misspelled words: 45934
```
