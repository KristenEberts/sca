import cs50, sys

if len(sys.argv) != 2 or len(sys.argv[1]) == 0:
    print("Usage: python vigenere.py keyword")
    exit(1)

keyword = sys.argv[1]
if not keyword.isalpha():
    print("invalid keyword")
    exit(1)

print("plaintext:  ", end="")
plaintext = cs50.get_string()

index = 0
print("ciphertext: ", end="")
for c in plaintext:
    if c.isalpha():
        key = ord(keyword[index].upper()) - ord('A')
        if c.isupper():
            print(chr((ord(c) - ord('A') + key) % 26 + ord('A')), end="")
        else:
            print(chr((ord(c) - ord('a') + key) % 26 + ord('a')), end="")
        index = (index + 1) % len(keyword)
    else:
        print(c, end="")
print()
