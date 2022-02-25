

import random


intro = """
___.   .__                 __          ____.              __       _________.__         
\_ |__ |  | _____    ____ |  | __     |    |____    ____ |  | __  /   _____/|__| _____  
 | __ \|  | \__  \ _/ ___\|  |/ /     |    \__  \ _/ ___\|  |/ /  \_____  \ |  |/     \ 
 | \_\ \  |__/ __ \\  \___|    <  /\__|    |/ __  \  \___|    <   / ___ \  \|  |  |  Y Y \\
 |___  /____(____  /\___  >__|_ \ \________(____  /\___  >__|_ \ /_______  /|__|__|_|  /
     \/          \/     \/     \/               \/     \/     \/         \/          \/ 
                                                                                                  
  ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/                                                                                                                                                                                                
  ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/ 
                                                                                                                                                                                                     

                                                .___     _________ 
                    _______   ____ _____     __| _/__.__.\_____   \\
                    \_  __ \_/ __ \\__  \   / __ <   |  |   /   __/
                    |  | \/\  ___/ / __ \_/ /_/ |\___  |  |   |   
                    |__|    \___  >____  /\____ |/ ____|  |___|   
                                \/     \/      \/\/       <___>   
   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  
   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/                               
                                                                                                                                                                                                   
"""

house_wins = """ \n

█░█ █▀█ █░█ █▀ █▀▀   ▄▀█ █░░ █░█░█ ▄▀█ █▄█ █▀   █░█░█ █ █▄░█ █▀
█▀█ █▄█ █▄█ ▄█ ██▄   █▀█ █▄▄ ▀▄▀▄▀ █▀█ ░█░ ▄█   ▀▄▀▄▀ █ █░▀█ ▄█
   \n """

draw = """ \n
▀█▀ ▀▀█▀▀ █ █▀▀ 　 █▀▀█ 　 █▀▀▄ █▀▀█ █▀▀█ █░░░█ █ 
▒█░ ░░█░░ ░ ▀▀█ 　 █▄▄█ 　 █░░█ █▄▄▀ █▄▄█ █▄█▄█ ▀ 
▄█▄ ░░▀░░ ░ ▀▀▀ 　 ▀░░▀ 　 ▀▀▀░ ▀░▀▀ ▀░░▀ ░▀░▀░ ▄ \n"""


player_wins = """\n
▒█▀▀█ █▀▀█ █▀▀█ █▀▀▄ 　 █▀▀ █░░█ █▀▀█ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀▄ █▀▀▀ 　 ▒█▀▀█ █▀▀█ █░░░█ █▀▀▄ █▀▀█ █░░█ █ 
▒█░▄▄ █░░█ █░░█ █░░█ 　 ▀▀█ █▀▀█ █░░█ █░░█ ░░█░░ ▀█▀ █░░█ █░▀█ 　 ▒█░░░ █░░█ █▄█▄█ █▀▀▄ █░░█ █▄▄█ ▀ 
▒█▄▄█ ▀▀▀▀ ▀▀▀▀ ▀▀▀░ 　 ▀▀▀ ▀░░▀ ▀▀▀▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀▀ 　 ▒█▄▄█ ▀▀▀▀ ░▀░▀░ ▀▀▀░ ▀▀▀▀ ▄▄▄█ ▄ \n"""


suits = ["Hearts", "clubs", "Spades", "Diamonds"]
values = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

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
    


#Create the dealer/player class, do they need to be separate or the same?
class Player:
    is_playing = True
    is_bust = False
    def __init__(self,name) -> None:
        self.name = name
        self.hand = []
        self.score = 0
    
    def __repr__(self) -> str:
        #Desc of the player
        return "This is {}, please dont touch my cards!".format(self.name)

    def calc_score(self):
        #This will be the dominant function in deciding what will happen next in the game, players need their score to be able to progress accordingly.
        total = 0
        has_ace = False
        for card in self.hand:
            if (card[1] == "Jack" or card[1] == "Queen" or card[1] == "King"):
                total += 10
            elif (card[1] == "Ace"):
                total += 11
                has_ace = True
            else:
                total += card[1]
        if (total > 21 and has_ace):
            total -= 10
        self.score = total


    def show_score(self):
         print("{name}'s score is: {points}".format(name=self.name,points=self.score))   

    def show_dealer_cards(self):
        face_down_card = self.hand[0]
        face_up_cards = self.hand[1:]
        print(" \n ___________________________________________ \n \n you cannot see the dealer's first card. " + "You can see: " + str(face_up_cards) + "\n ___________________________________________ \n")
        

    def show_player_cards(self):
        print(" \n {name}'s cards are: ".format(name=self.name) + str(self.hand))
            

#Function to end the game, has been tested.
def end_game(p1,p2):
    p1.is_playing = False
    p2.is_playing = False
