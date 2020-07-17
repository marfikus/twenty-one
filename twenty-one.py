
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
masti = ["bubi", "trefy", "piki", "chervy"]

available_cards = {}
user_set = []

def get_card(n=1):
    for i in range(n):
        # mast = random.choice(masti)
        mast = random.choice(list(available_cards.keys()))
        nominal = random.choice(available_cards[mast])
        card = {
            "mast": mast,
            "nominal": nominal
        }
        user_set.append(card)
        
        available_cards[mast].remove(nominal)
        
        if len(available_cards[mast]) == 0:
            del available_cards[mast]

def show_user_set():
    print("==============")
    for card in user_set:
        print(card["nominal"], card["mast"])
    print("==============")
        
def calc_scores():
    for card in user_set:
        pass

def game():
    # nominals_list = list(nominals.keys())
    for mast in masti:
        # available_cards[mast] = {}
        available_cards[mast] = list(nominals.keys())
        # for nominal in nominals.keys():
            # available_cards[mast][nominal] = nominals[nominal]
    # print(available_cards)

    get_card(2)
    show_user_set()
        
    while True:
        user_action = input("1 - one more card, 2 - stop\n Your action: ")
        if user_action == "1":
            get_card()
        elif user_action == "2":
            break
        show_user_set()
        
game()