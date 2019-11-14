# -*- coding: utf-8 -*-
import copy
import os
import random
import time

# if you do it this way then you can easily add new languages without having to type out the whole dictionary. You just need
# to create two lists, one for the card numbers and one for the suit names, and the program will do the rest for you :)
numerical_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
numerical_names = ["Two", "Three", "Four", "Five","Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
all_cards = dict(zip(numerical_names, numerical_values))
suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
with_suits = {}
for x in suits:
    with_suits.update({x:all_cards})        

deck = copy.deepcopy(with_suits)

def ace_test(var):
    if var == 11:
        start.aces += 1

def user_victory(count):
    print(count, 'points\n')
    print('Player won!')
    start.user_win += 1
    reset()

def comp_victory(comp_count):
    print(comp_count, 'points\n')
    print('Computer won!')
    start.comp_win += 1
    reset()
    choice = "yes"

def reset():
    start.comp_count = 0
    start.count = 0
    start.aces=0
    print('\nScore: ' + str(start.user_win) + ':' + str(start.comp_win))
    start.choice = input('would you like to play again?(done or yes) ')



def getRandomCard():
    suit = random.sample(list(deck),1)[0]
    card = random.sample(list(deck[suit]),1)[0]
    print(card + ' of ' + suit)
    return int(deck[suit].pop(card))

def welcomeScreen():
    os.system('cls')
    print('\n\n\n\n\n\t\t\tBlack Jack\n\t\t\tGame')
    time.sleep(2)
    os.system('cls')
    print('\n\n\n\n\n\t\t\t...Loading...')
    time.sleep(2)
    os.system('cls')

def playerTurn(count):
    print('Card for you')
    time.sleep(1)
    start.aces
    var = getRandomCard()
    ace_test(var)
    if start.count + var > 20 and start.aces !=0:
        start.count -= 10
        start.aces -= 1
    return var

def compTurn(comp_count):
    print('Card for AI')
    time.sleep(1)
    global aces
    var = getRandomCard()
    ace_test(var)
    if start.comp_count + var > 20 and start.aces != 0:
        var -= 10
        start.aces -= 1
    return var



def start():
    start.user_win = 0
    start.comp_win = 0
    start.count = 0
    start.comp_count = 0
    start.aces = 0
    start.choice = "yes"
    print('\nWell, play Black Jack\n\n')
    while start.choice == 'yes':
        os.system('cls')
        while start.count <= 21:
            if start.count == 21:
                user_victory(start.count)
            start.count = start.count + playerTurn(start.count)
            print('Total:' + str(start.count), 'points')
            if start.count < 21:
                start.choice = input('One more?(yes/no) ')
                break
            if start.count > 21:
                print('You busted!')
                comp_victory(start.count)
            else:
                start.choice = "no"
    if start.choice == "no":
        while start.comp_count < start.count and start.comp_count < 21:
            start.comp_count = start.comp_count + compTurn(start.comp_count)
            print('+' + str(start.comp_count), 'points')
            if start.comp_count >= 17:
                print('Dangerous. AI have to think...')
                time.sleep(3)
                if random.randint(0,1) == 1:
                    start.comp_count = start.comp_count + compTurn(start.comp_count)
                    print(start.comp_count, 'points\n')
                else:
                    print('It is enough for AI')
            else:
                start.comp_count = start.comp_count + compTurn(start.comp_count)
                print(start.comp_count, 'points\n')
                time.sleep(1)
        if start.count == 21:
            comp_victory(start.comp_count)
        else:
            print('Computer busted!')
            user_victory(start.comp_count)
    else:
        print ("Thank you for playing")

    choice = input ("done to to exit or yes to play another game")
    if input == "done":
        print('\nFinal score: ' + str(user_win) + ':' + str(comp_win))

if __name__ == '__main__':
    start()
