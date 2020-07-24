
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

def detect_winner(user_set, comp_set):
    user_scores = calc_scores(user_set)
    comp_scores = calc_scores(comp_set)

    if user_scores == comp_scores:
        print("Tie")
        return

    if user_scores > 21 and comp_scores > 21:
        print("No winners")
        return

    if user_scores <= 21 and comp_scores > 21:
        print("You win")
        return

    if user_scores > 21 and comp_scores <= 21:
        print("You lose")
        return

    if (21 - user_scores) < (21 - comp_scores):
        print("You win")
        return        
    
    if (21 - user_scores) > (21 - comp_scores):
        print("You lose")
        return

def calc_success_probability(scores):
    """
    В зависимости от набранных очков, 
    подсказывает компьютеру: стоит ли брать ещё карту.
    Примитивная имитация принятия решения.
    """
    # определяем вероятность того, что будет взята ещё 1 карта
    if scores <= 12:
        # 100%
        probability = [1, 1, 1, 1]
    elif 12 < scores <= 14:
        # 75%
        probability = [1, 1, 1, 0]
    elif 14 < scores <= 17:
        # 50%
        probability = [1, 1, 0, 0]
    elif 17 < scores <= 19:
        # 25%
        probability = [1, 0, 0, 0]

    # добавим немного случайности
    ch = random.choice(probability)
    if ch:
        return True
    else:
        return False

# наборы карт пользователя и компьютера:
user_set = []
comp_set = []

def game():
    # формируем колоду карт:
    # nominals_list = list(nominals.keys())
    for suit in suits:
        # available_cards[suit] = {}
        available_cards[suit] = list(nominals.keys())
        # for nominal in nominals.keys():
            # available_cards[suit][nominal] = nominals[nominal]
    # print(available_cards)

    # флаг окончания игры:
    game_over = False
    # флаг очереди пользователя:
    is_user_step = True
    # флаг остановки набора карт пользователем:
    user_stopped_game = False

    # раздаём первые карты:
    get_card(user_set, 2)
    print("Your set:")
    show_set(user_set)
    print("Your scores:", calc_scores(user_set), "\n")

    get_card(comp_set, 2)
        
    while not game_over:
        if is_user_step:
            # ход пользователя.
            # если он уже завершил набор, то пропускаем:
            if user_stopped_game:
                is_user_step = False
                continue
            # иначе запрашиваем действие, выполняем..
            user_action = input("1 - get one more card, 2 - stop\n Your action: ")
            if user_action == "1":
                get_card(user_set)
            elif user_action == "2":
                user_stopped_game = True
            is_user_step = False
            print("Your set:")
            show_set(user_set)
            print("Your scores:", calc_scores(user_set), "\n")
        else:
            # ход компьютера.
            comp_scores = calc_scores(comp_set)
            if comp_scores >= 20:
                if user_stopped_game:
                    game_over = True
            else:
                # тут комп прикидывает, брать ли ещё карту:
                if calc_success_probability(comp_scores):
                    get_card(comp_set)
                else:
                    # print(f"comp is passed. comp_scores: {comp_scores}")
                    if user_stopped_game:
                        game_over = True
            is_user_step = True

    print("Comp set:")
    show_set(comp_set)
    print("Comp scores:", comp_scores, "\n")
    detect_winner(user_set, comp_set)
        
game()
