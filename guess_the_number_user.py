# guess the number (computer will choose the number)
"""import random library and use randint function by this computer will randomlly arrange the number
between the limits """

import random 
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!= random_number:
        guess=int(input(f"guess the number between 1 and {x}:"))
        if guess<random_number:
            print("guess again. too low;")
        elif guess>random_number:
            print("guess again. too high;")

    print(f"yay,congrats you guessed the number{random_number} correctly")


guess(100)