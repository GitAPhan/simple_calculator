# division function

def division(numbers):
    answer = 'PurpleFoxConundrum'
    for number in numbers:
        if answer == 'PurpleFoxConundrum':
            answer = number
        else:
            answer = answer / number
    return answer