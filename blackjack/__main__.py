#!/usr/bin/env python3
from time import sleep
from deck import Deck
from person import Person
from helpers import *

# Function that actually plays BJ Game
# Takes in Objects for player, dealer, deck, and int value for wager
def play(player, dealer, deck, wager):
    # Initialize necessary  variables for game
    result = 7  # result of current hand - assigned arbitrary value
    hand = 0  # Current hand
    revealed_cards = []  # 'Hole' Cards revealed by dealer
    stand = False
    doubledown = False
    winnings = 0  # Total profit/loss

    while result > 5:
        hand += 1
        print('HAND ' + str(hand))
        print(dealer.get_name() + ' is dealing - \n')

        for i in range(2):
            if hand < 2 or max(dealer.get_value()) <= 16:
                hit(dealer, deck)
            if not stand:
                hit(player, deck)
                if doubledown:
                    stand = True
            
            #if not first hand don't iterate
            if hand > 1: break

        # Prints 'Hole' Cards
        revealed_cards.append(dealer.reveal(hand))
        print('DEALER CURRENTLY SHOWS:')
        for i in revealed_cards:
            print('Card : ' + str(i))
        think()

        # Evaluates hands for player and dealer
        d_hand = check_hand(dealer)
        p_hand = check_hand(player)
        result = evaluate_hands(d_hand, p_hand)

        # If neither player nor dealer have gotten BJ or Bust
        if result == 6:
            print("Your Hand is " + p_hand)

            if not stand:
                # Take in, validate and execute next move
                print("Enter next move - Hit(A) Stand(B) Double Down(C) :")
                move = (input().strip()).lower()
                while not check_move(move):
                    print('Wrong Entry! Type A, B or C!')
                    move = (input().strip()).lower()

                if move == 'b':
                    stand = True
                elif move == 'c':
                    wager *= 2
                    doubledown = True
                continue

            # if both dealer and player stop playing
            elif max(dealer.get_value()) > 15:
                print("The Game is Over as neither you nor Jack can play")
                print('Calculating Who Won:')
                think()

                # Calculate who won
                fin_eval = final_eval(player, dealer)
                if fin_eval == 0: # Player's Hand > Dealer's
                    winnings += wager * 0.5
                    print("You beat the dealer! and Won $" + str(wager * 0.5))
                    print('Total winnings = ' + str(winnings))

                elif fin_eval == 1:# Dealer's Hand > Player's
                    winnings -= wager
                    print("The dealer beat you! and you " +
                          "lost your wager of $" + str(wager))
                    print('Total winnings = ' + str(winnings))

                else:
                    print("It's a tie!")
                    print('Total winnings = ' + str(winnings))

            # if Dealer can play but player can't
            else:
                if doubledown:
                    choice = "Double Down"
                else:
                    choice = "Stand"

                print("You cannot take another hit as you chose to " + choice)
                continue

        # Dealer and Player BlackJack
        elif result == 0:
            winnings += 0
            print('Double BlackJack! - You win nothing: Total winnings = $' + str(winnings))

        # Only Dealer BlackJack
        elif result == 1:
            winnings -= wager
            print('Dealer BlackJack! - You lost your wager of $' + str(wager))
            print('Total winnings = ' + str(winnings))

        # Only Player BlackJack
        elif result == 2:
            winnings += wager
            print("BlackJACK!!! - You won $" + str(wager))
            print('Total winnings = ' + str(winnings))

        # Dealer and Player Bust
        elif result == 3:
            winnings += 0
            print('Double Bust! - You win nothing: Total winnings = $' + str(winnings))

        # Dealer Bust
        elif result == 4:
            winnings += wager * 0.5
            print("Dealer Bust!!! - You won $" + str(wager * 0.5))
            print('Total winnings = ' + str(winnings))

        # Player Bust
        elif result == 5:
            winnings -= wager
            print('BUST! - You lost your wager of $' + str(wager))
            print('Total winnings = ' + str(winnings))

        # If Current game is over, ask to restart
        print('Would you like to play again? (Y/N)')

        if get_answer():
            print('Thank you for playing again')

            # Re-instantiate necessary variables
            player.empty_cards()
            dealer.empty_cards()
            deck.new_deck()
            deck.shuffle()
            result = 7
            hand = 0
            revealed_cards = []
            stand = False
            doubledown = False

            print('Give ' + dealer.get_name() + ' a moment to reset the table')
            think()

            print('Do you want to change your wager? (Y/N)')
            if get_answer():
                # Take in integer wager and check if valid
                print('\nPlace an integer wager between 1 and 1000 and hit Enter to begin')
                wager = get_wager()

            print("LET'S PLAY!")

        else: return winnings

# driver function for Game
def main():

    print('''Hello and Welcome to Abhi's Blackjack Game\n
    Here are the RULES:\n
    To begin, you will place a bet (winning 1:1 if you beat the house and 3:2 
    if you get Blackjack)\n
    To win you either need to get blackjack (21) or the house dealer needs 
    exceed 21\n
    After initial two cards have been dealt to you and the dealer you can choose
     to either:\n
        A: Hit - receive another card\n
        B: Stand - Stop playing where you are\n
        C: Double Down - you double your wager and take one final hit''')

    # Take in integer wager and check if valid
    print('\nPlace an integer wager between 1 and 1000 and hit Enter to begin')
    wager = get_wager()

    # Take in Name - no need to check validity
    print('You have bet $', wager, '\n Now Enter your Name please? . . . ')
    name = input().strip()
    print("Thanks " + name + ', the game will now commence!')

    # Instantiate deck and 'shuffle' it
    deck = Deck()
    print('Cards are being shuffled', end = " ")
    think()  # sleeps for <1 second
    deck.shuffle()
    print('\n')

    # Instantiate necessary objects for game
    player = Person('player', [], name)
    dealer = Person('dealer', [])

    # Loop containing main game, returns winnings when done
    try:
        winnings = play(player, dealer, deck, wager)
    except:
        print("oops something went wrong here," + 
        "so let's just say no win no loss?")
        winnings = 0

    print("Thank you for Playing")
    if winnings >= 0:
        print("You have won a total of $" + str(winnings))
    else:
        print("You have lost a total of $" + str(winnings))

    # Check/save/print current winnings as high score
    save_high_score(winnings, player)
    print_high_scores()

    print("\n GOODBYE: Please play again sometime :)")
    #Please also take me on as a KP Fellow :)


if __name__ == "__main__":
    main()

