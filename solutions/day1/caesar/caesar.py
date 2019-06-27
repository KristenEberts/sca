import cs50, sys

if not len(sys.argv) == 2:
    print("Usage: {} <key>".format(sys.argv[0]))
    exit(1)

plaintext = input("plaintext: ")
print("ciphertext: ", end="")

for char in plaintext:
    if char.isupper():
        print(chr((ord(char) - ord('A') + int(sys.argv[1])) % 26 + ord('A')), end="")
    elif char.islower():
        print(chr((ord(char) - ord('a') + int(sys.argv[1])) % 26 + ord('a')), end="")
    else:
        print(char)
print()
