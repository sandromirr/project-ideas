import random

def getOperation(number):
    if number == 0:
        return '+'
    elif number == 1:
        return '-'
    elif number == 2:
        return '*'
    else:
        return '/'


def getAnswer(number1, operation, number2):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    else:
        return number1 // number2


try:
    n = int(input())

    f = open("questions.txt", "w")
    s = f"{n}\n"

    for count in range(0, n):
        while True:
            number1 = random.randint(0, 100)
            number2 = random.randint(1, 100)
            operation = getOperation(random.randint(0, 100) % 4)
            answer = getAnswer(number1, operation, number2)
            l = [answer]

            for i in range(0, 3):
                l.append(random.randint(0, 100))
            random.shuffle(l)
            #print(number1,operation,number2)
            if operation == '+' or operation == '-' or operation == '*':
                s += f"{number1}{operation}{number2}=;{l[0]};{l[1]};{l[2]};{l[3]};{answer}\n"
                break

    f.write(s)
    print(s)
except NameError:
    print(NameError)