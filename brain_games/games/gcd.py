import math

from brain_games.constants import GCD_INSTRUCTION
from brain_games.engine import run_game
from brain_games.utils import get_random_num


def get_nums_gcd():
    first_num, second_num = get_random_num(), get_random_num()
    gcd = math.gcd(first_num, second_num)
    nums = f'{first_num} {second_num}'
    return nums, str(gcd)


def run_game_gcd():
    run_game(get_nums_gcd, GCD_INSTRUCTION)
