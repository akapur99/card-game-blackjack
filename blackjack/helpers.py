#!/usr/bin/env python3

"""
    Helper Functions for Black Jack Game

    ...

    Functions
    -------
       
    check_hand()
        Checks person's hand for Black Jack or bust if neither,
        returns value of hand
    
    check_move()
        Validate user move, returns boolean

    check_wager()
        Validate user wager input, returns boolean

    evaluate_hands()
        Evaluates player and dealer's hands to check for Black Jack or Bust
    
    final_eval()
        Evaluates and returns who has higher hand value between 2 hands

    get_answer()
        Takes and validates Yes/No Answers and returns True if yes, False if No

    get_wager()
        Takes in wager from user input, validates and returns int
    
    hit()
        'Hit' person - deal them a card, if player - print out value

    print_high_scores()
        Reads and prints high_scores from local .txt, if any
    
    save_high_score()
        Check if current winnings are a high score and save them if they are

    think()
        Sleep for <1 second 

"""

from deck import Deck
from time import sleep
from person import Person


def final_eval(player, dealer):
    p_value = max(player.get_value())
    d_value = max(dealer.get_value())

    if p_value > d_value:
        return 0
    elif p_value < d_value:
        return 1
    else:
        return 2


def evaluate_hands(dhand, phand):
    if dhand == 'BJ' and phand == 'BJ':
        return 0
    elif dhand == 'BJ':
        return 1
    elif phand == "BJ":
        return 2
    elif dhand == "bust" and phand == "bust":
        return 3
    elif dhand == "bust":
        return 4
    elif phand == "bust":
        return 5
    else:
        return 6


def check_hand(person):
    value = person.get_value()

    if len(value) < 2:  # If no Ace
        if value[0] == 21:
            return 'BJ'
        elif value[0] > 21:
            return 'bust'
        else:
            return str(value[0])
    else:  # If Ace
        if value[0] == 21 or value[1] == 21:
            return 'BJ'
        elif value[0] > 21:  # Checks if smaller value of Ace returns bust
            return 'bust'
        elif value[1] > 21:
            # If larger Ace value returns bust
            # simplify the deck - only retain smaller value
            person.cards.remove('A')
            person.cards.append(1)
            return str(value[0])
        else:
            # Return value of deck without Ace
            # and inform player they have an ace
            return str(value[0]-1) + ' and an Ace!'


def print_high_scores():
    high_scores = []
    with open('high_score.txt', "r") as hs:
        high_scores = hs.readlines()
    
    if len(high_scores) > 0:
        print('HIGH SCORES ARE:')
        for i in high_scores:
            print(i)
    else:
        print("NO HIGH SCORES SET YET!")


# Implement binary search
def bin_search(x, lst):
    left = 0
    right = len(lst)-1

    while left <= right: 
        mid = left + (right - left)/2; 
        # Check if x present at mid 
        if lst[mid] == x: 
            return mid 
        # If x is greater than mid ignore left half 
        elif lst[mid] < x: 
            left = mid + 1
        # If x is smaller than mid ignore right half 
        else: 
            right = mid - 1
      
    # If element not present 
    return -1


def save_high_score(high_score, player):
    high_scores = []

    # Read in past high scores if any
    try:
        with open('high_score.txt', "r") as hs:
            high_scores = hs.readlines()
    except:
        pass
    i = len(high_scores)

    # Find index to insert current high score
    for k in range(i):
        prev_score = (int)(high_scores[k].split(' - ')[2])
        if high_score > prev_score:
            i = k
            break

    # Create string to be inserted
    new_h = str(i+1) + " - " + player.get_name() + " - " + str(high_score)

    # if index is at end of high score list
    if i == len(high_scores):
        if i > 6:  # Only Allow top 6 high scores to be saved
            print(' SORRY SCORE ISN\'T HIGH ENOUGH FOR BOARD')
            return
        else:             
            high_scores.append(new_h)
    # If index in middle/front of the list
    else:
        # Only Allow top 6 high scores to be saved
        if len(high_scores) > 6: r = 6
        else: r = len(high_scores)

        # Insert new high score first
        high_scores.insert(i, new_h)
        # Loop through remaining scores, updating their ranking
        for k in range(i+1, r):
            to_replace = str(k) + ' -'
            new_hs = str(k+1) + ' -'
            high_scores[k].replace(to_replace, new_hs)

    print('YOU MADE THE HIGH SCORE BOARD')
    
    # Write in new high scores
    with open('high_score.txt', "w") as hs:
        hs.writelines(high_scores)


def get_answer():
    answer = (input().strip()).lower()
    while answer != 'y' and answer != 'n':
        print('Wrong Entry! Type Y or N')
        answer = (input().strip()).lower()
    if answer == 'y':
        return True
    return False


def get_wager():
    wager = input().strip()
    while not check_wager(wager):
        print('Wrong Entry! Place an integer wager between 1 and 1000!')
        wager = input().strip()
    return int(wager)


# Validate wager
def check_wager(wager: str):
    if wager.isdigit() and 1000 >= int(wager) >= 1:
        return True
    else:
        return False


def hit(person, deck):
    person.cards.append(deck.deal())

    if person.is_player():
        print('You were dealt - ', str(person.cards[-1]))


def check_move(move):
    if move != 'a' and move != 'b' and move != 'c':
        return False
    return True


def think():
    for i in range(3):
        sleep(0.3)
        print(".", end=" ")
