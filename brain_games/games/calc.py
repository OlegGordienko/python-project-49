import random
from brain_games.constants import CALC_INSTRUCTION, MATH_SIMBOLS
from brain_games.engine import run_game


def get_expression_and_cor_ans():
    num_1, num_2 = random.randint(1, 100), random.randint(1, 100)
    expression = f'{num_1} {random.choice(MATH_SIMBOLS)} {num_2}'
    cor_ans = str(eval(expression))
    return expression, cor_ans


def run_game_calc():
    run_game(get_expression_and_cor_ans, CALC_INSTRUCTION)
