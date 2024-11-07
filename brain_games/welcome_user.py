import prompt


def welcome_user(instruction):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{instruction}')
    return name
