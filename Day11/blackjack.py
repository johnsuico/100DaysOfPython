import art, card_deck, random, os

clear = lambda: os.system('cls')

def deal_deck_start():
    temp_deck = []
    temp_deck.append(random.choice(list(card_deck.card_deck)))
    temp_deck.append(random.choice(list(card_deck.card_deck)))
    return temp_deck

def deal_deck():
    return random.choice(list(card_deck.card_deck))

def calc_card_total(deck):
    total = 0
    temp_total = 0
    for card in deck:
        if card == "Ace":
            temp_total += card_deck.card_deck[card][1]
            if temp_total > 21:
                total += card_deck.card_deck[card][0]
            else:
                total += card_deck.card_deck[card][1]
        else:
            total += card_deck.card_deck[card]
    return total

def hit_input():
    hit = input("Would you like to get another card? Type 'y' or 'n': ").lower()

    if hit == 'y':
        return True
    else:
        return False

def print_hands(player_hand, player_total, dealer_hand, dealer_total):
    print(f"Player cards: {player_hand} Total: {player_total}")
    print(f"Dealer cards: {dealer_hand} Total: {dealer_total}\n\n")


# Create variables to hold player and dealers hand + total
player_hand = []
player_total = 0
dealer_hand = []
dealer_total = 0

# START GAME
clear()
print(art.logo)

# play_choice = input("Would you like to play blackjack? Type 'y' for yes and 'n' for no. ").lower()

# Deal to players
player_hand = deal_deck_start()
dealer_hand = deal_deck_start()

# Calculate totals
player_total = calc_card_total(player_hand)
dealer_total = calc_card_total(dealer_hand)

print(f"Player cards: {player_hand} Total: {player_total}")
print(f"Dealer cards: {dealer_hand[0]} Value: {card_deck.card_deck[dealer_hand[0]]}")

hit = hit_input()

while hit:

    if dealer_total <= 16:
        dealer_hand.append(deal_deck())
        dealer_total = calc_card_total(dealer_hand)
        
    player_hand.append(deal_deck())
    player_total = calc_card_total(player_hand)

    if player_total > 21:
        hit = False
        break

    print(f"Player cards: {player_hand} Total: {player_total}")
    print(f"Dealer cards: {dealer_hand[0]} Value: {card_deck.card_deck[dealer_hand[0]]}")

    hit = hit_input()

# Check who has the higher cards
if player_total > 21:
    print("\n\nPLAYER BUST")
    print("DEALER WINS")
    print_hands(player_hand, player_total, dealer_hand, dealer_total)
elif dealer_total > 21:
    print("\n\nDEALER BUST")
    print("PLAYER WINS")
    print_hands(player_hand, player_total, dealer_hand, dealer_total)
elif player_total > dealer_total:
    print("\n\nPLAYER WINS")
    print_hands(player_hand, player_total, dealer_hand, dealer_total)
elif player_total == dealer_total:
    print("\n\nDRAW")
    print_hands(player_hand, player_total, dealer_hand, dealer_total)
elif dealer_total > player_total:
    print("\n\nDEALER WINS")
    print_hands(player_hand, player_total, dealer_hand, dealer_total)
elif dealer_total > 21 and player_total > 21:
    print("\n\nNo one wins")
    print_hands(player_hand, player_total, dealer_hand, dealer_total)