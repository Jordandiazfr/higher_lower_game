from art import logo, vs
from replit import clear
from game_data import data
import random
game_over = False
SEP = "=================================================================="

def selector(data):
    player = random.choice(data)
    data.remove(player)
    return player


def compare(p1, p2, choice):
    if choice == p1:
        player = p1
        computer = p2
    else:
        player = p2
        computer = p1
    if player['follower_count'] > computer['follower_count']:
        return player # winning
    else:
        return 0  # loosing


# get the two comparaisons
A_ = selector(data)
B_ = selector(data)
score = 0


while not game_over:
    print(logo)
    print(
        f"Compare A: {A_['name']}, a {A_['description']}, from {A_['country']}") #pstt... {A_['follower_count']}
    print(vs)
    # Second contendant
    print(
        f"Compare B: {B_['name']}, a {B_['description']}, from {B_['country']}") # pstt... {B_['follower_count']}
    choice = input("Who has more followers type 'A' or 'B' ").upper()
    # Compare function
    if choice == "A":
        choice = A_
    else:
        choice = B_

    winner = compare(A_, B_, choice)
    clear()
    if winner == 0:
        print(SEP)
        print("You losee, final score: %d" %(score))
        print(SEP)
        game_over = True
    else:
        score = score + 1
        print(SEP)
        print("You got it right, score: %d" % (score))
        print(SEP)
    #The winner is the new A option, And we got a random new B option 
    A_ = winner
    B_ = selector(data)
