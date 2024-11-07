import random
from brain_games.constants import PRIME_INSTRUCTION
from brain_games.engine import run_game


def is_prime(num):
    i = 2
    while i != num - 1:
        if num % i == 0:
            return 'no'
        else:
            i += 1
    return 'yes'


def get_num_and_is_prime():
    num = random.randint(1, 1000)
    return str(num), is_prime(num)


def run_game_prime():
    run_game(get_num_and_is_prime, PRIME_INSTRUCTION)
