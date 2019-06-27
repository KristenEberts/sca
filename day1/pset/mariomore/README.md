# Mario (More Comfortable)

## TL;DR

Create a program that prints the following shape with a user-inputted height:

```
~/workspace/ $ mario.py
height: 5
    #  #
   ##  ##
  ###  ###
 ####  ####
#####  #####
```

## Background

### Mario 1-1

In the 1985 game **Super Mario Bros.**, Mario encounters two half-pyramids he must jump over! I decided to reminisce and play a little of the game myself and I took a screenshot!

![mariomore](mariomore.png)

We're going to create a program that prints out this same shape. However, we're going to make the program ask for user input for the height of the half-pyramids. Then, we're gonna print out the shape!

## Specification

- Write a program that recreates these half-pyramids using hashes (`#`) for blocks.
- To make things more interesting, first prompt the user for the half-pyramid's height, a non-negative integer no greater than `23`. (The height of the half-pyramids pictured above happens to be `4`, the width of each half-pyramid `4`, with an a gap of size `2` separating them.)
- If the user fails to provide a non-negative integer no greater than `23`, you should re-prompt for the same again.
- Then, generate (with the help of `printf` and one or more loops) the desired half-pyramid.
- Take care to left-align the bottom-left corner of the left-hand half-pyramid with the left-hand edge of your terminal window.

## Help from CS50's own Zamyla Chan

{% video https://www.youtube.com/embed/gqS876f0lk0 %}

## Check Your Work

To check your work run `check50 cs50/2017/ap/sentimental/mario/more`
