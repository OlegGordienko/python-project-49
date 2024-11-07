import prompt
from brain_games.constants import AMOUNT_OF_ROUNDS
from brain_games.welcome_user import welcome_user


def run_game(get_question_and_answer, instruction):
    name = welcome_user(instruction)
    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string('Question: ' + question + '\n'
                                    'Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\"{user_answer}\" is wrong answer ;(. '
                  f'Correct answer was \"{correct_answer}\".\n'
                  f'Let\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')
