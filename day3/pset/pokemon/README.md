# Pokemon

### TL;DR

Create a Pokemon class!

### Background
Classes are like templates or blueprints for objects. Pokemon also have a 'template': each creature has attributes like skills, levels, and a name.

#### Thinking about Classes and Objects

Now, what IS a Pokemon? What can a Pokemon do? In programming, when we create a class, we think about all the attributes and functions that class should have. So we need to think about the Pokemon class.

### Your Mission

In a file called `pokemon.py`, create a **Pokemon** class that, when instantiated (created as an individual object), will be given a list of four moves. (Hint: define an `__init__` function to assign those moves to a `moves` attribute.) For example:

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

Then, you'll want to test your method! Using the example above, you could write Pikachu.forget('Growl'), then see if Pikachu forgets his **Growl** move!

#### Learning Moves
Next, create a **learn** method that adds a new move to the Pokemon's skill list, but only if there are fewer than four items in the list. If the list is full, print a message to the trainer. Be sure to test your method!

### Bonus Challenges
Pokemon do more than learn and forget moves, right? They also have attributes like their **name**, their **type**, and their **level**. Add those attributes to your `Pokemon` class. Then, add a method called `fight` that prints a skill and its effectiveness, like so:

```
>>> Pikachu.fight()
>>> Pikachu used Growl! It's not very effective.
```
Tip: You can create a set of possible outcomes, then pop something off the set to determine how effective the move is.