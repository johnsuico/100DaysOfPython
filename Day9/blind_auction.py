import os

clear = lambda: os.system('cls')
clear()

print("Welcome to the secret auction prgram.")

more_bids = False
bids = {}

def add_bidder():
    name = input("What is your name?: ")
    amount = input("What's your bid?: ")

    bids[name] = amount

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if more_bidders == "yes":
        return True
    else:
        return False

more_bids = add_bidder()

while more_bids:
    clear()
    more_bids = add_bidder()

max_bid = 0
max_bid_person = ""

clear()

for person in bids:
    if int(bids[person]) > max_bid:
        max_bid = int(bids[person])
        max_bid_person = person

print(f"{max_bid_person} has the highest bid with: ${max_bid}")