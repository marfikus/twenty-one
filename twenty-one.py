
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

def get_card(player_set, n=1):
    for i in range(n):
        # suit = random.choice(suits)
        suit = random.choice(list(available_cards.keys()))
        nominal = random.choice(available_cards[suit])
        card = {
            "suit": suit,
            "nominal": nominal
        }
        player_set.append(card)
        
        available_cards[suit].remove(nominal)
        
        if len(available_cards[suit]) == 0:
            del available_cards[suit]

def show_set(player_set):
    print("==============")
    for card in player_set:
        print("{} of {}".format(card["nominal"], card["suit"]))
    print("==============")
        
def calc_scores(player_set):
    scores = 0
    for card in player_set:
        scores += nominals[card["nominal"]]
    return scores

user_set = []
comp_set = []

def game():
    # nominals_list = list(nominals.keys())
    for suit in suits:
        # available_cards[suit] = {}
        available_cards[suit] = list(nominals.keys())
        # for nominal in nominals.keys():
            # available_cards[suit][nominal] = nominals[nominal]
    # print(available_cards)

    game_over = False
    is_user_step = True
    user_stopped_game = False

    get_card(user_set, 2)
    show_set(user_set)
    print("Your scores:", calc_scores(user_set), "\n")

    get_card(comp_set, 2)
        
    while not game_over:
        if is_user_step:
            if user_stopped_game:
                is_user_step = False
                continue
            user_action = input("1 - get one more card, 2 - stop\n Your action: ")
            if user_action == "1":
                get_card(user_set)
            elif user_action == "2":
                # break
                user_stopped_game = True
            is_user_step = False
            show_set(user_set)
            print("Your scores:", calc_scores(user_set), "\n")
        else:
            if calc_scores(comp_set) >= 20:
                if user_stopped_game:
                    game_over = True
                    print("detect_winner")
                    # detect_winner(user_set, comp_set)
                # else:
                #     is_user_step = True
            else:
                get_card(comp_set)
            is_user_step = True

        
game()
