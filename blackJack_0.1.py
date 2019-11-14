# -*- coding: utf-8 -*-
import copy
import os
import random
import time


cards = {'Clubs':{'Ace':11,'Jack': 2, 'Queen': 3, 'King':4, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10},
        'Diamonds':{'Ace':11,'Jack': 2, 'Queen': 3, 'King':4, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10},
        'Hearts':{'Ace':11,'Jack': 2, 'Queen': 3, 'King':4, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10},
        'Spades':{'Ace':11,'Jack': 2, 'Queen': 3, 'King':4, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10}}

ru_cards = {'Крестей':{'Туз':11,'Валет': 2, 'Дама': 3, 'Король':4, 'Шестерка':6, 'Семерка':7, 'Восьмерка':8, 'Девятка':9, 'Десятка':10},
        'Бубей':{'Туз':11,'Валет': 2, 'Дама': 3, 'Король':4, 'Шестерка':6, 'Семерка':7, 'Восьмерка':8, 'Девятка':9, 'Десятка':10},
        'Червей':{'Туз':11,'Валет': 2, 'Дама': 3, 'Король':4, 'Шестерка':6, 'Семерка':7, 'Восьмерка':8, 'Девятка':9, 'Десятка':10},
        'Пик':{'Туз':11,'Валет': 2, 'Дама': 3, 'Король':4, 'Шестерка':6, 'Семерка':7, 'Восьмерка':8, 'Девятка':9, 'Десятка':10}}        

deck = copy.deepcopy(cards)

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

def playerTurn():
    print('Card for you')
    time.sleep(1)
    count = 0
    count += getRandomCard()
    print('+' + str(count), 'points')
    return count
    
def compTurn():
    print('Card for AI')
    time.sleep(1)
    comp_count = 0
    while comp_count < 20:
        comp_count += getRandomCard()
        print('+' + str(comp_count), 'points')
        return comp_count

def start():
    welcomeScreen()
    user_win = 0
    comp_win = 0
    end = 'yes'       
    while end == 'yes':
        os.system('cls')
        print('Score: ' + str(user_win) + ':' + str(comp_win))        
        print('\nWell, play Black Jack\n\n')
        count = 0
        comp_count = 0
        count += playerTurn()
        print()
        choice = ''
        while choice != 'no':
            choice = input('One more?(yes/no) ')
            print()
            if choice == 'yes':            
               count +=  playerTurn()
               if count == 21:
                print(count, 'points\n')
                print('Player won!')
                user_win += 1
                break                
               elif count > 21:
                print(count, 'points\n')
                print('Player lost.(')
                comp_win += 1
                break
               else:
                print(count, 'points\n')
        if choice == 'no':
            while comp_count < count:
                if comp_count >= 17:
                    print('Dangerous. AI have to think...')
                    time.sleep(3)
                    if random.randint(0,1) == 1:
                        comp_count += compTurn()
                        print(comp_count, 'points\n')
                    else:
                        print('It is enough for AI')
                        break
                else: 
                    comp_count += compTurn()
                    print(comp_count, 'points\n')
                    time.sleep(1)

            if count <= comp_count and comp_count < 22:
                print('Player lost.(')
                comp_win += 1
                
            elif count < 22 and count > comp_count:
                print('Player won!')
                user_win += 1
            elif comp_count > 21 and count < 22:
                print('Player won!')
                user_win += 1
        end = input('One more game?(yes/no) ')
    os.system('cls')
    print('\nFinal score: ' + str(user_win) + ':' + str(comp_win))
    input('Press ENTER to exit') 

if __name__ == '__main__':
    start()
