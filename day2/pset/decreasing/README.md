# Decreasing

### TL;DR

Determine if a list of numbers is in decreasing order.

### Background

This problem deals with lists of numbers. Remember, a list can have no
elements:

```
[]
```

One element:

```
["cat"]
```

Five elements:

```
[1, 2, 3, 4, 5]
```

or any other number of elements. Say I create a variable that refers
to a list, like this:

```
my_list = ["a", "b", "c"]
```

This line of code says I have a variable `my_list` and its value is
set to the list `["a", "b", "c"]`.

One thing we can do with a list is get elements out of it using their
**index**. The first element in a list is at index 0, the next is at
index 1, and so on.

> **Check for understanding**
>
> If a list has 5 elements, what is the index of the last element?
> What if the list has 10 elements? 100 elements? Some number *n*
> elements?
>
> {% spoiler "Answer" %}
> If a list has 5 elements, the index of the last element is 4. The
> five indices are 0, 1, 2, 3, 4. For 10 elements the last index is 9
> and for 100 elements the last index is 99. In general, for *n*
> elements, the last index is *n*-1.
> {% endspoiler %}

Another thing we can do with a list is *append* to it, or add
something to its end. If we have a list like this:

```
numbers = [1, 2, 3]
```

And then we do this:

```
numbers.append(4)
```

Then numbers now has the value `[1, 2, 3, 4]`. I've appended `4` to the list.

If I run the following code:

```
pets = []
pets.append("cat")
pets.append("dog")
pets.append("fish")
```

Then at the end `pets` has the value `["cat", "dog", "fish"]`.

### Your Mission

Write a function that takes a list of numbers as an argument and
returns `True` if the list is in decreasing order and `False`
otherwise.

*Hint:* a list is in decreasing order if it is empty or if each of its
elements besides the last is greater than or equal to the next
element.

> **Check for understanding**
>
> Is a list with a single element in decreasing order?
> 
> {% spoiler "Answer" %}
> Yes, because it has no element besides its last element, so nothing
> is required to be greater or equal to anything else for it to be
> decreasing.
> {% endspoiler %}


##### Suggested steps:

1. Detect if lists of 0 or 1 element are decreasing

2. Add code to detect if lists of 2 elements are decreasing

3. Add code to detect if lists of 3 or 4 elements are decreasing

4. Use a loop instead to detect if lists of at least 1 element are
   decreasing.

##### Bonus Challenge

Change your function to detect if a list first decreases and then
increases (but does not decrease again). Don't forget to write tests!
