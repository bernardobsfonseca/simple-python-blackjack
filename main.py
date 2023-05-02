from random import randint

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
resp = 'y'
num_cards = len(cards)


def first_drawn():
    drawn = [cards[randint(0, num_cards - 1)], cards[randint(0, num_cards - 1)]]
    return drawn


def drawn_one(deck):
    draw = cards[randint(0, 12)]

    if draw == 11:
        if calculate_sum(deck) > 10:
            draw = 1

    deck.append(draw)


def calculate_sum(deck):
    return sum(deck)


while resp == 'y':
    print('<<<<<<<<<< Blackjack >>>>>>>>>>')

    player = first_drawn()
    opponent = first_drawn()

    print(f'player: {player[0]}, {player[1]}')
    print(f'opponent: {opponent[0]}')

    question_draw = input("Hit (h) or Stand (s): ")

    if question_draw == 'h':
        drawn_one(player)

    if calculate_sum(opponent) <= 11:
        drawn_one(opponent)

    print(f'player: {player}')
    print(f'opponent: {opponent}')

    sum_player = calculate_sum(player)
    sum_opponent = calculate_sum(opponent)

    if sum_player == 21 or sum_opponent > 21 or (21 > sum_player > sum_opponent):
        print('You win')
    elif sum_opponent == 21 or sum_player > 21 or (21 > sum_opponent > sum_player):
        print('You lose')
    else:
        print('Draw')

    resp = input('Continue (y/n): ')
