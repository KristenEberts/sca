name = input("Enter a name: ")
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
adverb = input("Enter an adverb: ")
food1 = input("Enter a food: ")
food2 = input("Enter another food: ")
noun = input("Enter a noun: ")
place = input("Enter a place: ")
verb = input("Enter a verb: ")

print('''
%s was planning a dream vacation to %s.
%s was especially looking forward to trying the local
cuisine, including %s %s and %s %s.

%s will have to practice the language %s to
make it easier to %s with people.

%s has a long list of sights to see, including the
%s museum and the %s river.''' % (name, place, name, adj1, food1, adj2, food2, name, adverb, verb, name, noun, adj1))
