from brain_games.utils import get_random_num
from brain_games.engine import run_game
from brain_games.constants import EVEN_INSTRUCTION


def is_even(num):
    return num % 2 == 0


def get_num_and_cor_ans():
    num = get_random_num()
    cor_ans = 'yes' if is_even(num) else 'no'
    return str(num), cor_ans


def run_even_game():
    run_game(get_num_and_cor_ans, EVEN_INSTRUCTION)
