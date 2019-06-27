# Pokemon

### TL;DR

Create a Pokemon class!

### Background
Classes are like templates or blueprints for objects. Pokemon also have a 'template': each creature has attributes like skills, levels, and a name.

#### Thinking about Classes and Objects

Now, what IS a Pokemon? What can a Pokemon do? In programming, when we create a class, we think about all the attributes and functions that class should have. So we need to think about the Pokemon class.

### Your Mission

Create a **Pokemon** class that, when instantiated (created as an individual object), will be given a list of four moves. For example:

```
moves = ['Growl', 'Thunder Shock', 'Tail Whip', 'Quick Attack']
```
Pokemon can learn moves, and forget moves, but they can only have four moves at one time. So you need to add functions (methods) that let you train your Pokemon!

#### Forgetting Moves
To train your Pokemon in something else, you need to first make them forget a move. Create a **forget** method that removes a specific move from the list. But what if a trainer tries to make a Pokemon forget a move that it doesn't know? (Using `in` might be helpful here).

#### Learning Moves
Create a **learn** method that adds a new move to the Pokemon's skill list, but only if there are fewer than four items in the list. If the list is full, print a message to the trainer.

#### Testing

To test this, outside of the class definition, create an instance of the object (i.e., a specific Pokemon) with a given dict of moves like below:

```
moves = ['Growl', 'Thunder Shock', 'Tail Whip', 'Quick Attack']

Pikachu = Pokemon(drinks)
```

Then, you'll want to test your method!
