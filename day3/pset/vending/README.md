# Vending Machine

### TL;DR

Create a vending machine class!

### Background

#### So Thirsty

![Thirsty Spongebob](thirsty.jpg)

Scene: It's a hot summer day on the streets of Japan and you find yourself feeling a bit thirsty. No worries! There's bound to be a vending machine nearby on the street somewhere. That's just how Japan rolls.

So, you pop over to a machine, pick a cool, refreshing Peach Coke and pay the requisite Yen (currency in Japan). Donk! Out pops your soda!

#### Thinking about Classes and Objects

Now, what IS a vending machine? What can a vending machine do? In programming, when we create a class, we think about all the attributes and functions that class should have. So we need to think about the vending machine class.

### Your Mission

Create a **Vending_Machine** class that, when instantiated (created as an individual object), will be given a dictionary of drinks. This dictionary of drinks will have the drink name as a key and the price as a value. For example:

```
drinks = {"Coke": 1.99, "Arizona Tea": 0.99, "Dasani": 1.50}
```

You will also want to create a function (method) in the class that will ask the user for a drink and dispense it (as by printing the name of the drink to the screen)! Of course, you only want to dispense drinks in the dictionary (thus `in` might be helpful here).

#### Testing

To test this, outside of the class definition, create an instance of the object with a given dict of drinks like below:

```
drinks = {"Coke": 1.99, "Arizona Tea": 0.99, "Dasani": 1.50}

cokeMachine = Vending_Machine(drinks)
```

Then, you'll want to test your method!
