import random
from brain_games.get_num import get_random_num
from brain_games.constants import CALC_INSTRUCTION
from brain_games.engine import run_game


def get_math_symbol_ans(first_num, second_num):
    return random.choice([
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num)
    ])

def get_expression_and_cor_ans():
    first_num, second_num = get_random_num(), get_random_num()
    symbol, cor_ans = get_math_symbol_ans(first_num, second_num)
    expression = f'{first_num} {symbol} {second_num}'
    return expression, str(cor_ans)


def run_game_calc():
    run_game(get_expression_and_cor_ans, CALC_INSTRUCTION)
