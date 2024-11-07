import random
from brain_games.constants import (PROGRESSION_INSTRUCTION,
                                   MIN_LEN_PROGRESSION as min,
                                   MAX_LEN_PROGRESSION as max)
from brain_games.engine import run_game


def get_progression_and_mis_num():
    progression = []
    dif = random.randint(1, 10)
    start = random.randint(1, 20)
    for i in range(random.randint(min, max)):
        element = start + dif
        start = element
        progression.append(str(element))
    mis_num = random.choice(progression)
    index_mis_num = progression.index(mis_num)
    print(index_mis_num)
    progression[index_mis_num] = '..'
    progression_str = ' '.join(progression)
    return progression_str, str(mis_num)


def run_game_progression():
    run_game(get_progression_and_mis_num, PROGRESSION_INSTRUCTION)
