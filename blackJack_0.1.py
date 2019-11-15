#- * - coding: utf - 8 - * -
import copy
import os
import random
import time

numerical_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
numerical_names = ["Two", "Three", "Four", "Five","Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
all_cards = dict(zip(numerical_names, numerical_values))
suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
deck = {}
for x in suits:
    deck.update({x:all_cards})




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

def reset():
    start.comp_count = 0
    start.count = 0
    start.aces=0
    print('\nScore: ' + str(start.user_win) + ':' + str(start.comp_win))


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
    print("Let's Play!")

def playerTurn(count):
    print('Card for you')
    time.sleep(1)
    var = getRandomCard()
    ace_test(var)
    return var

def compTurn(comp_count):
    print('Card for AI')
    time.sleep(1)
    var = getRandomCard()
    ace_test(var)
    return var

def player_seq():
    start.count = start.count + playerTurn(start.count)
    if start.count == 21:
        print('Total:' + str(start.count), 'points')
        user_victory(start.count)
        start.choice = input('would you like to play again?(done or y) ')
    if start.count < 21 and start.count != 0:
        print('Total:' + str(start.count), 'points')
        start.choice = input('One more?(y/n) ')
    if start.count > 21:
        if start.aces == 0:
            print('Total:' + str(start.count), 'points')
            print('You busted!')
            comp_victory(start.count)
            start.choice = input('would you like to play again?(done or y) ')
        else:
            start.aces -= 1
            start.count -= 10
            print('Total:' + str(start.count), 'points')
            start.choice = input('One more?(y/n) ')
    initialize()

def comp_seq():
    start.comp_count = start.comp_count + compTurn(start.comp_count)
    if start.comp_count < 22:
        if start.comp_count > start.count:
            print('Total:' + str(start.comp_count), 'points')
            comp_victory(start.comp_count)
            start.choice = input('would you like to play again?(done or y) ')
    if start.comp_count >= 22:
        if start.aces == 0:
            print('Total:' + str(start.comp_count), 'points')
            print('Computer busted!')
            user_victory(start.comp_count)
            start.choice = input('would you like to play again?(done or y) ')
        else:
            start.comp_count -= 10
            start.aces -= 1
            print('Total:' + str(start.comp_count), 'points')
    initialize()

def initialize():
    if  start.choice == 'y':
        player_seq()
    if start.choice == "n":
        comp_seq()
    else:
        print ("Thank you for playing")
        print('\nFinal score: ' + str(start.user_win) + ':' + str(start.comp_win))
        __name__ == False

def start():
    start.user_win = 0
    start.comp_win = 0
    start.count = 0
    start.comp_count = 0
    start.aces = 0
    start.choice = "y"
    initialize()

if __name__ == '__main__':
    start()
