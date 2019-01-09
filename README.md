# Trade Up Game

## Introduction
The Trade Up game starts simple and can build up to something extravagant. The game is set in a mall and has six stores and four items within each store. The player will start with a pen and go to various stores trading items that progressively get better and better. Essentially, the game is a choose your own journey of sorts, except there are catches, exceptions, and arbitrary rules throughout. 

The Trade Up game should be run from any standard command line. Please call the “Trade_Up_Game_Project.py” file from the command line as opposed to opening up a terminal within Spyder or any other type of software. Then, please follow the prompts and play along! The game will quit when you press [Q] or when you win or lose. I encourage you to play the game as many times as you would like and to take different journeys throughout the mall.

## Coding Elements
The code of the game contains four classes. The first two classes create instances of the items and the stores. All items have a name, tier, and size, while all stores have a name and selected items to go into them. Within each of these classes, I created an initialization method as well as one or two printing methods so that I could easily print specific information about the stores themselves and the items within the stores over and over again.

The third class, the user class contains a large tier trading method that details the rules of trading from one tier to another tier one higher than the current tier. This method also details the ability to jump over given tiers with two specific items, states whether an item is too big to carry, and prohibits the trading of some stores to other stores. The tier_trading method works directly with the carry method that states whether an item is able to be carried around the store, passing the tier trading rules with a Boolean function.

The user class also contains the while_in_store method which details everything that happens within each store. Within this method, I used a global variable to essentially bypass two loops and help the user quit the game whenever they wanted (inside of a store or not). This method is responsible for telling a user if their trade was successful, their current store/tier, etc. and printing helpful messages to guide the user along their journey.

The fourth class, the turn class, kept track of a user’s turns throughout the game. Players lose the game after six turns but are able to win on their sixth turn. On a player’s fifth turn, a helpful message is printed that the player has one turn to go before they lose. The game logic comes last, and the entire game exists in a while loop taking users in and out of each store and keeping track of their turns.
