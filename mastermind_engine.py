from random import randint

global step_count
step_count = 0



def ai_step():
    global res
    res = []

    while True:
        random_num = randint(1000, 9999)
        res = list(str(random_num))
        res_set = set(res)
        if len(res_set) == len(res):
            break



def enter_number(user_number):
    global user_num
    user_num = user_number
    user_num = list(str(user_num))


def check_number():
    global step_count
    step_count = step_count + 1
    bulls, cows = 0, 0
    for i in range(len(user_num)):
        for j in range(len(res)):
            if user_num[i] == res[j]:
                bulls += 1
    user_num_set = set(user_num)
    res_set = set(res)
    total_set = user_num_set.union(res_set)
    cows = 8 - len(total_set) - bulls
    answer = {'bulls': bulls, 'cows': cows, 'step': step_count, 'win': 'False'}
    if bulls == 4:
        answer['win'] = 'True'
    return answer

# def is_gameover():
#     return




