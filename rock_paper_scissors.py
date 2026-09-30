#rock paper scissor game with computer 
import random

def play():
    user=input("'r' for rock,'s' for scissors,'p' for paper:")
    computer=random.choice(['r','s','p'])
    # r>s , s>p , p>r
    if user==computer:
        return "tie"
    if is_win(user,computer):
        return "you won!"
    return "you lost!"

def is_win(player,opponent):
#return true if player wins 
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True 
    
print(play())