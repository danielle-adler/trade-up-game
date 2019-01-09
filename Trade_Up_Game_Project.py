# Danielle Adler's Trade Up Game Project 1


class item:
    """Creating each item with name, tier, and size"""

    # Defining item name, item tier, and item size
    def __init__(self, name_i, tier, size):
        """Initializing the item name, tier, and size of each item"""
        self.name_i = name_i
        self.tier = tier
        self.size = size

    # Printing the labels when someone selects an item
    def item_label(self):
        """Printing a label showing the items attributes"""
        label_to_print = ("\nYou have selected " + self.name_i
                          + " in tier " + str(self.tier) + ".")
        return label_to_print


class store:
    """Creating each store with name and the specific items in the store"""

    # Defining the name of and items in the store
    def __init__(self, name_s, items_in_store):
        """Initializing the store name and items within it"""
        self.name_s = name_s
        self.items_in_store = items_in_store

    def store_name_print(self):
        """Printing a label showing the store's name"""
        store_label = ("You are in " + self.name_s
                       + ". These are the items in the store: ")
        return store_label

    # Printing the items when someone is in a specific store
    def items_in_store_print(self):
        i = 1

        # Iterating through and printing the items in the store
        for item in self.items_in_store:
            print("[", str(i), "] ", item.name_i, sep="", end="  ")
            i += 1


class User:
    """Creating the user trading and exceptions within the game"""

    def __init__(self, item):
        """Initializing the user adding items to their hand"""
        self.item = item    # When the game first starts, the item is a pen
        self.add = False    # If tier trading is correct, this will set to True

    def tier_trading(self, item):
        """All of the rules around tier trading (lower tier to one higher tier)
        exceptions for skipping tiers, exceptions for size of an item, and
        exceptions for stores that won't trade with one another"""

        # Initial tier is the item the user has going into the store and final
        # tier is the item the user has when leaving the store
        initial_tier = self.item.tier
        final_tier = item.tier

        # Not allowing items that are too large to be carried
        if item.size is False:
            self.add = False
            print("The", item.name_i, "is too big to carry around the mall." +
                  "\nPlease select a different item.\n\nAfter you have" +
                  " checked all items, if no item of the proper tier" +
                  " exists\nplease type [4] to leave the store.")

        # Standard jumping of tier trading and checking to make sure the final
        # tier is one tier higher than the initial tier
        elif final_tier == initial_tier + 1:
            self.add = True

        # Jumping exceptions; if the initial item is earrings, that can jump
        # to purse, and if the initial item is iPod_Shuffle, that can jump
        # to Air_Jordan_Space_Jam_11
        elif self.item.name_i == 'Earrings' and item.name_i == 'Purse':
            self.add = True
            print("You have hit a jumping exception and get to skip a tier!")

        elif (self.item.name_i == 'iPod_Shuffle' and
              item.name_i == 'Air_Jordan_Space_Jam_11'):
            self.add = True
            print("You have hit a jumping exception and get to skip a tier!")

        # If the tier is not acceptable we have to set self.add back to False
        else:
            self.add = False
            print("You are not allowed to select items in that tier."
                  "\n\nPlease pick another item one tier higher than your" +
                  " current tier.\n\nAfter you have checked all items," +
                  " if no item of the proper tier exists,\nplease type [4]" +
                  " to leave the store.")

    def carry(self, item):
        """Making the added item the item you are carrying to the next store"""

        # If you can add with the tier,
        # you have to check that its viable to carry
        if self.add is True:

            # This takes the new item and makes it your current item
            if item.size is True:
                self.item = item


class Turns:
    """Counting the number of turns taken"""

    def __init__(self):
        """Starting at turn 0 with a pen"""
        self.turn = 0

    def end_turn(self):
        """Adding one turn each time the user leaves a store"""
        self.turn += 1


def while_in_store(store, user, turn, In_Store):
    """Characteristics for what will happen within each store"""

    while In_Store:
        user_choice = input("\n\nPlease select either [1], [2], [3] for" +
                            " items, [4] to exit the store, or [Q] to" +
                            " quit the game\n >>> ").upper()

        # Giving the user the option to leave the store and
        # still remind them of where they are in the game
        if user_choice == "4":

            turn.end_turn()
            print("You are on tier ", user.item.tier, ".", sep="")
            print("You have exited ", store.name_s, ".", sep="")

            In_Store = False

        # Exiting out of the whole game; global Loop allows the user to break
        # out of both while loops simultaneously
        elif user_choice == "Q":
            global Loop
            Loop = False
            break

        # Allowing users to select their choice with a number
        # and then printing the relevant item label
        elif user_choice in ["1", "2", "3"]:

            x = store.items_in_store[int(user_choice) - 1]
            print(x.item_label())

            old_item = user.item.name_i

            if (store.name_s == 'Coach' and old_item in
               ['Air_Jordan_Space_Jam_11', 'Yeezy_Sneakers', 'Sweatshirt']):
                print("Sorry, Flight Club's items are not accepted in" +
                      " Coach.\nPLease select [4] to exit the store.")

            elif (store.name_s == 'Flight_Club' and old_item in
                  ['Keychain', 'Purse', 'Luggage']):
                print("Sorry, Coach's items are not accepted in" +
                      " Flight_Club.\nPLease select [4] to exit the store.")

            else:
                # Trading out old items and adding new items to the given hand
                user.tier_trading(x)
                user.carry(x)

                if user.add is True:

                    # Printed message when someone has been successful in
                    # trading one item for another (old item for new item)
                    print("You have been successful in trading ", old_item,
                          " for ", user.item.name_i, ".", sep="")

                    # Ending the turn and printing relevant information
                    # for the user to keep track of their turn and their tier
                    turn.end_turn()
                    print("You are on tier ", user.item.tier, ".\n\n" +
                          "You have exited ", store.name_s, ".", sep="")
                    In_Store = False

        # Making sure that the user only selects items with numbers
        # 1, 2, 3 or 4 to leave the store, or Q to quit the game
        else:
            print("Please select [1], [2], [3], [4], or [Q] only.")


# Initializing all of the items
Pen = item('Pen', 0, True)
Tshirt = item('Tshirt', 1, True)
Jeans = item('Jeans', 2, True)
Couch = item('Couch', 4, False)
iPhone_5 = item('iPhone_5', 3, True)
Mini_Fridge = item('Mini_Fridge', 3, False)
iPod_Shuffle = item('iPod_Shuffle', 2, True)
Surfboard = item('Surfboard', 3, False)
Beach_Towel = item('Beach_Towel', 1, True)
Bathing_Suit = item('Bathing_Suit', 2, True)
Earrings = item('Earrings', 1, True)
Necklace = item('Necklace', 2, True)
Makeup = item('Makeup', 1, True)
Keychain = item('Keychain', 1, True)
Purse = item('Purse', 3, True)
Luggage = item('Luggage', 4, True)
Air_Jordan_Space_Jam_11 = item('Air_Jordan_Space_Jam_11', 4, True)
Yeezy_Sneakers = item('Yeezy_Sneakers', 4, True)
Sweatshirt = item('Sweatshirt', 2, True)


# Initializing all of the stores
Urban_Outfitters = store('Urban_Outfitters', [Tshirt, Jeans, Couch])
Best_Buy = store('Best_Buy', [iPhone_5, Mini_Fridge, iPod_Shuffle])
Billabong = store('Billabong', [Surfboard, Beach_Towel, Bathing_Suit])
Claires = store('Claires', [Earrings, Necklace, Makeup])
Coach = store('Coach', [Keychain, Purse, Luggage])
Flight_Club = store('Flight_Club', [Air_Jordan_Space_Jam_11,
                                    Yeezy_Sneakers, Sweatshirt])

# User introduction to the game
print("\n\nWelcome to the The Trade Up game!\n\n" +
      "You will start with a pen and work to" +
      " trade up to something extravagant.\n\n" +
      "You will go through stores in the mall trying to trade one item for" +
      "\nanother with a slightly higher monetary value. You will continue to" +
      "\ntrade items until you have something awesome, like" +
      " Yeezy_Sneakers.\n\nYou will have 4 tiers of items to go through" +
      " not including the pen.\nSome items throughout the game will" +
      " have different rules, so keep a lookout!\n\n" +
      "Your turn will begin each time you enter a store" +
      " and end when you exit.\nAnd be aware, that you only have 6 turns to" +
      " get to the best item,\na tier 4 item, to win.\n\nYour current tier" +
      " and turn will always be displayed,\nand I will be guiding you the" +
      " whole time.\nMost importantly, good luck and have fun!\n")

Loop = True
turn = Turns()
user = User(Pen)

# While loop for game logic going through each store
while Loop:

    if user.item.tier == 4 and user.add is True:
        print("Congrats! You have WON THE GAME!")
        break

    if turn.turn >= 6:
        print("You LOSE the game because that was your 6th turn." +
              " Try again next time!")
        break

    # Stating the number of users turns
    print("You have completed turn number ", turn.turn, ".\n", sep="")
    if turn.turn == 5:
        print("You have one more turn to go!\n")

    users_select = input("Pick a store [1] Urban_Outfitters, [2] Best_Buy," +
                         " [3] Billabong, [4] Claires, [5] Coach, [6]" +
                         " Flight_Club, or [Q] to quit the game\n >>>").upper()

    if users_select == "Q":
        print("You have selected [Q] and quit the game.")
        break

    if users_select == "1":

        # Reminding the users of which store they are in
        # and printing the items for that store
        a = Urban_Outfitters.store_name_print()
        print(a)
        Urban_Outfitters.items_in_store_print()

        In_Store = True

        while_in_store(Urban_Outfitters, user, turn, In_Store)

    elif users_select == "2":

        # Reminding the users of which store they are in
        # and printing the items for that store
        a = Best_Buy.store_name_print()
        print(a)
        Best_Buy.items_in_store_print()

        In_Store = True

        while_in_store(Best_Buy, user, turn, In_Store)

    elif users_select == "3":

        # Reminding the users of which store they are in
        # and printing the items for that store
        a = Billabong.store_name_print()
        print(a)
        Billabong.items_in_store_print()

        In_Store = True

        while_in_store(Billabong, user, turn, In_Store)

    elif users_select == "4":

        # Reminding the users of which store they are in
        # and printing the items for that store
        a = Claires.store_name_print()
        print(a)
        Claires.items_in_store_print()

        In_Store = True

        while_in_store(Claires, user, turn, In_Store)

    elif users_select == "5":

        # Reminding the users of which store they are in
        # and printing the items for that store
        a = Coach.store_name_print()
        print(a)
        Coach.items_in_store_print()

        In_Store = True

        while_in_store(Coach, user, turn, In_Store)

    elif users_select == "6":
        # Reminding the users of which store they are in
        # and printing the items for that store
        a = Flight_Club.store_name_print()
        print(a)
        Flight_Club.items_in_store_print()

        In_Store = True

        while_in_store(Flight_Club, user, turn, In_Store)

    else:
        print("Please select [1], [2], [3], [4], [5], [6], or [Q] to quit" +
              " the game only")
