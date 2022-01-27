from tokenize import Name
import functions.addition as a
import functions.subtraction as s
import functions.multiplication as m
import functions.division as d

# welcome message
print('Welcome to the simple calculator, please select from the following options:')
print('1: Addition')
print('2: Subtraction')
print('3: Multiplication')
print('4: Division')

# test: define Python user-defined exceptions
class CustomError(Exception):
    pass


class ValueTooSmallError(CustomError):
    pass


class ValueTooLargeError(CustomError):
    pass

# user function selection
while True: # this will keep looping if there is an error
    try:
        # function selection 
        function_selection = input('Please enter your selection: ')
        # value validation
        if int(function_selection) <= 4 and int(function_selection) >= 1:
            function_selection = int(function_selection)
        # played around with custom errors             
        elif int(function_selection) > 4:
            raise ValueTooLargeError
        elif int(function_selection) < 1:
            raise ValueTooSmallError
        break
    except ValueTooLargeError:
        print("You've entered a value to large")
    except ValueError:
        print('Please enter a valid selection (1-4)')
    except Exception as e:
        print(e)

# user selects how many numbers are in the calculation    
try:
    number_of_numbers = input('How many numbers would you like to calculate (default is 2)? ')
    number_of_numbers = int(number_of_numbers)
    # doesn't make sense to do calculations if there are less than 2 numbers
    if int(number_of_numbers) < 2:
        raise ValueTooSmallError
    # message to inform user of selection
    print('You have selected', number_of_numbers, 'numbers')
except ValueError:
    # if the user enters an invalid value, the default value will be 2
    print("You've entered an invalid value")
    print('default of 2 numbers has been selected')
    number_of_numbers = 2
except ValueTooSmallError:
    print("You've entered a value too small!")
    print('default of 2 numbers has been selected')
    number_of_numbers = 2
except Exception as e:
    print(e)

while True:
    # user input number values
    try:
        numbers = []
        # loop to prompt 
        for i in range(number_of_numbers):
            # conditional to display ordinal number
            if str(i+1).endswith('1'):
                ordinal = str(i+1) + 'st'
            elif str(i+1).endswith('2'):
                ordinal = str(i+1) + 'nd'
            elif str(i+1).endswith('3'):
                ordinal = str(i+1) + 'rd'
            else:
                ordinal = str(i+1) + 'th'
            # prompt message
            message = 'please enter your ' + ordinal + ' number: '
            # user input
            number = input(message)
            # validate number
            number = float(number)
            # add number to numbers array
            numbers.append(number)
        break
    except Exception as e:
        print(e)
        print('lets try entering your numbers again')

# calculator function execution 
try:
    if function_selection == 1:
        answer = a.addition(numbers)
    elif function_selection == 2:
        answer = s.subtraction(numbers)
    elif function_selection == 3:
        answer = m.multiplication(numbers)
    elif function_selection == 4:
        answer = d.division(numbers)
except TypeError:
    print('Please enter valid number to be calculated')
except ZeroDivisionError:
    print("You can't divide by zero")
except Exception as e:
    print(e)

# answer from calculation function to be printed
try:
    print('Your result: ', answer)
except NameError:
    print('We could not calculate your results, please enter valid numbers')
except Exception as e:
    print(e)
