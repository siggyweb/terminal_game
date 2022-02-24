#Welcome to my first portolio project! I will be building a terminal game to play blackjack!

import random






intro = """
___.   .__                 __          ____.              __       _________.__         
\_ |__ |  | _____    ____ |  | __     |    |____    ____ |  | __  /   _____/|__| _____  
 | __ \|  | \__  \ _/ ___\|  |/ /     |    \__  \ _/ ___\|  |/ /  \_____  \ |  |/     \ 
 | \_\ \  |__/ __ \\  \___|    <  /\__|    |/ __ \\  \___|    <   /        \|  |  Y Y  \
 |___  /____(____  /\___  >__|_ \ \________(____  /\___  >__|_ \ /_______  /|__|__|_|  /
     \/          \/     \/     \/               \/     \/     \/         \/          \/ 
                                                                                                  
  ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/                                                                                                                                                                                                
  ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/ 
                                                                                                                                                                                                     

                                                .___     _________ 
                    _______   ____ _____     __| _/__.__.\_____   \
                    \_  __ \_/ __ \\__  \   / __ <   |  |   /   __/
                    |  | \/\  ___/ / __ \_/ /_/ |\___  |  |   |   
                    |__|    \___  >____  /\____ |/ ____|  |___|   
                                \/     \/      \/\/       <___>   
   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  
   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/                               
                                                                                                                                                                                                   
"""


suits = ["Hearts", "clubs", "Spades", "Diamonds"]
values = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]

#Create a function to intialise the deck for any fresh game
def initialise_deck():
    deck = []
    for suit in suits:
        for value in values:
            deck.append([suit,value])
    return deck

#Take initialised deck and shuffle it ready for game
def game_deck(deck):
    new_deck = random.shuffle(deck)
    

deck = initialise_deck()
game_deck(deck)
#print(deck)


#Create the dealer/player class, do they need to be separate or the same?
class Player:
    is_playing = True
    def __init__(self,name) -> None:
        self.name = name
        self.hand = []
        self.score = 0
    
    def __repr__(self) -> str:
        #Desc of the player
        return "This is {}, please dont touch my cards!".format(self.name)

    def calc_score():
        #This will be the dominant function in deciding what will happen next in the game, players need their score to be able to progress accordingly.
        total = 0
        has_ace = False
        for card in self.hand:
            if (card[1] == "Jack" or card[1] == "Queen" or card[1] == "King"):
                total += 10
            elif (card[1] == "Ace"):
                total += 11
                has_ace = True
        if (total > 21 and has_ace):
            total -= 10





        

#Here create the user input required to begin the game. if yes run begin game and print the intro.

#Deal initial cards to player and dealer

#show all cards on the table (as a function)

#assess dealer and player objects to see if playing is True, if either is true, continue gamne

#when both players finished their plays, 