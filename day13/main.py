from art import logo
from art import vs
from game_data import data
import random
import os


def format_data(data):
    """format the account data into a printable format"""
    return f"{data['name']}, {data['description']}, from {data['country']}."


def random_data_num():
    return random.randint(0, len(data) - 1)


sum = 0
correct = True
rand1 = random_data_num()

while correct:
    print(logo)
    if sum > 0:
        print(f"You're right! Current score: {sum}.")
    rand2 = random_data_num()
    while rand2 == rand1:
        rand2 = random_data_num()
    data1 = data[rand1]
    data2 = data[rand2]
    print(f"Compare A: {format_data(data1)}")
    print(vs)
    print(f"Against B: {format_data(data2)}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if data1["follower_count"] > data2["follower_count"] and answer == "a":
        sum += 1
        rand1 = rand2
        os.system("cls" if os.name == "nt" else "clear")
    elif data1["follower_count"] < data2["follower_count"] and answer == "b":
        sum += 1
        rand1 = rand2
        os.system("cls" if os.name == "nt" else "clear")
    else:
        correct = False
        os.system("cls" if os.name == "nt" else "clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {sum}.")
