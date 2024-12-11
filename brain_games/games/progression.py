import random

from brain_games.constants import MAX_LEN_PROGRESSION as max
from brain_games.constants import MIN_LEN_PROGRESSION as min
from brain_games.constants import PROGRESSION_INSTRUCTION
from brain_games.engine import run_game
from brain_games.utils import get_random_num


def get_progression_and_mis_num():
    start = get_random_num()
    dif = get_random_num()
    len_progression = random.randint(min, max)
    missed_num_ind = random.randint(0, len_progression - 1)
    progression_str = ' '.join([
        '..' if i == missed_num_ind else str(start + dif * i)
        for i in range(len_progression)
    ])
    mis_num = start + dif * missed_num_ind
    return progression_str, str(mis_num)


def run_game_progression():
    run_game(get_progression_and_mis_num, PROGRESSION_INSTRUCTION)
