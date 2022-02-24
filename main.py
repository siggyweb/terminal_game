#Welcome to my first portolio project! I will be building a terminal game to play blackjack!

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
        print("{name}'s score is: {points}".format(name=self.name,points=total))
        self.score = total

    def show_dealer_cards(self):
        face_down_card = self.hand[0]
        face_up_cards = self.hand[1:]
        print(" \n ___________________________________________ \n \n you cannot see the dealer's first card. " + "You can see: " + str(face_up_cards) + "\n ___________________________________________ \n")
        

    def show_player_cards(self):
        print("My cards are: " + str(self.hand))
            

#Function to end the game, has been tested.
def end_game(p1,p2):
    p1.is_playing = False
    p2.is_playing = False




        

#Here create the user input required to begin the game. if yes run begin game and print the intro.
print(intro)

player_name = input(""" \n ___________________________________________ \n \n Hello player, what's your name? \n ___________________________________________ \n""")
ready_to_play = input("Would you like to play a game of chance? (y/n) ")

if (ready_to_play.lower() == "y"):
    deck = initialise_deck()
    game_deck(deck)
    print(""" \n ___________________________________________ \n  \n Let's go! \n ______________________________________________ \n""")
else:
    "Come back another time!"

#instantiate players and card objects
player1 = Player(player_name)
dealer = Player("Dealer")
initialise_deck()
game_deck(deck)

#Deal initial cards to player and dealer and display opening hands
print("""\n ___________________________________________ \n \n Opening Hands: \n ______________________________________________ \n""")
player1.hand.append(deck.pop())
player1.hand.append(deck.pop())
player1.show_player_cards()
player1.calc_score()

dealer.hand.append(deck.pop())
dealer.hand.append(deck.pop())
dealer.show_dealer_cards()
dealer.calc_score()


#assess dealer and player objects to see if playing is True, if either is true, continue game until both are in agreement to declare a winner

while (player1.is_playing or dealer.is_playing):
    next_move = input(""" \n ___________________________________________ \n Do you want to hit or stick? (hit/stick) \n ___________________________________________ \n""")
    if (dealer.score < 17):
        dealer.hand.append(deck.pop())
        
        print("""\n ___________________________________________ \n \n" Dealer draws a card. \n ___________________________________________ \n""")
        dealer.calc_score()
        dealer.show_dealer_cards()
        if (dealer.score > 21):
            print("""\n ___________________________________________ \n \n" Dealer has gone bust. \n ___________________________________________ \n""")
            dealer.is_bust = True
            end_game(player1,dealer)
            
    else:
        dealer.is_playing = False
    
    if (next_move.lower() == "stick"):
        player1.is_playing = False
    elif (next_move.lower() == 'hit'):
        player1.hand.append(deck.pop())
        print("\n ___________________________________________ \n \n {} draws a card. \n ___________________________________________ \n".format(player1.name))
        player1.show_player_cards()
        player1.calc_score()
        if (player1.score > 21):
            print("""\n ___________________________________________ \n \n" {} has gone bust. \n ___________________________________________ \n""".format(player1.name))
            player1.is_bust = True
            end_game(player1,dealer)
    
#when both players finished their plays, it is time to calculate score and declare a winner!
if (player1.is_bust and not dealer.is_bust):
    print(house_wins)
elif (not player1.is_bust and dealer.is_bust):
    print(player_wins)
elif (dealer.score > player1.score and not dealer.is_bust):
    print(house_wins)
elif (player1.score > dealer.score and not player1.is_bust):
    print(player_wins)
elif (dealer.score == player1.score):
    print(draw)