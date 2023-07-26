#Welcome to my first portolio project! I will be building a terminal game to play blackjack!

from game_func import *

#Here create the user input required to begin the game. if yes run begin game and print the intro.
print(intro)
player_name = input(""" \n ___________________________________________ \n \n Hello player, what's your name? \n ___________________________________________ \n""")

while True:

    ready_to_play = input("Would you like to continue playing? (y/n) ")

    if (ready_to_play.lower() == "y"):
        deck = initialise_deck()
        game_deck(deck)
        print(""" \n ___________________________________________ \n  \n Let's go! \n ______________________________________________ \n""")
    else:
        print("Come back another time!")
        quit()


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
    player1.show_score()

    dealer.hand.append(deck.pop())
    dealer.hand.append(deck.pop())
    dealer.show_dealer_cards()
    dealer.calc_score()


    #assess dealer and player objects to see if playing is True, if either is true, continue game until both are in agreement to declare a winner
    #Take players next move, they will move before dealer and 
    while (player1.is_playing or dealer.is_playing):
        next_move = input(""" \n ___________________________________________ \n Do you want to hit or stick? (hit/stick) \n ___________________________________________ \n""")
        if (next_move.lower() == "stick"):
            player1.is_playing = False
        elif (next_move.lower() == 'hit'):
            player1.hand.append(deck.pop())
            print("\n ___________________________________________ \n \n {} receives a new card. \n ___________________________________________ \n".format(player1.name))
            player1.show_player_cards()
            player1.calc_score()
            player1.show_score()
            if (player1.score > 21):
                print("""\n ___________________________________________ \n \n" {} has gone bust. \n ___________________________________________ \n""".format(player1.name))
                player1.is_bust = True
                end_game(player1,dealer)
                break
        
        if (dealer.score < 17):
            dealer.hand.append(deck.pop())
            
            print("""\n ___________________________________________ \n \n" Dealer draws a new card. \n ___________________________________________ \n""")
            dealer.calc_score()
            dealer.show_dealer_cards()
            if (dealer.score > 21):
                dealer.show_score
                print("""\n ___________________________________________ \n \n" Dealer has gone bust. \n ___________________________________________ \n""")
                dealer.show_score()
                dealer.is_bust = True
                end_game(player1,dealer)
                break
                
        else:
            dealer.is_playing = False
        

    #All players must show their hand to announce a winner fairly.
    player1.show_player_cards()
    dealer.show_player_cards()


        
    #Now both players have finished their plays, it is time to declare a winner!
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