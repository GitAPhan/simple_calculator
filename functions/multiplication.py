# multiplication function

def multiplication(numbers):
    answer = 'PurpleFoxConundrum'
    for number in numbers:
        if answer == 'PurpleFoxConundrum':
            answer = number
        else:
            answer = answer * number
    return answer