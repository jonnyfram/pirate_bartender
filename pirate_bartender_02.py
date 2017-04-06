import random

first_drink = True #Bool to check if first drink or not

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

adjectives = [
"Battleship",
"Accident",
"Accordion",
"Accountant",
"Achiever",
"Acid",
"Chain",
"Chairlift",
"Goodie",
"Goose",
"Gopher",
"Kangaroo",
"Karate",
"Karen",
"Kayak",
"Kazoo",
"Weedkiller",
"Weekend",
"Weekender"
]

nouns = [
    'People',
    'History',
    'Way',
    'Art',
    'World',
    'Map',
    'Family',
    'Government',
    'Health',
    'System',
    'Computer',
    'Meat',
    'Year',
    'Music',
    'Person',
    'Reading',
    'Method',
    'Data',
    'Understanding',
    'Theory',
    'Law',
    'Bird',
    'Literature',
    'Problem',
    'Software',
    'Control',
    'Knowledge',
    'Power',
    'Ability',
    'Economics',
    'Love'
]

def RandomDrinkName():
   adjective = random.choice(adjectives)
   noun = random.choice(nouns)
   drink_name = (str(adjective)+" "+str(noun))
   return drink_name
    
def OrderDrink():
    
    answers = {}
    for key, question in questions.items():
        
        answer = input(question)
       
        
        if (answer == "y") or (answer == "Y"):
            answers[key] = True
            #print("True answer in OrderDrink function:")
            #print(answers)
        else: 
            answers[key] = False
            #print("False answer in OrderDrink function:")
            #print(answers)
        
    return answers
    
def WantDrink():
    
    first_drink_text = "Do ye want a drink?"
    not_first_drink_text = "Another drink?"
    
    if first_drink:
        drink_text = first_drink_text
    else:
        drink_text = not_first_drink_text
    
    answer = input(drink_text)
    if (answer == "y") or (answer == "Y"):
            want_drink = True
    else: 
        want_drink = False
    return want_drink
    
def MixDrink(answers):
    drink = []
    
    for key, answer in answers.items():## items returns a list of the dicts (key, value) tuple pairs
        
        if (answer == True):
            drink.append(random.choice(ingredients[key]))

    return drink
            
if __name__ == '__main__':
    
    want_drink = WantDrink()
    
    while want_drink:
        first_drink = False
        answers=OrderDrink()
    
        drink = MixDrink(answers) 
        
        drink_name = RandomDrinkName()
        
        #Variables cannot be accessed outside the scope of a function they were defined in.
        #so we create a variable with the same name outside of the MixDrink() and print that
        print("Arrr. One "+drink_name+" coming right up; "+", ".join(drink)+"... Here ye arrrr... Drink up ya scurvy bum!")
        want_drink = WantDrink()