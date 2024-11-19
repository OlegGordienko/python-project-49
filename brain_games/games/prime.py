import math
from brain_games.constants import PRIME_INSTRUCTION
from brain_games.engine import run_game
from brain_games.get_num import get_random_num


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def get_num_and_cor_ans():
    num = get_random_num()
    cor_ans = 'yes' if is_prime(num) else 'no'
    return str(num), cor_ans


def run_game_prime():
    run_game(get_num_and_cor_ans, PRIME_INSTRUCTION)
