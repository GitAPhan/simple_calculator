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
print('5: Multiple numbers operation')
print('* if option 5 is selected select from choices 1-4 afterwards')

# user input
try:
    # function selection 
    function_selection = input('Please enter your selection: ')
    first_number = input('Please enter your first number: ')
    second_number = input('Please enter your second number: ')
    # value verification
    function_selection = int(function_selection)
    first_number = float(first_number)
    second_number = float(second_number)
except ValueError:
    print('Please enter valid value')

except Exception as e:
    print(e)

try:
    if function_selection == 1:
        answer = a.addition(first_number, second_number)
    elif function_selection == 2:
        answer = s.subtraction(first_number, second_number)
    elif function_selection == 3:
        answer = m.multiplication(first_number, second_number)
    elif function_selection == 4:
        answer = d.division(first_number, second_number)
except TypeError:
    print('Please enter valid number to be calculated')
except ZeroDivisionError:
    print("You can't divide by zero")
except Exception as e:
    print(e)

try:
    print('Your result: ', answer)
except NameError:
    print('We could not calculate your results, please enter valid numbers')
except Exception as e:
    print(e)
