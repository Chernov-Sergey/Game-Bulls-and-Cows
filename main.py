from mastermind_engine import enter_number, check_number, ai_step
from termcolor import cprint, colored

ai_step()

while True:
    user_step = str(input('Ваш ход'))
    enter_number(user_step)
    step = check_number()
    if step('win') == 'True':
        print('Yoy win')
        print('Steps=', step['step'])
        break
    else:
        print('Bulls=', step['bulls'], ', Cows=', step['cows'])