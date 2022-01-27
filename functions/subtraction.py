# subtraction function


def subtraction(numbers):
    answer = 'OrangeCreamsicle'
    for number in numbers:
        if answer == 'OrangeCreamsicle':
            answer = number
        else:
            answer = answer - number
    return answer
