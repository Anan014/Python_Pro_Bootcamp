from art import logo
import os

print(logo)

winner_name = ""
winner_bid = 0
next_bid = True
bids_dict = {}

while next_bid:
    name = input("Whats your name? ")
    bid = int(input("Whats your bid? "))
    bids_dict[name] = bid
    if bid > winner_bid:
        print("winner_bid")
        winner_name = name
        winner_bid = bid
    ask = input("Other users wants to bid? 'yes' or 'no' ").lower()
    if ask == "no":
        next_bid = False
    os.system("cls" if os.name == "nt" else "clear")

print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
