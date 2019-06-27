# Pokemon

### TL;DR

Create a Pokemon class!

### Background
Classes are like templates or blueprints for objects. Pokemon also have a 'template': each creature has attributes like **name**, **XP** and **HP**, which we've already added.

#### Thinking about Classes and Objects

So far, we've added attributes to describe what a Pokemon *is*. But what can a Pokemon *do*? In programming, when we create a class, we think about both the attributes and the functions that class should have. So we need to add methods (class-specific functions) to the Pokemon class. 

### Your Mission

In a file called `pokemon.py`, extend the **Pokemon** class so that, when instantiated, a new object of that class will be given a list of four moves. (Hint: extend the `__init__` function to assign those moves to a `moves` attribute.) For example:

```
moves = ['Growl', 'Thunder Shock', 'Tail Whip', 'Quick Attack']
```
Pokemon can learn moves, and forget moves, but they can only have four moves at one time. So you need to add functions (methods) that let you train your Pokemon!

#### Forgetting Moves
To train your Pokemon in something else, you need to first make them forget a move. Create a **forget** method that removes a specific move from the list. But what if a trainer tries to make a Pokemon forget a move that it doesn't know? (Using `in` might be helpful here).

#### Testing

To test this, enter the Python interpreter by typing `python` in your console. Import your Pokemon class (`from pokemon import Pokemon`) Then, create an instance of the class (i.e., a specific Pokemon object) with a given list of moves like below:

```
>>> moves = ['Growl', 'Thunder Shock', 'Tail Whip', 'Quick Attack']
>>> Pikachu = Pokemon(moves)
```

Then, you'll want to test your method! Using the example above, you could write `Pikachu.forget('Growl')`, then see if Pikachu forgets his **Growl** move!

#### Learning Moves
Next, create a **learn** method that adds a new move to the Pokemon's skill list, but only if there are fewer than four items in the list. If the list is full, print a message to the trainer. Be sure to test your method!

### Bonus Challenge
Pokemon do more than learn and forget moves, right? They also battle other Pokemon! Add a method called `fight` that asks for a move as input, then prints out its effectiveness, like so:

```
>>> Pikachu.fight()
>>> What move? Pikachu knows Growl and Tail Whip.
>>> Growl
>>> Pikachu used Growl! It's not very effective.
```
Tip: You can create a list or set of possible outcomes, then use `random.choice()` to choose one of the outcomes at random.