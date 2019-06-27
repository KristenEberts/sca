# Vigenére

## tl;dr

Implement a program that runs like the following examples:

```
~/workspace/ $ python vigenere.py
key: ABC
plaintext: HELLO
ciphertext: HFNLP
```

```
~/workspace/ $ python vigenere.py
key: ABC
plaintext: Hello, world!
ciphertext: Hfnlp, yosnd!
```

## The Vigenére Cypher

So the Caesar cipher isn't all that secure. There are only going to be 26 different possible keys a hacker needs to try ('a' doesn't even change the message!). We have to be able to do better. One slightly more secure cipher is the Vigenére cipher!

Vigenère's cipher improves upon Caesar's cipher by encrypting messages using a sequence of keys (or, put another way, a keyword). In other words, if _p_ is some plaintext and _k_ is a keyword (i.e., an alphbetical string, whereby A represents 0, B represents 1, C represents 2, ..., and Z represents 25), then each letter, _c<sub>i</sub>_, in the ciphertext, _c_, is computed as:

**c<sub>i</sub> = (p<sub>i</sub> + k<sub>j</sub>) % 26**

Note this cipher's use of _k<sub>j</sub>_ as opposed to just _k_. And if _k_ is shorter than _p_, then the letters in _k_ must be reused cyclically as many times as it takes to encrypt _p_.

In other words, if Vigenère himself wanted to say HELLO to someone confidentially, using a keyword of, say, ABC, he would encrypt the H with a key of 0 (i.e., A), the E with a key of 1 (i.e., B), and the first L with a key of 2 (i.e., C), at which point he'd be out of letters in the keyword, and so he'd reuse (part of) it to encrypt the second L with a key of 0 (i.e., A) again, and the O with a key of 1 (i.e., B) again. And so he'd write HELLO as HFNLP.

**Encrypting HELLO with a keyword of ABC (reused cyclically as ABCAB) yields HFNLP.**

| *plaintext*    | H | E | L | L | O |
|--|--|--|--|--|--|
| *key*        | A | B | C | A | B |
| *key value* | 0 | 1 | 2 | 0 | 1 |
| *ciphertext* | H | F | N | L | P |

## Specification

Design and implement a program that encrypts messages using Vigenère's cipher.

- Implement your program in a file called `vigenere.py` in a directory called `vigenere`.
- Your program must accept a single command-line argument: a keyword, _k_, composed entirely of alphabetical characters.
- If your program is executed without any command-line arguments, with more than one command-line argument, or with one command-line argument that contains any non-alphabetical character, your program should print an error (of your choice) and exit immediately, with `main` returning `1` (thereby signifying an error).
- Otherwise, your program must proceed to prompt the user for a string of plaintext, _p_, (as by a prompt for `plaintext:`) which it must then encrypt according to Vigenère's cipher with _k_, ultimately printing the result (prepended with `ciphertext:` and ending with a newline) and exiting, with `main` returning `0`.
- With respect to the characters in _k_, you must treat `A` and `a` as 0, `B` and `b` as 1, ... , and `Z` and `z` as 25.
- Your program must only apply Vigenère's cipher to a character in _p_ if that character is a letter. All other characters (numbers, symbols, spaces, punctuation marks, etc.) must be outputted unchanged. Moreover, if your code is about to apply the _j<sup>th</sup>_ character of _k_ to the _i<sup>th</sup>_ character of _p_, but the latter proves to be a non-alphabetical character, you must wait to apply that _j<sup>th</sup>_ character of _k_ to the next alphabetical character in _p_; you must not yet advance to the next character in _k_.
- Your program must preserve the case of each letter in _p_.

## CS50's Own Zamyla for Help

Ignore the first minute or so, but this should help get you started.

{% video https://www.youtube.com/embed/n4gcWaHKhoU?start=52 %}

## Testing

To test, run `check50 cs50/2017/fall/vigenere` in the terminal.
