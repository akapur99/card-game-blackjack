# DESIGN: Blackjack
### Abhimanyu Kapur, 2019

## Instructions
*To run*:
`python ./blackjack/__main__.py`

*To install as package*
`./install.sh`
Though not really much need for this

## Rationale for Choice of Tools / Data Structures 

**Language**: Python
I chose Python over other languages such as C, Java, JS, etc. as my goal was to
 create a simple, small and quick card game. The standard library in Python is
 quite useful and abstracts away the implementation of basic data structures 
 and methods - I didn't want to use external libraries so this worked out well. 

**Data Structures**
I didn't use any complex data structures such as `trees`, `dictionaries`
 (`hashtables`) or searching/sorting algorithms as I didn't think any were
 needed in this project (I initially implemented `binary search` to deal with
 aces and face cards but refactored my code rendering it unnecessary). I used
 created `Person` and `Deck` classes as to represent the player/dealer and the
 deck of cards. This helped me simplify the code and make it more intuitive.
 I use `lists` to represent the card decks and hands. I considered using a 
 `dictionary` due to improved time efficiency of indexing - however given that 
 the size of the card deck would be a max of 52 and hands would rarely exceed
 9, I didn't think it was necessary. Also I needed to 'randomly' shuffle the 
 card deck, which was easy with a `list`.

**Note about Game Design**:
I've never played Black Jack before, and based most of the game instructions
 on an article. I've realised a little late that splitting is a part of the 
 game hence I wasn't able to include it. Also, I made the game single player,
 although given the design of the program, it would be pretty simple to allow
 multiple players.

## Modules

`__main__` : Driver code which runs the game

`helpers` : Contain useful helper functions

`deck` : Contains `deck` class 

`person` : Contains `Person` class 

## Pseudo code for logic/algorithmic flow
The `blackjack game` will run as follows:

1. Execute from CLI or in IDE
2. In `__main__.py`, `main()` is called
3. Print instructions and take user input for initial wager and name
4. Initialize objects for player, dealer, card deck
5. call `play()` function
6. In `play()`, Initialize necessary  variables for game
7. Start 'playing' within a loop with optional exit condition allowing 
replayability
8. Deal cards to player and dealer (if possible)
9. Show Dealer's 'hole' cards
10. Evaluate player and dealer's hands
11. if no one has BlackJack or has gone bust, let the player choose their next 
move, validate it and `continue`
11. If BlackJack or Bust, add/deduct from winnings and ask player if they want 
to replay
12. If yes, ask to change wager and restart by re-initializing game variables
4. If no, condition to exit loop is met, exit loop and reach end of function
5. Control passes back to `main()`
6. Check and save high_scores (if in top 6)
7. Print high score board
8. The game completes and exit. 

## Testing plan

**Integration testing.** 
  Assembled the game and test it as a whole. In each case, examined the output 
  carefully to be sure it has the correct results. 

  *Edge cases* included wager out of range, incorrect moves given, deleting 
  `high_scores.txt` before running, incorrect answer to yes/no queries.

**Module testing.**
  Tested each function independently.  
