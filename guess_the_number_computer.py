#now we will make a program in which a user will decide a number and computer will guess the number 

import random
def computer_guess(x):
    print(f"think a number between 1 and{x}.")
    low=1
    high=x
    attempts=0
    while True:
        guess=random.randint(1,x)
        attempts+=1
        print(f"my guess is: {guess}")
        response=input("enter'h' if too high,'l' if too low,'c' if correct:").lower()
        if response=='c':
            print(f'yay! i guessed your number in {attempts} attempts')
        elif response=='h':
            high=guess-1
        elif response=='l':
            low=guess+1
        else:
            print("invalid input! please enter h,l or c ")

computer_guess(1000)