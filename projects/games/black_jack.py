import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_blackjack():

    want_to_play = True

    while want_to_play:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        print("\n")

        if play != 'y':
            want_to_play = False
            print("Thanks for playing!")
            break

        computer_dealer = []
        user_cards = []

        for i in range(2):
            computer_dealer.append(random.choice(cards))
            user_cards.append(random.choice(cards))

        computer_dealer_total = computer_dealer[0] + computer_dealer[1]
        user_cards_total = user_cards[0] + user_cards[1]

        while user_cards_total > 21 and 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)
            user_cards_total -= 10

        print(f"This is the dealer's first card {computer_dealer[0]}")
        print("\n")
        print(f'These are your cards: {user_cards} with a total of {user_cards_total}')
        print("\n")

        if user_cards_total > 21:
            print("\n"*2)
            print("Dealer win!")
            print("\n")
            print(f"This is the dealer's total {computer_dealer_total} with the following cards: {computer_dealer}")
            print("\n")
            print(f"The following is your total {user_cards_total} with the following cards: {user_cards}")
            continue

        
        while user_cards_total < 21:
            another_card = input("Do you want to draw another card? Type 'y' or 'n': ")

            if another_card.lower() == "y":
                new_card = random.choice(cards)  
                if new_card == 11 and user_cards_total + new_card > 21:
                    new_card = 1
                user_cards.append(new_card)  
                user_cards_total += new_card 

                while user_cards_total > 21 and 11 in user_cards:
                    user_cards.remove(11)
                    user_cards.append(1)
                    user_cards_total -= 10
                print("\n")
                print(f"You drew {new_card}. Your new total is {user_cards_total}.") 

            else:
                break

        if user_cards_total > 21:
            print("\n"*2)
            print("Dealer win!")
            print("\n")
            print(f"This is the dealer's total {computer_dealer_total} with the following cards: {computer_dealer}")
            print("\n")
            print(f"The following is your total {user_cards_total} with the following cards: {user_cards}")
            continue
        
        while computer_dealer_total < 17:
            new_card = random.choice(cards)
            if new_card == 11 and computer_dealer_total + new_card > 21:
                new_card = 1
            computer_dealer.append(new_card)
            computer_dealer_total += new_card


        if computer_dealer_total > 21: 
            print("\n"*2)
            print("You win!")
            print("\n")
            print(f"This is the dealer's total {computer_dealer_total} with the following cards: {computer_dealer}")
            print("\n")
            print(f"The following is your total {user_cards_total} with the following cards: {user_cards}")
        elif computer_dealer_total == user_cards_total:
            print("\n"*2)
            print("Tie!")
            print("\n")
            print(f"This is the dealer's total {computer_dealer_total} with the following cards: {computer_dealer}")
            print("\n")
            print(f"The following is your total {user_cards_total} with the following cards: {user_cards}")     
        elif computer_dealer_total > user_cards_total:
            print("\n"*2)
            print("Dealer Wins!")
            print("\n")
            print(f"This is the dealer's total {computer_dealer_total} with the following cards: {computer_dealer}")
            print("\n")
            print(f"The following is your total {user_cards_total} with the following cards: {user_cards}")
        else: 
            print("\n"*2)
            print("You win!")
            print("\n")
            print(f"This is the dealer's total {computer_dealer_total} with the following cards: {computer_dealer}")
            print("\n")
            print(f"The following is your total {user_cards_total} with the following cards: {user_cards}")
        


play_blackjack()