#Welcome to my first portolio project! I will be building a terminal game to play blackjack!

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




        


#Here create the user input required to begin the game. if yes run begin game and print the intro.


#Deal initial cards to player and dealer


#show all cards on the table (as a function)



#assess dealer and player objects to see if playing is True, if either is true, continue gamne




#when both players finished their plays, 

suits = ["Hearts", "clubs", "Spades", "Diamonds"]
values = [1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
deck = []

#Create a function to intialise the deck for any fresh game
def initialise_deck():
    deck = []
    for suit in suits:
        for value in values:
            deck.append([suit,value])


#Create the dealer/player class, do they need to be separate or the same?
class Dealer:
    dealers_hand = []
    is_playing = True
    def __init__(self) -> None:
        pass
    
    def __repr__(self) -> str:
        return "This is the dealer, please dont touch!"

    def begin_game():
        pass


initialise_deck() 
print(deck)
        
