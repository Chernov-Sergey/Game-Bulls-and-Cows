from random import randint

def ai_step():
    global res
    res = []



    while True:
        result = randint(1000, 9999)
        res = len(str(result))
        for i in range(0, len(res + 1)):
            for j in range(1, len(res +1)):
                if res[i] == res[j]:
                    break




def enter_number(user_number):
    pass


def check_number():
    pass


