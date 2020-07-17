
import random

nominals = {
    "two": 2, 
    "three": 3, 
    "four": 4, 
    "five": 5, 
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine": 9, 
    "ten": 10, 
    "jack": 2, 
    "queen": 3, 
    "king": 4, 
    "ace": 11 
}
suits = ["spades", "clubs", "hearts", "diamonds"]

available_cards = {}
user_set = []

def get_card(n=1):
    for i in range(n):
        # suit = random.choice(suits)
        suit = random.choice(list(available_cards.keys()))
        nominal = random.choice(available_cards[suit])
        card = {
            "suit": suit,
            "nominal": nominal
        }
        user_set.append(card)
        
        available_cards[suit].remove(nominal)
        
        if len(available_cards[suit]) == 0:
            del available_cards[suit]

def show_user_set():
    print("==============")
    for card in user_set:
        print(card["nominal"], card["suit"])
    print("==============")
        
def calc_scores(player_set):
    scores = 0
    for card in player_set:
        scores += nominals[card["nominal"]]
    return scores

def game():
    # nominals_list = list(nominals.keys())
    for suit in suits:
        # available_cards[suit] = {}
        available_cards[suit] = list(nominals.keys())
        # for nominal in nominals.keys():
            # available_cards[suit][nominal] = nominals[nominal]
    # print(available_cards)

    get_card(2)
    show_user_set()
    print("Your scores:", calc_scores(user_set), "\n")
        
    while True:
        user_action = input("1 - get one more card, 2 - stop\n Your action: ")
        if user_action == "1":
            get_card()
        elif user_action == "2":
            break
        show_user_set()
        print("Your scores:", calc_scores(user_set), "\n")
        
game()
