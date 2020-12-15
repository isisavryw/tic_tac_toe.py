from random import shuffle
my_list = [1, 2, 3]
my_list.append(8)
print(my_list)
my_list.pop()
print(my_list)
my_list.insert(200, 'hoe')
print(my_list)

# Functions
# def name_of_function(name):
# '''
# Docstring explains function
# ''''
# print("Hello")

# >>>name_of_function(name)
# >>> Hello


def add_function(num1, num2):
    return num1 + num2
    print(result=add_function(3, 55))


def say_hello():
    print("hello")
    print("how")
    print("are")
    print("you?")


print(say_hello())


def literals_idk(name='Default'):
    print(f'Hello {name}')


literals_idk('isis avry')


def add_numbers(num1, num2):
    return num1+num2

# Difference between calling print and return function is return actually processes it and saves it as a variable. So what you get from the retuen function, you can assign to a varible like below.


result = add_numbers(10, 20)


def print_result(a, b):
    print(a+b)


def return_result(a, b):
    return a+b


print_result(10, 20)
varibale = return_result(20, 20)

# % mod operator returns remainder from divison
20 % 2 == 0
# True^ even number
21 % 2 == 0
# False^ odd number


def even_check(number):
    result = number % 2 == 0
    return result
# or


def even_check(number):
    return number % 2 == 0


even_check(20)
even_check(21)

# RETURN TRUE IS ANY NUMBER IS EVEN INSIDE OF A LIST


def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass

          # ^ putting return False is wrong because not every return statment should have the same level of indentation, if you ran that return false statment, you would always get false if there were one odd # focus on the logic of what happening!
check_even_list([1, 3, 5, 4])
check_even_list([2, 1, 1, 1, 1, 14, 6, 3])
check_even_list([1, 1, 1, 2, 4, ])


def second_check_even_list(number_list):

    # return all even numbers in a list

    # placeholder variables
    even_numbers = []
    for number in number_list:
        if number % 2 == 0:
            even_numbers.append(number)
    else:
        pass
    return even_numbers


    #  so it'll go through the list, and if its even, it'll append it to the list. the return is in line with the four loop so it will iterate through the entire list before it returns to you the even numbers list
second_check_even_list([1, 2, 4, 5, 6, ])

# unpacking tuples
stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]
for item in stock_prices:
    print(item)
for ticker, price in stock_prices:
    print(price+(0.1*price))


work_hours = [('Abby', 100), ('Greg', 400), ('Cassie', 800)]


def employee_check(work_hours):

    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)
    resuly = employee_check(work_hours)
    name, hours = employee_check(work_hours)
    name
    hours


example = [1, 2, 3, 4, 5, 6, 7]
result = shuffle(example)
result


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


result = shuffle_list(example)
result
mylist = ['', 'o', '']
shuffle_list(mylist)


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("pick a number: 0,1 or 2")
    return int(guess)


    # input always returns a string
player_guess()
myindex = player_guess()


def check_guess(mylist, guess):
    if mylist[guess] == 'o':
        print("Correct!")
    else:
        print('wrong guess!')
        print(mylist)


# inital list
mylist = ['', 'o', '']
# shuffle list
mixedup_list = shuffle_list(mylist)
# user guess
guess = player_guess()
# check guess
check_guess(mixedup_list, guess)

# find the shortest length of a string in an array of strings:


def find_short(s):
    words = s.split(' ')
    words.sort(key=len)
    return len(words[0])
