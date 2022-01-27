# addition function

def addition(numbers):
    answer = 'BananaPancake'
    for number in numbers:
        if answer == 'BananaPancake':
            answer = number
        else:
            answer = answer + number
    return answer