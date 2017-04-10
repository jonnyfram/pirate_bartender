import random
adjectives = ["battleship",
"accident",
"accordion",
"accountant",
"achiever",
"acid",
"chain",
"chairlift",
"chairman",
"goodie",
"goose",
"gopher",
"kangaroo",
"karate",
"karen",
"kayak",
"kazoo",
"weedkiller",
"week",
"weekend",
"weekender"]

nouns = [
    'people',
    'history',
    'way',
    'art',
    'world',
    'map',
    'family',
    'government',
    'health',
    'system',
    'computer',
    'meat',
    'year',
    'thanks',
    'music',
    'person',
    'reading',
    'method',
    'data',
    'food',
    'understanding',
    'theory',
    'law',
    'bird',
    'literature',
    'problem',
    'software',
    'control',
    'knowledge',
    'power',
    'ability',
    'economics',
    'love']

def RandomDrinkName():
   adjective = random.choice(adjectives)
   noun = random.choice(nouns)
   print(str(adjective)+" "+str(noun))
   
print(RandomDrinkName())
    