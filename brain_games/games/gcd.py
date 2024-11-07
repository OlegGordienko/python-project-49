import random
import math
from brain_games.constants import GCD_INSTRUCTION
from brain_games.engine import run_game


def get_nums_gcd():
    num_1, num_2 = random.randint(1, 100), random.randint(1, 100)
    gcd = math.gcd(num_1, num_2)
    nums = f'{num_1} {num_2}'
    return nums, str(gcd)


def run_game_gcd():
    run_game(get_nums_gcd, GCD_INSTRUCTION)
