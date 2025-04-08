import random as rd

def creat_pwd(n_letter, n_number, n_cs):
    number = [n_letter, n_number, n_cs]
    cara = ["abcdefgijklmnopqrstuvwxyz","0123456789","*-/+%$#_"]
    index = 0
    c = []
    for i in cara:
        for n in range(number[index]):
            c.append(rd.choice(list(i)))
        index += 1
    rd.shuffle(c)
    return "".join(c)


print(creat_pwd(5,2,3))
        



