def decreasing(l):
    # TODO: Return True if `l` is decreasing, otherwise False
    return False

# TODO: Add more tests below

print("Testing that decreasing lists are detected")

# These should all print "True"
print(decreasing([]))
print(decreasing([15]))
print(decreasing([2, 1]))
print(decreasing([1, 0, -1]))
print(decreasing([50, 40, 38, 36, 29, 25, 20, 20, 20, 12]))

print("Testing that non-decreasing lists are detected")

# These should all print "False"
print(decreasing([1, 2]))
print(decreasing([5, 4, 3, 2, 3]))
