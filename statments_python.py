from random import randint
from random import shuffle
if True:
    print('its true')

if 3 > 2:
    print('its true')

hungry = False
if hungry:
    print('food')
else:
    print('no food')

loc = 'Store'
if loc == 'Store':
    print('get bagels')
elif loc == 'Farmhouse':
    print('another true conditional')
else:
    print('this will show if the boolean is false')

name = 'kaleb'
if name == 'willy':
    print('willy is the favorite kid')
elif name == 'lincoln':
    print('lincoln is the favorite kid')
elif name == 'isis':
    print('isis is the favorite kid')
elif name == 'atlas':
    print('atlas is the favorite kid')
elif name == 'keera':
    print('keera is the favorite kid')
else:
    print(" hahahaha its not kaleb loser")

restraunt = 'Atilanos'
if restraunt == 'taco bell':
    print('lets get quesadillas')
elif restraunt == 'Atilanos':
    print('lets get burritos bitches')
elif restraunt == 'subway':
    print('lets get hot steamers')
else:
    print('i dont want to eat there')

# for loops
# iterable means you can 'iterate' over the object

my_iterable = [1, 2, 3]
for item_name in my_iterable:
    print(item_name)

my_list = ['apple', 'pear', 'grape', 'pineapple']
for fruit in my_list:
    print('isis')

my_second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in my_second_list:
    # check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'odd number:{num}')
# if num % 2 == 0: means divided by pronounced as mod
list_sum = 0
for num in my_second_list:
    list_sum = list_sum + num
print(list_sum)

# for loops w strings
my_string = 'hello world'
for letter in my_string:
    print(letter)

for jelly in 'hello world':
    print(jelly)

for _ in 'my name':
    print('isis')

# tuples and for loops
tup = (1, 2, 3)
for item in tup:
    print(item)

apple_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
len(my_list)
for item in apple_list:
    print(item)

for (a, b) in apple_list:
    print(b)
    print(a)
# ^ this is called tuple unpacking in which you take the items in the tuple and iterate through each tuple

other_list = [(1, 2, 3), (5, 6, 7,), (11, 23, 37)]
for a, b, c in other_list:
    print(c)
    print(a)
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}
for key, value in d.items():
    print(value)
# d.items returns something in the (a,b) format this is called tuple unpacking otherwise it only iterates the keys

# while loops
# while loops will continue to execute a block of code WHILE the code is true

# while some_boolean_condition:
#   # do something
# else:
#   # do something different

x = 50
while x < 5:
    print(f'the current value of x is {x}')
    x = x + 1
else:
    print("x is not less than 5")

# break, contine, pass
# break: break out of the current enclosing loop
# continue: goes to the top of the closest enclosing loop
# pass: does nothing at all
m = [1, 2, 3]
for item in m:
    pass
print('pass was a placeholder')

string_pp = 'isis'
for letter in string_pp:
    if letter == 's':
        continue
    print(letter)
# this continue made it so it didnt print s
string_pp = 'isis'
for letter in string_pp:
    if letter == 's':
        break
    print(letter)
    # the break stops the loop at the letter before the s

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

kaleb_list = [20, 21, 22]
for num in range(30):
    print(num)
for bb in range(5, 20):
    print(bb)
list(range(0, 11, 2))

name = 'isis avry womack'
for word in name.split(' '):
    print(word)

name_list = [word.upper() for word in name.split(' ')]
print(name_list)

# useful operators
idk_list = [1, 2, 3, ]
for num in range(10):
    print(num)
for banana in range(3, 10):
    print(banana)
for pear in range(0, 10, 2):
    print(pear)
# (first number, number up to, step size)
list(range(6, 30, 2))
# ^ it will return the range like range(0,11,2)
# but is you cast it a list like above it will give you the range you typed in a list format

isis_count = 0
for letter in 'abcde':
    print('at this letter {} the index is {}' .format(isis_count, letter))
    isis_count += 1
# enumerate function to replicate this and to give # of times have iterate through for loop or what index you're at
kaleb_count = 0
word = 'abcde'
for item in enumerate(word):
    print(item)
# ^ returns tuples; it does the index count for you automatically in the form of tuples. as we know we have tuple unpacking in the form of for loosp so could say:
word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
# \n means new line
# the enumerate function takes in the iterable function and returns back an index counter and the object itself or the element at that particular iteration

dog_list1 = [5, 6, 7, ]
cat_list = ['a', 'b', 'c']
fishlist = [100, 200, 300]

for item in zip(dog_list1, cat_list, fishlist):
    print(item)
    # zip is only able to go as far as to zip togetehr the list which is the shortest
list(zip(dog_list1, cat_list, fishlist))
# ^ will zip them together into a list

# can use in operator to see if an object is in a list: it will return a boolean
'x' in [1, 2, 3]
'x' in ['x', 'y', 'z']

'mykey' in {'mykey': 345}
d = {'mykey': 345}
345 in d.values()

alist = [10, 20, 30, 40, 100]
min(alist)
max(alist)
# ^ these will report back the min and ,ax values of that list

# random library is built into python, you can download other ones from the internet: importing a library
shuffle(alist)
print(alist)
# ^shuffles list each time differently

randint(0, 100)
mynum = randint(0, 100)
print(mynum)
result = input('what is your name?:')
print(result)

# List comprehension
thisstring = 'shut up'
thislist = []
for letter in thislist:
    thislist.append(letter)
    print(thislist)

blue = [green for green in 'fuck off']
print(blue)

bluestring = 'blah'
pink = [purple for purple in bluestring]
print(pink)

purple = [qwewe for qwewe in 'periodt']
print(purple)

orange = [num**2 for num in range(0, 20)]
print(orange)
# print the square for each number in range^

yellow = [gray for gray in range(10, 20) if gray % 2 == 0]
print(yellow)
# x%`2 means only numbers that are equal to 2

celcius = [0, 10, 20, 30, 34.5]
farenheight = [((9/5)*temp + 32) for temp in celcius]
print(farenheight)
# (9/5)*temp + 32) is just the formulat for the conversion
farenheight = []
for temp in celcius:
    farenheight.append(((9/5)*temp + 32))
    print(farenheight)

results = [p if p % 2 == 0 else 'odd' for p in range(0, 11)]
print(results)

# nested loop:
footlist = []
for x in [8, 9, 6]:
    for y in [900, 800, 600]:
        footlist.append(x*y)
print(footlist)

for num in range(0, 101, 20):
    print(num)

ruby = 'this is a string and i want you to pull out all words that start with an "s" '
for word in ruby.split():
    if word[0] == 's' or word[0] == 'S':
        print(word)

chicken = 'isis avry womack kaleb james Womack keera delaine womack lincoln alexander womack William carter womack atlas kane womack'
for blueberry in chicken.split():
    if blueberry[0] == 'w' or blueberry[0] == 'W':
        print(blueberry)

bitches = 'two'
if bitches == 'two':
    print('chelsea is a cum guzzling bitch')
elif bitches == 'four':
    print('nick is banging my mom and its disgusting')
else:
    print('fuck the momacks, womacks for life bitch')

alot_string = 'apples And Adam and Audrey and Banana And bath and Bed Beaver bg bitch'


def find_a(alot_string):
    counter = 0
    for letter in alot_string:
        if letter == 'a' or letter == 'A':
            counter += 1
    return(counter)


# set name equal to string value isis
name = 'isis'
# set counter to 0 int
counter = 0
# iterate through name string and for every letter add 1 to the counter and save the value
for letter in name:
    counter += 1
counter

len(name)
