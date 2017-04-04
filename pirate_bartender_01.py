questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

answers = {"strong": False,
            "salty": False,
            "bitter": False,
            "sweet": False,
            "fruity": False,
}


ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

#print(answers)

def OrderDrink(answers):
    
    for key, question in questions.items():
        
        answer = input(question)
        answer = str(answer)
        
        if (answer == "y") or (answer == "Y"):
            answers[key] = True
            print("True answer in OrderDrink function")
            print(answers)
        else: 
            answers[key] = False
            print("False answer in OrderDrink function")
            print(answers)
        
        return answers

OrderDrink(answers)
print("Answers returned")
print(answers)
