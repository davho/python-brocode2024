# # --- Python Full Course for free 🐍 (2024) - https://www.youtube.com/watch?v=ix9cRaBkVe0 ---

# # Make sure Python, Python extension for VS Code and package installer for Python, aka `pip`, are installed (note, pip/pip3 was not installed at the time of archiving this course):
# # `python3 --version`
# # `pip3 --version`

# # To run the script in Terminal do `python3 brocode.py`

# # To study any lesson in this course simple comment out the lesson and run the script

# # In the comments, the lesson concepts are Capitalized and the names of Variables, Functions, Methods, Classes, Subclasses, Packages, Modules and Submodules are flanked with backticks, e.g. `variable_name`, `function_name`, as well as various Operators, e.g. `|`, `or`, `and`, and code snippets and structural demonstrations are also flanked with the `code` Markdown syntax, e.g. do `python3 <file-name>.py`, `age = int(input('How old are you?: '))`, `[start:end:step]`, `[ expression for element in iterable if condition ]`




# # Intro - 00:00:00

# # From Terminal run Python files with `python3 <file-name>.py`

# # `print` is the Python equivalent of `console.log` in JavaScript
# print('I')
# print('like')
# print('pizza')




# # Variables - 00:05:49

# # Variable = A container for a value. It behaves as if it were the value it contains. It isn't declared with `var`, `let` or `const`, as would be the case in JavaScript. The term "primitive data types" isn't used in Python either but it generally refers to the built-in data types that represent single values: Strings, Integers, Floats and Booleans.

# # Strings (regular Strings)
# first_name = 'Bro'
# food = 'pizza'
# email = '123@abc.io'
# ageAsStr = '25'
# emptyStr = ''

# # Integers
# ageAsInt = 25
# quantity = 3
# num_of_students = 30 # Underscores separating words that comprise Variable names is the naming convention in Python as opposed to camelCase in JavaScript

# # Float
# price = 10.99
# gpa = 3.2
# distance = 5.5

# # Boolean
# is_student = True # `True` and `False` must have their T and F capitalized
# is_for_sale = False
# is_online = True

# print(first_name)
# print(food)
# print(email)

# # F-Strings (Formatted Strings) = The Python equivalent of template Strings in JavaScript. Variables in the Formatted Strings don't need the dollar sign to signify them. The quotes can be single or double but not backtick.

# print(f'Hello {first_name}')
# print(f'You like {food}')
# print(f'Your email is {email}')
# print(f'You are {ageAsStr} years old. {ageAsInt} is an anxious time.') # Integers parse fine within Strings
# print(f'Your class has {num_of_students} students')
# print(f'The price is ${10.99}') # Dollar sign appears in the text and is not used to signify use of the Variable in the F-String
# print(f'Your GPA is {gpa}')
# print(f'You ran {distance}km')

# if (is_student):
#     print('You are a student')
# else:
#     print('You are not a student')

# if (is_for_sale):
#     print('This item is for sale')
# else:
#     print('This item is not for sale')

# if (is_online):
#     print('You are online')
# else:
#     print('You are not online')




# # Type Casting - 00:16:05

# # Type Casting = The process of converting a Variable from one data type to another.
# # `str`, `int`, `float`, `bool` are Functions each which eponymously convert the Arguments passed to them.

# ageAsInt = 25
# ageAsStr = '25'
# price = 10.99
# is_online = True
# emptyStr = ''

# print(type(ageAsInt))
# print(type(ageAsStr))
# print(type(price))
# print(type(is_online))

# print(ageAsInt == ageAsStr) # prints `False`
# print(ageAsInt == int(ageAsStr)) # prints `True`

# print(bool(ageAsStr)) # All actual Strings are `True`...
# print(bool(emptyStr)) # ...but empty Strings are `False`




# # User Input - 00:21:15

# # `input` = A Function that takes a String to prompt the user to enter data and returns the entered data as a String.

# name = input('What is your name?: ')
# age = input('How old are you?: ')
# age_next_year = int(age) + 1 # To do arithmetic with the user input, which is a String, we must first Type Cast it to an Integer or to a Float. And since Integers can be passed into the String we could even have converted the age immediately to an Integer by doing `age = int(input('How old are you?: '))`
# print(f'Hello {name}, you are {age} years old. Next year you will be {age_next_year}.')




# # Rectangle Area Calc Program - 00:26:14

# length = float(input('What is the length?: '))
# height = float(input('What is the height?: '))
# area = length * height

# print(f'The area of the rectangle is {area}')




# # Shopping Cart Program - 00:29:18

# item = input('What item would you like to buy?: ')
# price = float(input('What is the price?: '))
# quantity = int(input('How many would you like?: '))
# total = price * quantity

# print(f'You are buying {item} at {price} per {item} and the total price is {total}')




# # Madlibs Program - 00:32:46

# adjective1 = input('Enter an adjective: ')
# noun1 = input('Enter a noun: ')
# adjective2 = input('Enter another adjective: ')
# verb1 = input('Enter a verb ending with "ing": ')
# adjective3 = input('Enter yet another adjective: ')

# print(f'Today I went to a {adjective1} zoo.')
# print(f'In an exhibit, i saw a {noun1}')
# print(f'{noun1} was {adjective2} and {verb1}')
# print(f'I was {adjective3}')




# # Arithmetic & Math - 00:37:55

# friends = 5
# friends = friends + 1
# friends += 1 # This is simply the Augmented Assignment Operator for addition, same as in JavaScript
# friends -= 1 # This is simply the Augmented Assignment Operator for subtraction, same as in JavaScript
# friends *= 3 # This is simply the Augmented Assignment Operator for multiplication, same as in JavaScript
# friends /= 3 # This is simply the Augmented Assignment Operator for division, same as in JavaScript
# friends **= 3 # This is simply the Augmented Assignment Operator for power, same as in JavaScript
# friends %= 7 # This is simply the Augmented Assignment Operator for modulus, same as in JavaScript

# print(friends)

# a = 3.15
# b = -4
# c = 5

# round_example = round(a) # Same as `Math.round` in JavaScript
# absolute_value_example = abs(b) # Same as `Math.abs` in JavaScript
# power_example = pow(a, c) # Same as `Math.pow` in JavaScript
# max_example = max(a, b, c) # Same as `Math.max` in JavaScript
# min_example = min(a, b, c) # Same as `Math.min` in JavaScript

# print(round_example)
# print(absolute_value_example)
# print(power_example)
# print(max_example)
# print(min_example)


# import math # The `math` Module in Python, which has constants like `pi` as well as other functionality, must be intentionally imported, unlike the `Math` Module in JavaScript

# pi_example = math.pi # Same as `Math.PI` in JavaScript
# e_example = math.e # Same as `Math.E` in JavaScript
# square_root_example = math.sqrt(c) # Same as `Math.sqrt` in JavaScript
# ceiling_example = math.ceil(pi_example) # Same as `Math.ceil` in JavaScript
# floor_example = math.floor(pi_example) # Same as `Math.floor` in JavaScript

# print(pi_example)
# print(e_example)
# print(square_root_example)
# print(ceiling_example)
# print(floor_example)

# radius = float(input('Enter the radius of your circle: '))
# circumference = 2 * math.pi * radius
# circumference = round(circumference, 3) # Variables being modified after declaration act like JavaScript `var` or `let` in this respect, not `const`

# print(f'The circumference is: {circumference} cm')

# area = math.pi * pow(radius, 3)
# area = round(area, 3) # Variables being modified after declaration act like JavaScript `var` or `let` in this respect, not `const`

# print(f'The area is: {area} cm')


# side_a = float(input('Enter side A of right triangle to find hypotenuse: '))
# side_b = float(input('Enter side B of right triangle to find hypotenuse: '))
# side_c = round(math.sqrt(pow(side_a, 2) + pow(side_b, 2)), 3) # Each side to the power of 2, their results added, the square root of that result then rounded to 3 decimal points

# print(side_c)




# # `if` Statements - 00:51:46

# age = int(input('Enter your age: '))

# if age >= 18: # Indentation structure is imperative in Python Conditional Statements the way curly braces are imperative in JavaScript Conditional Statements
#     if age >= 100:
#         print('You are too old to sign up')
#     else:
#         print('You are now signed up')
# elif age < 0: # `elif` is obviously equivalent to `else if` in JavaScript (and C, C++, Java, and Ruby), and is a less common syntax than `else if` but still shared with bash (and the earlier Algol 68), so its likely that Guido van Rossum was partial to bash
#     print('You haven\'t been born yet')
# else:
#     print('You must be 18+ to sign up')


# response = input('Would you like food? (Y/N): ')

# if response == 'Y': # Double equals is used as the Comparison Operator because single equals is used exclusively as a Mathematical Operator. Unlike JavaScript, Python is strongly typed so does not perform implicit type coercion in comparisons, hence the `==` Operator in Python already behaves like JavaScript's `===` Operator. So unlike in JavaScript, there's no need for a separate `===` Operator in Python
#     print('Have some food')
# elif response == 'N':
#     print('No food for you')
# else:
#     print('Invalid input')


# name = input('Enter your name: ')

# if name == '':
#     print('You did not type in your name')
# else:
#     print(f'Hello {name}')


# for_sale = True

# if for_sale: # With `if` Statements you can write a Boolean as well as a condition with Comparison Operators
#     print('This item is for sale')
# else:
#     print('This item is not for sale')




# # Calculator Program - 01:00:06

# operator = input('Enter an operator (+ - * /): ')
# num1 = float(input('Enter the first number: '))
# num2 = float(input('Enter the second number: '))

# if operator == '+': # Note when writing Python and wanting to test in the middle of unfinished code you need to write `pass`, otherwise and unlike in JavaScript, an `if`, `elif` or `else` with empty content will crash. Placing `pass` instead of the empty block will prevent this
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '/':
#     result = num1 / num2
# else:
#     result = 'not invalid because you used an invalid operator'

# print(f'The answer is {result}')




# # Weight Converter Program - 01:05:59

# weight = float(input('Enter your weight: '))
# unit = input('Enter kilograms or pounds (K or L): ')

# if unit == 'K':
#     weight *= 2.205
#     unit = 'Ls'
# elif unit == 'L':
#     weight /= 2.205
#     unit = 'Ks'
# else:
#     weight = 'invalid'
#     unit = ''

# print(f'Your weight is {weight} {unit}')




# # Temperature Converter - 01:09:59

# unit = input('Is this temperature in Celsius or Fahrenheit? (C or F): ')
# temp = float(input('Enter the temperature: '))

# if unit == 'C':
#     temp = round((9 * temp)/5 + 32, 1)
#     unit = 'F°'
# elif unit == 'F':
#     temp = round((temp - 32) * 5/9, 1)
#     unit = 'C°'
# else:
#     temp = 'invalid.'
#     unit = 'Please enter a valid unit.'

# print(f'Your converted temperature is {temp} {unit}')




# # Logical Operators - 01:13:58

# # `or` = At least one condition must be `True`.
# # `and` = Both conditions must be `True`.
# # `not` = Inverts the condition (not `False`, not `True`).

# temp = 0
# is_raining = False
# is_sunny = False
# status = ''

# if temp >= 28 and is_sunny:
#     status = 'It is hot outside and it\'s sunny☀️'
# elif temp <= 0 and is_sunny:
#     status = 'It is cold outside but it\'s still sunny☀️'
# elif 28 > temp > 0 and is_sunny: # In JavaScript you'd have to deliberately specify that `28 > temp && temp > 0` but in Python you can express temp being between 28 and 0 without using Python's `and` Operator
#     status = 'It is warm outside and it\'s sunny☀️'
# elif temp >= 28 and not is_sunny:
#     status = 'It is hot outside and cloudy☁️'
# elif temp <= 0 and not is_sunny:
#     status = 'It is cold outside and cloudy☁️'
# elif 28 > temp > 0 and not is_sunny:
#     status = 'It is warm outside and cloudy☁️'

# print(status)




# # Conditional Expressions - 01:21:28

# # Conditional Expression = A one-line shortcut for the "if else" Statement known as the Ternary Operator in JavaScript (as well as many other programming languages) which involves placing both `if` and `else` in the same line. It prints or assigns one of two values based on a condition and is structured "X if condition else Y".

# num = 6
# a = 6
# b = 7
# c = 9
# age = 25
# temperature = 30
# user_role = 'admin'

# status_pos_or_neg = 'Positive' if num > 0 else 'Negative'
# status_even_or_odd = 'Odd' if num % 2 == 1 else 'Even'
# status_age = 'Adult' if age >= 18 else 'Teen' if age >= 13 else 'Child'
# status_temperature = 'Hot' if temperature > 30 else 'Warm' if temperature > 15 else 'Cold'
# status_user = 'Full access' if user_role == 'admin' else 'Limited access'

# print(f'num is {status_even_or_odd} and {status_pos_or_neg}')

# max_num = (a if a > b else b) if (a if a > b else b) > c else c # Nesting Python Conditional Expressions in this manner is redundant as illustrated here...
# max_num_nested_ternary_example = a if a > b else b if b > c else c # ...but you can do this to make the code more readable

# min_num = a if a < b else b

# print(max_num_nested_ternary_example)
# print(status_age)
# print(status_temperature)




# # String Methods - 01:27:03

# # `len` = Python Function that takes a String to return the number of characters in that String, i.e. the length of that String. It behaves like the `length` Property in JavaScript, but is not a Property of the String prototype like in JavaScript. Rather, it's a standalone Function in Python. Note, Python's `len` can technically be used with various types of Objects, not just Strings.
# # `find` = String Method in Python which returns the first match, same as JavaScript's `String.prototype.search`.
# # `rfind` = Stands for reverse find and finds the last match.
# # `capitalize` = Capitalizes the first letter of the String.
# # `upper` = Makes all the characters in the String uppercase.
# # `lower` = Makes all of the characters in the String lowercase.
# # `isdigit` = Returns a Boolean indicating if the String comprises only digits.
# # `isalpha` = Returns a Boolean indicating if the String comprises only alphabetic characters.

# # `count` = Returns the number of instances in the String of the String passed to it.
# # `replace` = Returns a new String with all instances in the String of the first Argument replaced with the second Argument.

# # `dir(str)` = Returns a comprehensive list of all the names of the Methods available to and Attributes of Strings, which you can then log with `print`. You can also call `dir` on any Variable itself that is a String, i.e. `dir(string_variable)`.
# # `help(str)` = Returns a comprehensive list of all the Methods available to and Attributes of Strings with information about them, which you can then log with `print`. You can also call `help` on any Variable itself that is a String, i.e. `help(string_variable)`.

# name = input('Enter your full name: ')
# name_length = len(name)
# first_occurrence_of_space = name.find(' ') # Will return -1 if nothing found
# first_occurrence_of_a = name.find('a') # Will return -1 if nothing found
# last_occurrence_of_ad = name.rfind('ad') # Will return -1 if nothing found
# capitalized_name = name.capitalize() 
# all_uppercase_name = name.upper()
# all_lower_name = name.lower()
# is_name_a_digit = name.isdigit() 
# is_name_entirely_alphabetic = name.isalpha() 

# phone_number = input('Enter your phone number: ')
# number_of_dashes_in_phone_number = phone_number.count('-')
# phone_number_with_spaces_instead_of_dashes = phone_number.replace('-', ' ')
# phone_number_with_dashes_removed = phone_number.replace('-', '')

# print(f'The length of the name is {name_length}')
# print(f'The first occurrence of a space is at position {first_occurrence_of_space}')
# print(f'The first occurrence of \'a\' is at position {first_occurrence_of_a}')
# print(f'The last occurrence of \'ad\' is at position {last_occurrence_of_ad}')
# print(f'The capitalized name is {capitalized_name}')
# print(f'The name in all uppercase is {all_uppercase_name}')
# print(f'The name in all lowercase is {all_lower_name}')
# print(f'It is {is_name_a_digit} that the name contains only digits')
# print(f'It is {is_name_entirely_alphabetic} that the name contains only alphabetic characters')

# print(f'There are {number_of_dashes_in_phone_number} dash in the phone number')
# print(f'{phone_number_with_spaces_instead_of_dashes} should have spaces instead of dashes, and {phone_number_with_dashes_removed} should simply have the dashes removed')

# print(all_string_methods)




# # Validate User Input Program - 01:35:08

# # Rules for program:
# # 1. `username` is not more than 12 characters long
# # 2. `username` must not contain spaces
# # 3. `username` must not contain digits

# username = input('Enter your username to see if it\'s valid: ')
# is_user_input_valid = len(username) <= 12 and username.find(' ') < 0 and username.isalpha()

# print(f'It is {is_user_input_valid} that the username is valid')




# # String Indexing - 01:39:09

# # String Indexing = Accessing the elements of a sequence using `[]`, aka the Indexing Operator. The Indexing Operator can take up to 3 Arguments: The first Argument alone returns the character at that index, the first and second Arguments together return the section of the String from and inclusive of the starting index to and excluding the ending index, and the first second and third Arguments together return the String from and inclusive of the starting index to and excluding the ending index according to the step specified in the third Argument. The format for this is `[start:end:step]`.

# credit_card_number = '1234-5678-9012-3456'

# first_character_is = credit_card_number[0]
# last_character_is = credit_card_number[-1] # String Indexing will "wrap around" with negative values
# second_to_last_character_is = credit_card_number[-2] # String Indexing will "wrap around" with negative values
# first_four_characters_are = credit_card_number[:4] # String Indexing defaults 0 as the first Argument regardless of whether or not it's specified
# all_odd_indexed_characters = credit_card_number[::2] # String Indexing defaults 0 as the first Argument and the last index as the second Argument regardless of whether or not it's specified
# all_even_indexed_characters = credit_card_number[1::2]
# every_third_character_from_beginning_is = credit_card_number[::3]
# every_third_character_beginning_count_at_second_index_is = credit_card_number[1::3]
# last_four_digits = credit_card_number[-4:]
# reversed_order = credit_card_number[::-1] # A negative step Argument will reverse the stepping order, which of course effectively reverses the String when the first and second Arguments are the first and last character, respectively, as is the case with the defaults

# print(first_character_is)
# print(last_character_is)
# print(second_to_last_character_is)
# print(first_four_characters_are)
# print(all_odd_indexed_characters)
# print(all_even_indexed_characters)
# print(every_third_character_from_beginning_is)
# print(every_third_character_beginning_count_at_second_index_is)
# print(last_four_digits)
# print(reversed_order)




# # Format Specifiers - 01:46:34

# # Format Specifiers = {value:flags} format a value by following it with a colon and whichever flags you specify after the colon

# # `:.<number>f` = round to that many decimal places (fixed point)
# # `:<number>` = allocate that many spaces
# # `:03` = allocate and zero pad that many spaces
# # `:<` = left justify
# # `:>` = right justify
# # `:^` = center align
# # `:+` = use a plus sign to indicate positive value
# # `:=` = place sign to leftmost position
# # `: ` = insert a space before positive numbers
# # `:,` = comma separator

# price1 = 3.14959
# price2 = -987.65
# price3 = 12.34
# price4 = 12345.67

# print(f'Price 1 rounded at two decimal places is {price1:.2f}') # `price1` with Format Specifier indicating that two decimal places should be displayed and rounded
# print(f'Price 2 at 3 decimal places is {price2:.3f}') # `price2` with Format Specifier indicating that three decimal places should be displayed which, in the case of `price2`, adds an extra 0, and that anything after that will round (so it will effectively simply truncate in the case of `price2`, so the `f` signifying that the number should be formatted as a fixed-point number is important otherwise you'd get -9.88e+02)
# print(f'Price 3 with 10 spaces allocated to it {price3:10}') # `price3` with Format Specifier indicating that 10 spaces should be allocated to its display regardless of its length
# print(f'Price 1 with 12 spaces allocated to it filled with zeros {price1:012}') # `price1` with Format Specifier indicating that 12 spaces should be allocated to its display regardless of its length and the spaces should be filled with zeros
# print(f'Price 3 with 12 spaces allocated to it and left-justified is {price3:<12} and I\'m adding text afterward to show justification boundaries') # `price3` with Format Specifier indicating that 12 spaces should be allocated to its display regardless of its length and that it should be left-justified
# print(f'Price 3 with 12 spaces allocated to it and right-justified is {price3:>12} and I\'m adding text afterward to show justification boundaries') # `price3` with Format Specifier indicating that 12 spaces should be allocated to its display regardless of its length and that it should be right-justified
# print(f'Price 3 with 12 spaces allocated to it and center-justified is {price3:^12} and I\'m adding text afterward to show justification boundaries') # `price3` with Format Specifier indicating that 12 spaces should be allocated to its display regardless of its length and that it should be center-justified
# print(f'Price 3, which is a positive value, with positivity specified is {price3:+}') # `price3` with Format Specifier indicating that plus sign should be shown if the value is positive
# print(f'Price 4 comma delimited is {price4:,}') # `price4` with Format Specifier indicating that value should be separated by commas (if its length is 4 digits or more)
# print(f'Price 4 comma delimited with plus sign and rounded to the nearest one decimal place truncated is {price4:+,.1f}') # `price4` with a series of Format Specifiers




# # While Loops - 01:51:54

# # While Loop = Executes some code WHILE some condition remains `True`, which could be infinite (works well for waiting for user input) and can exit with the `break` Statement. It can also continue with the `continue` Statement, which skips the rest of the code inside the loop for the current iteration and jumps back to the beginning of the loop to check the condition again.


# name = input('Enter your name: ')

# if name == '': # Without a While Loop you can only prompt the user to enter something once...
#     print('You did not enter your name')
# else:
#     print(f'Hello {name}')

# # ..vs...

# while name == '': # ...continually prompting the user until some requirement is met, in this case until the user enters something other than an empty String
#     print('You did not enter your name!')
#     name = input('Enter your name: ')
# print(f'Hello {name}')


# age = int(input('Enter your age: '))

# while age < 0:
#     print('Age can\'t be anything other than 0 or a positive number')
#     age = int(input('Enter your age: '))

# print(f'You are {age} years old')


# food = input('Enter a food you like (press \'q\' to quit): ')

# while not food == 'q':
#     print(f'You like {food}')
#     food = input('Enter a food you like (press \'q\' to quit): ')

# print('bye')

# num = int(input('Enter a # between 1-10: '))

# while num < 1 or num > 10:
#     print(f'{num} is not valid')
#     num = int(input('Enter a # between 1-10: '))

# print(f'Your number is {num}')




# # Python Compound Interest Calculator - 01:58:52

# principle = 0
# rate = 0
# time = 0

# while True:
#     principle = float(input('Enter the principle amount: '))
#     if principle < 0:
#         print('Principle can\'t be less than or equal to zero')
#     else:
#         break

# while True:
#     rate = float(input('Enter the interest rate: '))
#     if rate < 0:
#         print('Interest rate can\'t be less than or equal to zero')
#     else:
#         break

# while True:
#     time = float(input('Enter the interest time: '))
#     if time < 0:
#         print('Time can\'t be less than or equal to zero')
#     else:
#         break

# total = principle * pow((1 + rate / 100), time)

# print(principle)
# print(rate)
# print(time)

# print(f'Balance after {time} year/s: {total:.2f}')




# # For Loops - 02:06:29

# # For Loops = Execute a block of code a fixed number of times. You can iterate over a range, String, sequence, etc.

# for x in range(1, 11): # The second number is exclusive so to count to 10 make it 11
#     print(x)

# for x in reversed(range(1, 11)): # Use the `reversed` Method to count backward
#     print(x)


# for x in range(1, 11, 2): # The third number passed to the For Loop is the step, which defaults to 1, so increasing the step to 2 starting from 1 and going to but exclusive of 11 counts odd numbers from 1-9, and note that the step must be an Integer
#     print(x)


# credit_card = '1234-5678-9012-3456'

# for x in credit_card: # You can also For Loop over characters in a String
#     if x.isdigit():
#         print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue # The `continue` Statement skips to the next iteration, whereas the `break` Statement breaks out of the loop entirely
#     else:
#         print(x)




# # Countdown Program - 02:11:33

# import time # The `time` Module has the `sleep` Function, which is what we need it for
# import math

# time.sleep(3) # The program will sleep for the given number of seconds passed to the `sleep` Function of the `time` Module

# print('3 seconds have passed')

# my_time = int(input('Enter the time in seconds: '))

# for x in range(0, my_time): # Counting forwards by 1 using a For Loop works without providing the step, i.e. the 3rd value, because +1 is the default step
#     print(f'In seconds {x} passed')
#     time.sleep(1)

# for x in range(my_time, 0, -1): # To count backwards using a For Loop the step, i.e. the 3rd value, must be specified as -1
#     print(f'Countdown in seconds: {x}')
#     time.sleep(1)

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60 # Type Casting as `int` simply makes the otherwise long Float point value a long Integer without a heading 0
#     hours = int(x / 3600) # Type Casting as `int` simply makes the otherwise long Float point value a long Integer without a heading 0
#     print(f'{hours:02}:{minutes:02}:{seconds:02}') # Using Format Specifiers to two places and to pad the numbers with a zero if need be effectively truncates the long Integers created in minutes and hours
#     time.sleep(1)




# # Nested Loops - 02:17:29

# # Nested Loop = A loop within another loop (outer, inner) where you could have a While Loop inside of a While Loop, a For Loop inside of a For Loop, a While Loop inside of a For Loop, or a For Loop inside of a While Loop.

# for x in range(3):

#     for y in range(1, 10): # Because the second number is excluded from a range, this is a 1-9 range
#         print(y, end='') # `print` Statements have a second Argument, the `end` Argument, which is the character that should follow the printed Statement and it defaults to `\n`, namely a newline character, so setting it to an empty String will print and remain on the same line

#     print() # This will simply create a newline from the outer loop after the inner loop has completed




# # Rectangle Printing Program - 02:21:02

# rows = int(input('Enter the # of rows: '))
# columns = int(input('Enter the # of columns: '))
# symbol = input('Enter a symbol to use: ')

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end='')
#     print()




# # Collections - 2:23:02

# # Collection = A single Variable used to store multiple values, often referred to as elements just like in JavaScript Arrays, of which there are 4 types List, Set, Tuple, Dict

# # List = [] ordered and changeable where duplicates are okay.
# # Set = {} unordered and immutable, but adding and removing are okay, however, no duplicates.
# # Tuple = () ordered and unchangeable, where duplicates are okay and it's faster performance wise.

# # `dir(list)` = Returns a comprehensive list of all the names of the Methods available to and Attributes of a List, which you can then log with `print`. You can also call `dir` on any Variable itself that is a List, e.g. `dir(list_variable)`.
# # `help(list)` = Returns a comprehensive list of all the Methods available to and Attributes of a List with information about it, which you can then log with `print`. You can also call it on any Variable itself that is a List, e.g. `help(list_variable)`.

# # `dir(set)` = Returns a comprehensive list of all the names of the Methods available to and Attributes of a Set, which you can then log with `print`. You can also call `dir` on any Variable itself that is a Set, e.g. `dir(set_variable)`.
# # `help(set)` = Returns a comprehensive list of all the Methods available to and Attributes of a Set with information about it, which you can then log with print. You can also call it on any Variable itself that is a Set, i.e. `help(set_variable)`.

# # `dir(tuple)` = Returns a comprehensive list of all the names of the Methods available to and Attributes of a Tuple, which you can then log with `print`. You can also call `dir` on any Variable itself that is a Tuple, `i.e. dir(tuple_variable)`.
# # `help(tuple)` = Returns a comprehensive list of all the Methods available to and Attributes of a Tuple with information about it, which you can then log with `print`. You can also call it on any Variable itself that is a Tuple, e.g. `help(tuple_variable)`.

# veggie = 'pea'

# print(veggie) # The Variable `veggie` unchanged
# print([veggie]) # The Variable `veggie` as a List
# print({veggie}) # The Variable `veggie` as a Set
# print((veggie)) # The Variable `veggie` as a Tuple


# fruits = ['apple', 'orange', 'banana', 'coconut'] # Here's a List of fruits called `fruits`

# print(fruits[1]) # Use the Index Operator to access an element in the List, same as you do with Strings, i.e. `[start:end:step]`

# print(fruits[1:3]) # Use the Index Operator to access a range of elements exclusive of the end

# print(fruits[::2]) # You can also only specify a step, knowing that the start and end defaults are the very beginning and very end of the List

# print(fruits[::-1]) # You can even go backwards with a negative value, again, same as String Indexing

# for fruit in fruits: # You can iterate over the elements using For Loops, same as `forEach` of Arrays in JavaScript
# print(fruit)

# print(len(fruits)) # The `len` Function works on Lists the same way it does for Strings

# print('apple' in fruits) # The `in` Membership Operator returns a Boolean, in this case `True`

# print('pineapple' in fruits) # The `in` Membership Operator returns a Boolean, in this case `False`

# fruits[2] = 'kiwi' # Same as Arrays in JavaScript you can reassign elements

# fruits.append('plum') # You can append elements

# fruits.remove('apple') # You can remove elements

# fruits.insert(3, 'fig') # You can insert elements at a designated location

# fruits.sort() # You can sort Lists, the default for which is alphabetical order, same as Arrays in JavaScript

# fruits.reverse() # You can reverse Lists, same as Arrays in JavaScript

# print(fruits.index('fig')) # You can get the index of an element

# fruits.append('fig') # You can append another fig because duplicates are okay in Lists

# print(fruits.count('fig')) # You can get the count of the specified element

# print(fruits.count('spinach')) # Getting the count of a specified element which doesn't exist will gracefully return 0 when the element is not present

# fruits.clear() # You can clear all the elements out of a List with the `clear` Method

# print(fruits)


# fruits = {'apple', 'orange', 'banana', 'coconut'} # Here's a Set of fruits called fruits

# print(fruits) # Every time you execute a Python script containing a Set the order of the Set is subject to change because Sets, unlike Lists, Tuples and Dicts, are inherently unordered. For this reason you cannot use the Index Operator on a Set and you cannot change the value of a Set. You can, however, add and remove elements of a Set but you cannot add duplicates to a Set, though trying to do so will not throw an error, rather, will simply not affect the Set

# print(len(fruits)) # Using the `len` Function to show the length of the Set

# print('pineapple' in fruits) # Using the `in` Membership Operator to check if the element 'pineapple' is in the Set

# fruits.add('pineapple') # Though you can't change the value of a Set you can still add elements to it

# print(fruits)

# fruits.remove('pineapple') # You can also remove elements

# print(fruits)

# fruits.pop() # You can remove the "first" element by using the `pop` Method, though because Sets are unordered the element to be removed will be random

# print(fruits)

# fruits.add('banana') # Adding a duplicate to a Set doesn't work so trying to do so throw an error

# print(fruits)

# fruits.clear() # You can clear a Set entirely, same as illustrated in Lists

# print(fruits)


# fruits = ('apple', 'orange', 'banana', 'coconut') # Here's a Tuple of fruits called fruits which, despite having different Properties than a List or a Set, is rendered faster than those, so use Tuples when possible

# print(len(fruits)) # Using the `len` Function to show the length of the Tuple

# print('pineapple' in fruits) # Using the `in` Operator to check if the element 'pineapple' is in the Tuple

# print(fruits.index('apple')) # Just like Lists, but unlike Sets, we can find the index of an element because Tuples are ordered

# print(fruits.count('coconut')) # Like both Lists and Sets we can use the `count` Method, but if we want to add another coconut we couldn't because Tuples are immutable

# for fruit in fruits: # Like all Collections (Lists, Sets, Tuples and Dicts) they are iterable so we can run For Loops on them
#     print(fruit)




# # Shopping Card Program - 02:38:07

# # This is to practice Lists, Sets and Tuples

# foods = []
# prices = []
# total = 0

# while True:
#     food = input('Enter a food to buy (press \'q\' to Quit): ')
#     if food.lower() == 'q':
#         break
#     else:
#         price = float(input('Enter the price of a {food}: $'))
#         foods.append(food)
#         prices.append(price)

# print('----- Your Cart -----')

# for food in foods:
#     print(food, end=' ') # The `end=' '` is to horizontally print all the foods on one line

# for price in prices:
#     total += price

# print() # This empty `print` Statement is to create another line
# print(f'Your total is {total} dollars')




# # 2D Collections - 2:45:20

# # 2D Collection = A Collection of Collections, i.e. [list1, list2, list3], which is useful if you need a grid or matrix of data, like a spreadsheet. You can make a List of Lists, a Tuple of Tuples, a List of Tuples, a Tuple of Lists, etc. 

# fruits =     ['apple', 'orange', 'banana', 'coconut'] # You can add whitespace within the defining of a Variable to make Variables of Collections that will be collated into a 2D Collection easier to read
# vegetables = ['celery', 'carrots', 'potatoes']
# meats =      ['chicken', 'fish', 'turkey']

# groceries = [fruits, vegetables, meats]

# print(groceries[0]) # `groceries` at index 0 is the `fruits` List

# print(groceries[0][0]) # `groceries` at index 0 with index 0 set on the `fruits` List is the 'apple' element, i.e. row 0 column 0

# groceries = [['apple', 'orange', 'banana', 'coconut'],
#              ['celery', 'carrots', 'potatoes'],
#              ['chicken', 'fish', 'turkey']] # You can also create 2D Collections directly like this, without defining the individual rows first

# for list in groceries: # If you need to iterate over the elements of a 2D Collection you can use Nested Loops
#     for food in list:
#         print(food, end=' ') # Using the second Argument in the `print` Method to keep every food on one line
#     print() # This empty `print` Statement is to create another line at the end of each individual List so that the end result looks more like a grid with rows and columns




# # Keypad Program - 2:51:37

# # Sets are unordered so we can't use those for this program, and Tuples are faster than Lists so we should use them if we can, and we can for this particular program.

# num_pad = ((1,2,3),
#            (4,5,6),
#            (7,8,9))

# for row in num_pad:
#     for num in row:
#         print(num, end=' ')
#     print()




# # Quiz Game Program - 2:54:00

# questions = ('How many elements are in the periodic table?: ',
#              'Which animal lays the largest eggs?: ',
#              'What is the most abundant gas in the Earth\'s atmosphere?: ',
#              'How many bones are in the human body?: ',
#              'Which planet in the solar system is the hottest?: ') # Define a Tuple of questions

# options = (('A. 116', 'B. 117', 'C. 118', 'D. 119' ),
#            ('A. Whale', 'B. Crocodile', 'C. Elephant', 'D. Ostrich' ),
#            ('A. Nitrogen', 'B. Oxygen', 'C. Carbon Dioxide', 'D. Hydrogen' ),
#            ('A. 206', 'B. 207', 'C. 208', 'D. 209' ),
#            ('A. Mercury', 'B. Venus', 'C. Earth', 'D. Mars' )) # Define a 2D Tuple of possible answers

# correct_answers = ('C', 'D', 'A', 'A', 'B') # Define the correct answers
# guesses = [] # Initialize guesses as a List
# score = 0 # Initialize score as 0

# while len(guesses) < len(questions):
#     print(questions[len(guesses)])
#     print(options[len(guesses)])
#     user_answer = input().upper()
#     guesses.append(user_answer)
#     if user_answer == correct_answers[len(guesses) - 1]:
#         score += 1
#         print('Correct \n')
#     else:
#         print('Incorrect')
#         print(f'{correct_answers[len(guesses) - 1]} is the correct answer\n')
    

# print(f'Your guesses were {guesses}')
# print(f'The correct answers were {correct_answers}')
# print(f'Your score is {int(score / len(questions) * 100)}%')




# # Dictionaries - 3:03:26

# # Dictionary = A Collection of {key: value} pairs ordered and changeable, with no duplicates. They're like Objects in JavaScript but 1) with Dictionaries keys can be of any immutable type, e.g. Strings, numbers or Tuples, whereas in JavaScript keys are typically Strings, symbols or any valid JavaScript identifier. As long as they're not reserved keywords, keys don't need to be placed in quotes in JavaScript Objects, 2) JavaScript Objects can have prototypes, which means they can inherit Properties and Methods from their prototype chain whereas Dictionaries in Python do not have this concept of prototypes, 3) You can iterate over a Dictionary using a For Loop directly on the Dictionary which by default iterates over the Dictionary's keys whereas in JavaScript you have to use a Method like `Object.keys` to get an Array of keys, 4) You access the Property of an Object in JavaScript using dot notation, but with Python Dictionaries you use square brackets to access the values for keys, the same way you do to access elements in ordered Collections i.e. Lists and Tuples, or the `get` Method on Dictionaries, to which you can also provide a default value if a key doesn't exist.

# # `dir(dict)` = Returns a comprehensive list of all the names of the Methods available to and Attributes of Dictionaries, which you can then log with `print`. You can also call `dir` on any Variable itself that is a Dictionary, e.g. `dir(tuple_variable)`.
# # `help(dict)` = Returns a comprehensive list of all the Methods available to and Attributes of Dictionaries with information about them, which you can then log with `print` You can also call `dir` on any Variable itself that is a Dictionary, e.g. `help(tuple_variable)`.


# capitols =  { 'USA': 'Washington D.C.',
#               'India': 'New Delhi',
#               'China': 'Beijing',
#               'Russia': 'Moscow'
#             } # Whitespace is ok in defining Dictionaries to get key:value pairs to line up

# print(capitols.get('USA')) # This will return "Washington D.C"

# print(capitols.get('Japan')) # This will return `None`, which is a reserved word in Python similar to `undefined` or `null` in JavaScript but with some slight differences, which is useful for `if` Statements

# if capitols.get('Japan'):
#     print('That capitol exists')
# else:
#     print('That capitol doesn\'t exist') # This `else` block should print accordingly

# capitols.update({'Germany': 'Berlin'}) # Using the `update` Method we can add a new key:value pair or `update` an existing key:value pair

# print(capitols) # This will print the capitols Dictionary but include the 'Germany': 'Berlin' key:value pair because capitols has been updated with it

# capitols.update({'USA': 'Detroit'}) # This is an example of changing an existing key:value pair

# print(capitols) # So this will print the capitols Dictionary but include the 'USA': 'Detroit' key:value pair because capitols has been updated with it

# capitols.pop('China') # The `pop` Method removes the key:value pair of the specified key

# print(capitols) # So this will print the capitols Dictionary without the 'China': 'Beijing' key:value pair

# capitols.popitem() # This removes the last key:value in the Dictionary

# print(capitols) # So in this case the 'Germany': 'Berlin' key:value pair will be gone

# print(capitols.keys()) # This returns all the keys of a Dictionary and presents them as if they're in a List, but technically they're in a View Object (yes, an Object, not Dictionary)

# for key in capitols.keys(): # You can iterate over specifically the keys
#     print(key)

# for key_value in capitols: # You can iterate over just the Dictionary but it will still automatically isolate the keys, even through the elements we're identifying in the Dictionary are the key_value pairs themselves
#     print(key_value)

# for value in capitols.values(): # To isolate the values use the `values` Method
#     print(value)

# for key, value in capitols.items(): # For getting both keys and values individually you can have two Arguments between `for` and `in` in the For Loop, then use the items Method, and then use a Formatted String to print them
#     print(f'{key}: {value}')

# for item in capitols.items(): # If formatting isn't an issue you can simply use the `items` Method directly, which returns a Dictionary Object which resembles a 2D List of Tuples
#     print(item)

# capitols.clear() # This removes all key:value pairs from the Dictionary

# print(capitols) # With `clear` having just run, only empty curly braces should print here, signifying a now empty Dictionary




# # Concession Stand Program - 3:11:33

# menu = {
#     'pizza': 3.00,
#     'nachos': 4.50,
#     'popcorn': 6.00,
#     'fries': 2.50,
#     'chips': 1.00,
#     'pretzel': 3.50,
#     'soda': 3.00,
#     'lemonade': 4.25
# }

# cart = []
# total = 0

# for key, value in menu.items(): # To display the menu nicely you can use two Arguments in the For Loop, since the `items` Method returns a 2D Dictionary Object of Tuples
#     print(f'{key:10}: {value:.2f}') # Format Specifying to display 10 spaces after the key and two decimal places after the value, where the f part of the :.2f makes the number a fixed-point number otherwise, despite the :.2 being specified, the zeros would be rounded off

# while True: # Keep the loop active to receive user input by using a While Loop
#     food = input('Select an item (q to quit): ').lower()
#     if food  == 'q': 
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# for food in cart:
#     total += menu.get(food)
#     print(food, end=' ')

# print()
# print(f'Total is {total:.2f}')




# # Random Numbers - 3:19:42

# import random # Import Python's native `random` Module

# random_number = random.randint(1, 6) # This generates a random Integer between 1 and 6 inclusive of both 1 and 6

# print(random_number)

# low = 1
# high = 100
# random_number = random.randint(low, high) # The `randint` Method of Python's native `random` Module also takes Variables as Arguments in lieu of Integers directly

# print(random_number)

# random_floating_point_number = random.random() # If you need a random floating point number between 0 and 1 inclusive of 0 but exclusive of 1 you can use the `random` Method on the `random` Module

# print(random_floating_point_number)

# options = ('rock', 'paper', 'scissors')
# option = random.choice(options)

# print(option)

# cards = ['2','3','4','5','6','7','8','9','10','J','K','Q','A']
# random.shuffle(cards) # Use the `shuffle` Method of Python's native `random` Module to shuffle a List in place, so take note that this does not return a new Variable you can store separately

# print(cards)




# # Number Guessing Game Program - 3:24:17

# # `dir(random)` = Returns a comprehensive list of all the names of the Methods available to and Attributes of Python's native `random` Module, which you can then log with `print`.

# # `help(dict)` = Returns a comprehensive list of all the Methods available to and Attributes of Python's native `random` Module with information about those Methods, which you can then log with `print`.

# import random

# lowest_num = 1
# highest_num = 50
# answer = random.randint(lowest_num, highest_num)
# guesses = 0

# while True:
#     guess = input(f'Select a number between {lowest_num} and {highest_num}: ')
    
#     if guess.isdigit():
#         guesses += 1
#         guess = int(guess)

#         if (guess < lowest_num or guess > highest_num):
#             print('That number is out of range')
#         elif guess < answer:
#             print('Too low')
#         elif guess > answer:
#             print('Too high')
#         else:
#             print(f'Correct! {guess} is the number. You got it in {guesses} guesses')
#             break
#     else:
#         print('Invalid guess')




# # Rock, Paper Scissors Game Program - 3:32:37

# import random

# options = ('rock', 'paper', 'scissors') # Using a Tuple is better than using a List, since we won't be changing the options for this game
# scores = {
#     'player': 0,
#     'computer': 0
# }

# is_running = True

# while is_running: # We could also say `while True` and then use a `break` Statement but if the conditions were to develop more lines it would be more difficult to manage the code than to have a dedicated Variable for designating if the program is running or not, so the this approach with a `is_runnin`g Variable is better

#     computer_choice = random.choice(options)

#     player_choice = input('Enter a choice (rock, paper or scissors) or q to quit: ').lower()

#     print(f'\nPlayer\'s choice: {player_choice}\nComputer\'s choice: {computer_choice}\n')

#     if player_choice == 'rock':
#         if computer_choice == 'paper':
#             scores['computer'] += 1
#         elif computer_choice == 'scissors':
#             scores['player'] += 1
#     elif player_choice == 'paper':
#         if computer_choice == 'rock':
#             scores['player'] += 1
#         elif computer_choice == 'scissors':
#             scores['computer'] += 1
#     elif player_choice == 'scissors':
#         if computer_choice == 'rock':
#             scores['computer'] +=1
#         elif computer_choice == 'paper':
#             scores['player'] += 1
#     elif player_choice == 'q':
#         is_running = False
#     else:
#         print('Invalid entry')

# print(f'\nFinal scores are: \nPlayer: {scores['player']}\nComputer: {scores['computer']}')




# # ASCII Dice Roller Program - 3:42:05

# import random

# dice_art = {

#     1: (
#         " ------------------- ",
#         "|                   |",
#         "|                   |",
#         "|                   |",
#         "|         *         |",
#         "|                   |",
#         "|                   |",
#         "|                   |",
#         " ------------------- "
#     ),

#     2: (
#         " ------------------- ",
#         "|                   |",
#         "|    *              |",
#         "|                   |",
#         "|                   |",
#         "|                   |",
#         "|              *    |",
#         "|                   |",
#         " ------------------- "
#     ),

#     3: (
#         " ------------------- ",
#         "|                   |",
#         "|    *              |",
#         "|                   |",
#         "|         *         |",
#         "|                   |",
#         "|              *    |",
#         "|                   |",
#         " ------------------- "
#     ),

#     4: (
#         " ------------------- ",
#         "|                   |",
#         "|    *         *    |",
#         "|                   |",
#         "|                   |",
#         "|                   |",
#         "|    *         *    |",
#         "|                   |",
#         " ------------------- "
#     ),

#     5: (
#         " ------------------- ",
#         "|                   |",
#         "|    *         *    |",
#         "|                   |",
#         "|         *         |",
#         "|                   |",
#         "|    *         *    |",
#         "|                   |",
#         " ------------------- "
#     ),

#     6: (
#         " ------------------- ",
#         "|                   |",
#         "|    *         *    |",
#         "|                   |",
#         "|    *         *    |",
#         "|                   |",
#         "|    *         *    |",
#         "|                   |",
#         " ------------------- "
#     )
# }

# dice = []
# total = 0
# num_of_dice_input_by_user = int(input('How many dice do you want to roll?: '))


# for die in range(num_of_dice_input_by_user):
#     random_number_between_1_and_6 = random.randint(1, 6)
#     dice.append(random_number_between_1_and_6)
#     for line in dice_art[random_number_between_1_and_6]: # You can also use the `get` Method instead of using `[]`
#         print(line)


# print(f'\nYour total is {sum(dice)}')




# # Functions - 3:52:11

# # Function = A block of reusable code which can take Arguments in a `()` prefaced with the word `def` which, to invoke, you place the `()` containing the Arguments after its name, identically to JavaScript.

# # `return` = A Statement used to end a Function and send a result back to the place from which the Function was invoked.

# # There are 4 types of Function Arguments: 1. Positional Arguments, 2. Default Arguments, 3. Keyword Arguments, and 4) Arbitrary Arguments.

# # Positional Arguments = During a Function call, Arguments passed to the Function in the order the Function expects the Arguments.

# # Default Arguments = In a Function definition, Arguments with a default value which are used if no Argument is passed during the Function call.

# # Keyword Arguments = During a Function call, Arguments passed to the Function with the Argument name.

# # Arbitrary Arguments = In a Function definition, an Argument prefixed with an asterisk, `*`, which allows the Function to accept any number of Arguments (this is also known as a Variadic Functions). The standard convention is to call this Argument `*args` in the case of Arbitrary Positional Arguments, and `**kwargs` in the case of Arbitrary Keyword Arguments.

# def happy_birthday(name, age): # Define a Function called `happy_birthday`
#     print(f'♬ Happy birthday to {name} ♫')
#     print(f'♪ Happy birthday to {name} ♩')
#     print(f'♬ Happy birthday dear {name} ♫')
#     print(f'♬ Happy birthday to {name} ♫')
#     print(f'♬ You\'re {age} years old ♫')
#     print(f'♪ You\'re {age} years old ♩')
#     print(f'♬ You\'re {age} years old ♫')
#     print(f'♪ You\'re {age} years old ♩')

# Call the happy_birthday Function several times passing it different Arguments each time
# happy_birthday('Bro', 20)
# happy_birthday('Steve', 30)
# happy_birthday('Joe', 40)

# def display_invoice(username, amount, due_date): # Define a Function called `display_invoice`
#     print(f'Hello {username}')
#     print(f'Your bill of {amount:.2f} is due on {due_date}')

# Call the display_invoice Function a couple times passing it different Arguments each time
# display_invoice('Bro', 42.50, 'Jan 1st')
# display_invoice('Joe', 100.01, 'Feb 2nd')


# Some examples using `return` to return a value from a Function
# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))


# Another example using `return` to return a value from a Function
# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return f'{first} {last}'

# print(create_name('spongebob', 'squarepants'))




# # Default Arguments - 4:02:51

# # Default Arguments = A default value for certain Parameters in a Function, same as in JavaScript, which make your Functions more flexible and reduce the number of Arguments which must be passed, i.e. nothing needs to be passed solely as a placeholder.

# def net_price(list_price, discount=0, tax=0.05): # Here we want a default value for `discount` because sometimes there isn't one, and a default value for `tax` because it's usually 0.05
#     return f'{list_price * (1 - discount) * (1 + tax):.2f}'

# price_in_jurisdiction_b = net_price(500) # Passing just one Argument like this will pass 500 as `list_price` but use the default values for the `discount` and `tax` Arguments

# price_in_jurisdiction_a = net_price(500, .1, .08) # Passing all three Arguments like this will pass 500 as `list_price`, .1 as `discount` and .08 as `tax`

# price_in_jurisdiction_c = net_price(700, .075, .15) # Passing all three Arguments like this will pass 700 as `list_price`, .075 as `discount` and .15 as `tax`

# print(price_in_jurisdiction_a)
# print(price_in_jurisdiction_b)
# print(price_in_jurisdiction_c)


# import time

# def count(end, start=0): # Default Arguments must follow non-Default Arguments in a Function definition, so `start=0` must be at the end of the Arguments
#     for x in range(start, end + 1):
#         print(x)
#         time.sleep(1)
#     print('Done!')

# print(count(4))

# print(count(5, 1))




# # Positional Arguments and Keyword Arguments - 4:08:56

# # Positional Argument = An Argument passed to a Function in the order the Function expects it.

# # Keyword Argument = An Argument preceded by an identifier when passed to a Function, which helps with readability and makes the order of Arguments not matter in a Function call.

# def hello(greeting, title, first, last):
#     print(f'{greeting} {title} {first} {last}')

# print(hello('Hello', 'Mr.,', 'John', 'Smith')) # This is a call to the `hello` Function using Positional Arguments

# print(hello(last='Smith', title='Mr.', greeting='Hello', first='John')) # This is a call to the `hello` Function using Keyword Arguments showing that they can be in any order

# print(hello('Hello', last='Smith', first='John', title='Mr.')) # If you're mixing and matching Positional Arguments and Keyword Arguments in your call to a Function you have to make sure the Positional Arguments come first

# for x in range(1, 11):
#     print(x, end=' ') # `end` is a Keyword Argument found within Python's built-in `print` Method

# print(1,2,3,4,5,6,sep=' is less than ') # `sep`, which stands for separate, is also a Keyword Argument found within Python's built-in `print` Method


# def get_phone(first_few_digits, last_few_digits, country=1, area=123): # This Function has Default Arguments for `country` and `area`, expecting that it will mostly be used for U.S. numbers
#     return (f'{country}-{area}-{first_few_digits}-{last_few_digits}')

# phone_num = get_phone(456, country=55, area=123, last_few_digits=7890) # If you're mixing and matching Positional Arguments and Keyword Arguments in your call to a Function you have to make sure the Positional Arguments come first

# print(phone_num)




# # Arbitrary Arguments - 4:15:42

# # Arbitrary Arguments = They allow you to pass multiple Positional Arguments as a single Argument packed into a Tuple and prefixed with `*`, which is the non-Keyword Argument Unpacking Operator, and to pass multiple Keyword Arguments packed into a Dictionary and prefixed with `**` which is the Keyword Argument Unpacking Operator.

# def add_two_nums(a, b): # This `add_two_nums` Function only takes two Arguments
#     return a + b

# print(add(1, 2))

# def add_any(*nums): # This `add_any` Function takes an unspecified number of Arbitrary Arguments
#     print(type(nums)) # Printing how this `add_any` Function interprets these Arbitrary Arguments demonstrates that it interprets them as a Tuple
#     total = 0
#     for num in nums: # Knowing that `nums` is a Tuple we know we can iterate over it
#         total += num
#     return total

# print(add_any(1, 2, 5.3, 2.8, 7.3, 3))


# def display_name(*names): # This `display_name` Function takes an unspecified number of Arbitrary Arguments
#     for name in names: # Knowing that `names` is a Tuple we know we can iterate over it
#         print(name, end=' ')
#     print()

# display_name('Dr', 'Spongebob', 'Harold', 'Squarepants', 'III')


# def print_address(**kwargs): # This `print_address` Function takes an unspecified number of Keyword Arguments
#     print(type(kwargs)) # Knowing that `kwargs` is a Dictionary we know we can iterate over it
#     for key, value in kwargs.items(): # Knowing that `kwargs` is a Dictionary we can call Dictionary specific Methods on it like the `items` Method
#         print(f'{key}: {value}')
 


# print_address(street='123 Fake Street', # When calling Functions you can put Arguments on different lines and it particularly makes Keyword Arguments more readable
#               apt=100,
#               city='Detroit',
#               state='MI',
#               zip=54321
#               )


# def shipping_label(*args, **kwargs): # When defining a Function with a mix of Arbitrary non-Keyword Arguments and Arbitrary Keyword Arguments, the Arbitrary non-Keyword Arguments must come first followed by the Arbitrary Keyword Arguments
#     for arg in args:
#         print(arg, end=' ')
#     print()
#     for value in kwargs.values():
#         print(value, end=' ')
#     print()

# shipping_label('Dr.', 'Spongebob', 'Squarepants', 'III', # When calling a Function with a mix of Arbitrary non-Keyword Arguments and Arbitrary Keyword Arguments, the Arbitrary non-Keyword Arguments must come first followed by the Arbitrary Keyword Arguments
#                street='123 Fake St',
#                apt=100,
#                city='Detroit',
#                state='MI',
#                zip=54321
#                )




# # Iterables - 4:30:32

# # Iterable = An Object or Collection that can return its elements one at a time, allowing it to be iterated over in a loop.

# numbers_list = [1, 2, 3, 4, 5]

# for number in reversed(numbers_list): # Because `numbers_list` is a List and Lists are changeable Collections, we can use the `reversed` Method on `numbers_list` directly inside the loop (but if `numbers_list` were an immutable Collection like a Set you'd get "TypeError: 'set' object is not reversible")
#     print(number, end=' ' if number > 1 else '\n') # This Ternary inside the `print` Statement is computationally expensive, I'm just experimenting with Python Ternaries, which are more verbose than they are in JavaScript


# name_string = 'Bro Code'

# for character in name_string: # name_string is a String so trying to iterate over it defaults to first breaking it into characters, then iterating over those comprising characters
#     print(character, end=' ' if name_string.index(character) != len(name_string) - 1 else '\n') # Again, this Ternary inside the `print` Statement is computationally expensive, I'm just experimenting with Python Ternaries, which are more verbose than they are in JavaScript


# my_dictionary = {
#     "A": 1,
#     "B": 2,
#     "C": 3,
# }

# for will_this_be_a_key_or_a_value in my_dictionary: # By default using a For Loop on a Dictionary...
#     print(will_this_be_a_key_or_a_value) # ...will print the key, not the value...

# for value in my_dictionary.values(): # ...so to print the value you have to specifically use the `values` Method on the Dictionary...
#     print(value)

# for tuple_containing_key_and_value in my_dictionary.items(): # ...or the `items` Method, which returns both the key and the value as a Tuple...
#     print(type(tuple_containing_key_and_value)) # ...as verified here...
#     print(f'The key is {tuple_containing_key_and_value[0]} and the value is {tuple_containing_key_and_value[1]}') # ...and here


# for a, b in my_dictionary.items(): # You can also unpack the `items` Method's return of a Tuple directly in the initial For Loop Statement, where the Variable names can be generic, i.e. they don't need to be key and value, respectively, they can be `a` and `b` as demonstrated here...
#     print(f'The key is {a} and the value is {b}') # ...in which case there's no need to index into the Tuple to get the key and value, you can just use the Variable names you've assigned from the initial For Loop Statement




# # Membership Operators - 4:37:05

# # Membership Operators = Used to test whether a value or Variable is found in a sequence (i.e. in a String, List, Tuple, Set or Dictionary).

# secret_word = 'apple' # For example, have a `secret_word`...

# guessed_letter = input('Guess a letter in the secret word: ') # ...have the user guess letters in it...

# if guessed_letter.lower() in secret_word: # ...use the `in` Membership Operator, which tests to see if a value or a Variable is found within a sequence and returns a Boolean accordingly, to see if the guessed letter is within the `secret_word`...
#     print(f'There is a "{guessed_letter}" in the secret word') 
# else:
#     print(f'There is no "{guessed_letter}" in the secret word')


# if guessed_letter.lower() not in secret_word: # ...or the `not in` Membership Operator , which tests to see if a value or a Variable is not found within a sequence and returns a Boolean accordingly, to see if the guessed letter is not within the `secret_word`
#     print(f'There is no "{guessed_letter}" in the secret word') 
# else:
#     print(f'There is a "{guessed_letter}" in the secret word')


# students = {'spongebob', 'patrick', 'sandy'}

# student = input('Enter the name of a student: ') 

# if student.lower() in students: # Example using the `in` Membership Operator to find a value in a Set
#     print(f'{student} is a student')
# else:
#     print(f'{student} is not a student')


# grades = { 
#     'Sandy': 'A',
#     'Squidword': 'B',
#     'Spongebob': 'C',
#     'Patrick': 'D'
# }

# student = input('Enter the name of a student: ')

# if student.lower() in grades: # Example using the `in` Membership Operator to find a value in a Dictionary
#     print(f'{student}\'s grade is {grades[student]}')
# else:
#     print(f'{student} was not found')


# email = 'BroCode@gmail.com'

# if '@' in email and '.' in email: # Example using the `in` Membership Operator in two conditions to find values in a String
#     print('Valid email')
# else:
#     print('Invalid email')




# # List Comprehensions - 4:45:56

# # List Comprehension = A concise way to create Lists in Python which is compact and easier to read than using a traditional For Loop to create a List. List Comprehensions are set up like [ expression for element in iterable if condition ] and can be compared to `Array.prototype.filter` in JavaScript.

# doubles = [] # The For Loop way of filling this particular List with even numbers looks like this
# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)


# doubles = [ x * 2 for x in range(1, 11) ] # The List Comprehensions way looks like this, where the Argument before the word `for` is the expression

# print(doubles)


# fruits = [ fruit.upper() for fruit in ['apple', 'orange', 'banana', 'coconut'] ] # Here's an example of a List Comprehension using a String

# print(fruits)


# positive_numbers = [ num for num in [-1, -2, 3, 4, 5, -6, 8] if num >= 0 ]

# print(positive_numbers)


# negative_numbers = [ num for num in [-1, -2, 3, 4, 5, -6, 8] if num < 0 ]

# print(negative_numbers)


# even_numbers = [ num for num in [-1, -2, 3, 4, 5, -6, 8] if num % 2 == 0 ]

# print(even_numbers)


# odd_numbers = [ num for num in [-1, -2, 3, 4, 5, -6, 8] if num % 2 == 1 ]

# print(odd_numbers)


# grades = [85, 42, 79, 90, 56, 61, 30]
# pass_grades = [ grade for grade in grades if grade >=60 ]

# print(pass_grades)




# # Match Case Statements, aka Switch Statements - 4:56:17

# # Match Case statements aka Switch Statements = An alternative to using many `elif` Statements wherein you execute some code if a value matches a case, the benefit being that it's cleaner with more readable Syntax, same as in JavaScript

# def day_of_week(day): # This is a Conditional Statement using if/elif/else
#     if day == 1:
#         return 'It is Sunday'
#     elif day == 2:
#         return 'It is Monday'
#     elif day == 3:
#         return 'It is Tuesday'
#     elif day == 4:
#         return 'It is Wednesday'
#     elif day == 5:
#         return 'It is Thursday'
#     elif day == 6:
#         return 'It is Friday'
#     elif day == 7:
#         return 'It is Saturday'
#     else:
#         return 'Not a valid day'


# def day_of_week(day):  # This is the same Statement however using a Match Case Statement, aka a Switch Statement, which is structured the same as in JavaScript except to set the default condition at the end you use `case _:` instead of the word `default:`
#     match day:
#         case 1:
#             return 'It is Sunday'
#         case 2:
#             return 'It is Monday'
#         case 3:
#             return 'It is Tuesday'
#         case 4:
#             return 'It is Wednesday'
#         case 5:
#             return 'It is Thursday'
#         case 6:
#             return 'It is Friday'
#         case 7:
#             return 'It is Saturday'
#         case _:
#             return 'Not a valid day'

# print(day_of_week(1))
# print(day_of_week(2))
# print(day_of_week('pizza'))


# def is_weekend(day): # This is the same Statement except it makes use of the Logical Operator, `|`, to reduce the number of cases
#     match day:
#         case 'Saturday' | 'Sunday':
#             return True
#         case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
#             return False
#         case _:
#             return 'Not a valid day'

# print(is_weekend('Sunday'))
# print(is_weekend('Monday'))
# print(is_weekend('pizza'))




# # Modules - 5:02:14

# # Module = A file containing code you want to include in your program which you use the `import` keyword to reference. A Module can be built into Python, downloaded from a library or be built within and for the project itself. It's useful for breaking up a large program into reusable, separate files, same as in JavaScript.

# # You can do `print(help('modules'))` to see the comprehensive list of Modules built into Python, and you can pass the name of the Module into the help Function to get the comprehensive list of all the Methods and Attributes of that particular Module with information about them, for instance `print(help('math'))`

# import math # Example importing a Module as itself
# import math as the_native_python_math_module # Example importing a Module as an alias, similar to how it can be done in JavaScript

# pi = the_native_python_math_module.pi # Accessing the Attributes and Methods of a Module is done with the dot notation same as in JavaScript

# print(pi)

# from math import pi # You can deliberately import only some of the Methods or Attributes from a Module, similar to how it can be done in JavaScript, like this

# print(pi)


# import example_module # Consider the `example_module` (which is in the same directory as this file). Unlike how it's done in JavaScript, Modules in Python are inherently exported, i.e. they don't need to have anything exported from them. Rather, everything in them is already available. Side note, even if there's no `help` Function included in a Module, as is the case with `example_module`, Python's built-in `help` Method even provides some useful info for it

# print(example_module.pi)
# print(example_module.square(6))
# print(example_module.cube(3))
# print(example_module.circumference(3))
# print(example_module.area(5))




# # Variable Scope and Scope Resolution - 5:08:50

# # Variable Scope = Where in a project or program a Variable is visible and accessible
# # Scope Resolution = LEGB Rule, i.e. Local -> Enclosed -> Global -> Built-in, which means that Python will first look for the Variable within the Local Scope, then any Enclosed Scope, then the Global Scope, and lastly the Built-in Scope. This means you can override Python's built-in Variables with your own Variables, which is obviously not recommended, but is possible.

# from math import pi # If you were to import `pi` from Python's native `math` Module...
# pi = 123 # ...you could overwrite it with a Global Variable...
# print(pi)

# def pi_printer(): # ...with an Enclosed Variable...
#     pi = 456
#     print(pi)

# pi_printer()

# def pi_printer(): # ...or with a Local Variable
#     pi = 456
#     def pi_printer_local():
#         pi = 789
#         print(pi)
#     pi_printer_local()


# pi_printer()




# # Main Guards aka Main Checks  - 5:14:23

# # Main Guard aka Main Check = A conditional Statement used to determine whether a Python script is being run as the main program or if it is being imported as a Module into another script. It's able to do this because every Python Module has a special built-in Variable called `__name__`. When a Module is run directly the `__name__` Variable is set to '__main__'. When a Module is imported into another Module the `__name__` Variable is set to the Module's name. It's important to have in Python scripts because it leaves no Global Variables, i.e. avoids polluting the Global namespace, keeping the Global Scope clean and reducing the risk of Variable name conflicts, making the Module safer to import and use, and avoids unintended execution. The check is read "If Dunder name equals Dunder main" and is written `if __name__ == '__main__'`.

# # Imagine you have a Module called `my_module.py`...
# def primary(): # ...with a Function called `primary`...
#     print('This is the main function.')

# def secondary(): # ...and a Function called `secondary`...
#     print('This is a secondary function.')

# if __name__ == '__main__': # ...and you were to call the `primary` Function under the condition that Dunder name must equal Dunder main, if you were to do `python3 my_module.py` in Terminal you'd get the printed Statement "This is the main function", but if you were to import `my_module.py` into this file and do `python3 brocode.py` you'd get "This is the secondary function"
#     primary()
# else:
#     secondary()




# # Banking Program - 5:23:36

# def show_balance():
#     print(f'Your balance is {balance:.2f}') # The `balance` Variable is defined further down in the script, which is fine

# def deposit():
#     amount = input('Enter an amount to be deposited: ')
#     if amount.isdigit:
#         amount = int(amount)
#         if amount < 0:
#             print('That is not a valid amount')
#             return 0 # Even though an amount isn't "returned" from this condition (and from the similar conditions in the withdraw Function) a 0 must be returned because of how the `deposit` Function is being used in the Match Case Statement wherein it's called, otherwise you'd get a TypeError at case 2 of the Match Case Statement
#         else: 
#             return amount

# def withdraw():
#     amount = input('Enter an amount to be withdrawn: ')
#     if amount.isdigit:
#         amount = int(amount)
#         if amount < 0:
#             print('That is not a valid amount')
#             return 0
#         elif amount > balance:
#             print('Insufficient funds')
#             return 0
#         else: 
#             return amount


# def main(): # Wrap the program in a main Function

#     while is_running:
#         print('Banking Program\n1. Show Balance\n2. Deposit\n3. Withdraw\n4. Exit')

#         choice = int(input('Enter your choice (1-4): ')) # I'm Type Casting user input as an Integer, which is not necessary but I'm doing this because I want Integers as the cases in my Match Case Statement

#         match choice:
#             case 1: 
#                 show_balance()
#             case 2:
#                 balance += deposit()
#             case 3:
#                 balance -= withdraw()
#             case 4:
#                 print('Exiting')
#                 is_running = False
#             case _:
#                 print('Not a valid choice')

# balance = 0 # In Python Global Variables can be declared anywhere in the script. Unlike JavaScript, Python doesn't actually "hoist" variables. Instead Python reads the entire script before running it, so it knows about all Global Variables regardless of where they are declared. However you must define Global Variables before using them in your code to avoid errors. If a Global Variable is used in the main Function the main Function call must come after the Variable is defined. So the `balance` Variable can be declared after its use in the `show_balance` Function but the call to the main Function, the Function that calls the `show_balance` Function, must come after the `balance` Variable is defined.

# is_running = True

# if __name__ == '__main__': # Place a Main Guard on the program to ensure it runs only when executed directly
#     main()




# # Slot Machine Program - 5:38:37

# import random

# def spin_row():
#     symbols = ['🍒', '🍉', '🍋', '🔔', '⭐️']

#     results = [ random.choice(symbols) for _ in range(3) ] # This List Comprehension automatically selects 3 random elements from the `symbols` List. The `_` is a throwaway Variable since its value is not needed in the loop

#     # results = [] # The alternative would have been to have made an empty List...
#     # for symbol in range(3): # ...and to have used a For Loop to iterate over a range of 3...
#     #     results.append(random.choice(symbols)) # ...appending the results of the random choice of `symbols` to the List...
#     return results # ...and then returning the List

# def print_row(row): # Define a Function to print the `row`
#     print('------------')
#     print(' | '.join(row))
#     print('------------')

# def get_payout(row, bet): # Define a Function to get the payout
#     if row[0] == row[1] == row[2]: # If all three elements in the `row` are the same...
#         if row[0] == '🍒': # ...and if that element is a cherry...
#             return bet * 3 # ...return the bet times 3, and incrementally do the same for the other symbols with times 7 as the default...
#         elif row[0] == '🍉':
#             return bet * 4
#         elif row[0] == '🍋':
#             return bet * 5
#         elif row[0] == '🔔':
#             return bet * 6
#         else:
#             return bet * 7
#     else:
#         return 0 # ...but if the symbols don't match return a zero payout


# def main():
#     balance = 100 # Initial balance is 100
#     print('Welcome to Slot Machine Program') 
#     print('Symbols:' '🍒 🍉 🍋 🔔 ⭐️')

#     while balance > 0:
#         print(f'Current balance: {balance}') # Print the current balance

#         bet = input('Place your bet amount: ') # Prompt the user for a bet amount

#         if not bet.isdigit(): # If the `bet` is not a digit...
#             print('Your bet must be a number') # ...print this...
#             continue # ...and continue (note the `continue` Statement must be used to skip the rest of the loop and prompt the user for input again)

#         bet = int(bet) # Type Cast the valid digit as an Integer
        
#         if bet > balance: # If the `bet` is greater than the `balance`, indicate that there are insufficient funds 
#             print('Insufficient funds')
#             continue

#         if bet <= 0: # If the `bet` is less than or equal to zero, indicate as such
#             print('Bet must be greater than 0')
#             continue

#         balance -= bet # If those 3 initial checks pass, subtract the `bet` from the `balance`...

#         row = spin_row() # ...spin the r`ow`...
#         print('Spinning') 
#         print_row(row) # ...print the `row`...
#         payout = get_payout(row, bet) # ...and get the `payout`

#         if payout > 0:
#             print(f'You won {payout:.2f}')
#         else:
#             print('Sorry you lost this round')

#         balance += payout

#         play_again = input('Do you want to spin again? (Y/N): ').upper() # ...you could also use `capitalize` instead of `upper` to capitalize the first letter of the input, since the user is only answering with a single letter

#         if play_again != 'Y':
#             break

#     print(f'Game over! Your final balance is {balance}')

# if __name__ == '__main__':
#     main()




# # Substitution Cipher Encryption Program - 5:58:46

# import random
# import string

# chars_string = string.punctuation + string.digits + string.ascii_letters + ' ' # Create a String of all the characters we want to use in the substitution cipher, which we can do by using Python's built-in String Module which has a `punctuation` Attribute, a `digits` Attribute, and an `ascii_letters` Attribute (this is something that JavaScript doesn't have built-in) and finally add a whitespace character (note, there is also a `whitespace` Attribute but it includes a carriage return, which we don't want)

# chars_list = list(chars_string) # Type Cast the String of characters to a List of characters

# key_list = chars_list.copy() # Create an identical copy of the List of characters, which we have to do using the `copy` Method of the List Object because if we were to just set `key_list` equal to `chars_list` it would merely be a reference to the same List Object and any changes to one would affect the other

# random.shuffle(key_list) # Shuffle the key List of characters

# plain_text = input('Enter a message to encrypt: ')
# cipher_text = ''

# for char in plain_text:
#     index_of_char = chars_list.index(char)
#     cipher_text += key_list[index_of_char]

# print(cipher_text)


# encrypted_text = input('Enter a message to decrypt: ')
# plain_text = ''

# for char in encrypted_text:
#     index_of_char = key_list.index(char)
#     plain_text += chars_list[index_of_char]

# print(plain_text)




# # Hangman Game Program - 6:07:26

# import random

# words = ('apple', 'orange', 'banana', 'coconut', 'pineapple') # This is a Set of `words`

# hangman_art = { # This is a Dictionary where each pair contains a number and a Tuple, where the Tuple contains a sequence of Strings
#     0: (
#         '   ',
#         '   ',
#         '   '
#         ),
#     1: (
#         ' o ',
#         '   ',
#         '   '
#         ),
#     2: (
#         ' o ',
#         ' | ',
#         '   '
#         ),
#     3: (
#         ' o ',
#         '/| ',
#         '   '
#         ),
#     4: (
#         ' o ',
#         '/|\\',
#         '   '
#         ),
#     5: (
#         ' o ',
#         '/|\\',
#         '/  '
#         ),
#     6: (
#         ' o ',
#         '/|\\',
#         '/ \\'
#         )
# }


# def display_man(wrong_guesses):
#     for line in hangman_art[wrong_guesses]:
#         print(line)

# def display_answer_or_hint(answer_or_hint):
#     print(' '.join(answer_or_hint))  # This is a Pythonic way to join the elements of a List into a String, where the String you want to use to join the elements is placed before the `join` Method and the List whose elements you want to join is placed inside the parentheses of the `join` Method, so this is equivalent to `join(' ')` in JavaScript

# def display_guessed_letters(guessed_letters):
#     displayed_guessed_letters = ', '.join(guessed_letters)
#     return displayed_guessed_letters

# def main():
#     answer = random.choice(words)
#     hint = ['_'] * len(answer) # `['_' for x in range(1, len(answer) + 1)]` is how you would use a List Comprehension to create a List of underscores the same length as the answer, but that's not how we'll handle this because we want to demo how to multiply a List by a number to create a List of that many elements, and also to demo how the `join` Method works (featured in the `display_answer_or_hint` Function)
#     num_of_wrong_guesses = 0
#     guessed_letters = set() # You must initialize an empty Set to store the `guessed_letters`
#     is_running = True

#     while is_running:
#         display_man(num_of_wrong_guesses)
#         display_answer_or_hint(hint)
#         guess = input('Enter a letter: ').lower()

#         if len(guess) != 1 or not guess.isalpha(): # If the `guess` is not a single letter or if the `guess` is not a letter at all, indicate as such and continue
#             print('Please enter a letter and make it only one letter')
#             continue

#         if guess in guessed_letters: 
#             print(f'You already guessed {guess}. (Your guessed letters are {display_guessed_letters(guessed_letters)})')

#         if guess in answer: # If the `guess` is in the answer...
#             for i in range(len(answer)): # ...iterate over the letters in the `answer` with a For Loop set to the length of characters in the `answer`...
#                 if answer[i] == guess: # ...using Python's built-in interpretation of Strings as Lists, if the character at the index in question is equal to the `guess`...
#                    hint[i] = guess # ...set the character at the index of the `hint` to the `guess`...
#         else: # ...otherwise...
#             if guess not in guessed_letters: # ...if the `guess` is not in the Set of guessed letters...
#                 num_of_wrong_guesses += 1 # ...increment the `num_of_wrong_guesses` by 1...
#                 if num_of_wrong_guesses == len(hangman_art): # ...and if the `num_of_wrong_guesses` is equal to the length of the `hangman_art` Dictionary, indicate that the user has lost the game and stop the game from running...
#                     print('You lost!')
#                     display_answer_or_hint(answer)
#                     is_running = False

#         guessed_letters.add(guess) # ...otherwise add the `guess` to the Set of guessed letters...

#         if hint == list(answer): # ...if the `hint`, which is a List, is equal to the `answer` converted to a List (via Type Casting), indicate that the user has won the game and stop the game from running
#             is_running = False
#             print(f'Congrats you got it! The words was "{answer}"')


# if __name__ == '__main__': 
#     main()




# # Object Oriented Programming - 6:32:36

# # Object = A "bundle" of related Attributes (Variables) and Methods (Functions), example: phone, cup, book. You need a Class to create multiple Objects, Class Instances, that all share that Class's structure and Methods.

# # Class = A blueprint used to design the structure and layout of an Object or Objects.

# # Method = A Function that is associated with a Class, i.e. belongs in an Object.

# class Car: # A Class is defined with the keyword `class` followed by the name of the Class, which is capitalized by convention
#     def __init__(self, model, year, color, for_sale): # This "Dunder Method", which is required to create Objects, is the Constructor Method of the Class, and to assign the Attributes that come after `self` we have to access `self` with `.` much like how Classes in JavaScript are constructed but using `self` instead of `this`...
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

#     def drive(self):
#         print(f'You drive the {self.color} {self.model}')

#     def stop(self):
#         print(f'You stop the {self.color} {self.model}')

#     def describe(self):
#         print(f'This is a {self.color} {self.model} from {self.year}')

#     # ...and since Classes take up a lot of space it's often convention for them to be defined in a separate file, then imported into the main file like `from <name of file containing the Class> import <name of Class>`, and then the Objects are created in the main file from that imported Class

# car1 = Car('Mustang', '2024', 'Red', False) # `self` is provided for use behind the scenes automatically, so in order to create the `car1` Object from the `Car` Class we simply call the `Car` Class like a Function and pass in the Arguments that the Constructor Method requires, which in this case is the `model`, `year`, `color`, and `for_sale` Attributes, to create the `car1` Object

# print(car1) # If we try and print this `car1` Object we'll get a memory address, which is the default behavior unless the __str__ Method in the Class from which the Object was created is defined, in which case `print` will return whatever is specified by that Method...

# print(car1.model) # ...but if we print any of the Attributes of the `car1` Object, e.g. `model`, we'll correctly get those Attributes

# car2 = Car('Corvette', 2025, 'blue', True)
# car3 = Car('Charger', 2026, 'yellow', True)

# print(car3.describe())




# # Class Variables - 6:44:50

# # Class Variables = Variables that are shared among all Instances of a Class, are defined outside of any Method in the Class, and allow you to share data among all Objects created from that Class (namely, they are Static Variables).

# class Student:

#     graduation_year = 2024 # `graduation_year` and `num_of_students` are Class Variables because they are defined outside of any Instance Methods so are shared among all Instances of the Class
#     num_of_students = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#         Student.num_of_students += 1 # Knowing that any code inside our Constructor, i.e. this "Dunder init" part, is executed every time we instantiate an Object with the Class in question, we can add this Method that keeps track of the number of students (it does so by simply incrementing `num_of_students` by 1 each time a new Object is created), and to do this we have to maintain `num_of_students` inside the Class itself, i.e. as a Class Variable, not within `self`, i.e. not an Instance Variable

# student1 = Student('Spongebob', 30)
# student2 = Student('Patrick', 35)
# student3 = Student('Squidward', 55)
# student4 = Student('Sandy', 27)

# print(student1.name)
# print(student1.age)

# print(Student.graduation_year) # This is how you access a Class Variable directly, by using the Class name followed by a dot and the name of the Class Variable

# print(student1.graduation_year) # This is how you access a Class Variable through an Object. However, it is generally recommended to access or modify Class Variables directly through the Class itself to avoid confusion and maintain clarity.

# print(f'My graduating class of {Student.graduation_year} has {Student.num_of_students}')




# # Class Inheritance - 6:53:06

# # Class Inheritance = Allows a Class to inherit Attributes and Methods from another Class. This helps with code reusability and extensibility. It's performed by doing `class Child(Parent)` where the Child is also referred to as the Subclass and the Parent is known as the Superclass.


# class Animal:
#     def __init__(self, name, diet):
#         self.name = name
#         self.diet = diet
#         self.is_alive = True
    
#     def eat(self):
#         return f'{self.name} eats {self.diet}'

#     def sleep(self):
#         return f'{self.name} is asleep'


# class Dog(Animal): # Here the `Dog` Class inherits all the Attributes and Methods of the `Animal` Class without adding anything new to itself, and because Class is a Function and in this case there are no other Attributes or Methods to add you have to use the `pass` keyword to avoid a syntax error
#     pass


# class Cat(Animal): # Here the `Cat` Class inherits all the Attributes and Methods of the `Animal` Class but adds a Method called `think` which its Parent Class doesn't have
#     def think(self):
#         return f'{self.name} is thinking!!'


# class Mouse(Animal):
#     def __init__(self, name, diet, color): # Here the `Mouse` Class inherits all the Attributes and Methods of the` Animal` Class but adds an Attribute called `color`, and in order to add an Attribute that must happen through the `__init___` Method, meaning you have to override that entire Method...
#         super().__init__(name, diet) # ...and to do that you have to call the Parent Class's Constructor Method with the `super` Function, which is a built-in Python Function that returns a temporary Object of the Superclass which allows you to call the Superclass's Methods, so you pass in the Attributes that the Parent Class's Constructor Method requires...
#         self.color = color # ...and then add the new Attribute called `color`

#     def speak(self):
#         return f'{self.name} can speak!!'


# dog = Dog('Scooby', 'Snacks')
# cat = Cat('Garfield', 'Lasagna')
# mouse = Mouse('Mickey', 'Watermelon', 'Black')


# def tell_me_about_this_animal(animal):
#     print(animal.name)
#     print(animal.diet)
#     print(animal.is_alive)
#     print(animal.eat())
#     print(animal.sleep())
#     if animal == cat:
#         print(animal.think())
#     if animal == mouse:
#         print(animal.speak())
#         print(animal.color)


# tell_me_about_this_animal(dog)
# tell_me_about_this_animal(cat)
# tell_me_about_this_animal(mouse)




# # Multiple vs Multilevel Inheritance - 7:00:02

# # Multiple Inheritance = Inherit from more than one Parent Class, like `class Child(Parent1, Parent2)`.

# # Multilevel Inheritance = Inherit from a Parent which inherits from another Parent, like `class Child(Parent2) <- Parent2(Parent1) <- Parent1`.

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         return f'{self.name} is eating'

#     def sleep(self):
#         return f'{self.name} is sleeping'


# class Predator(Animal):
#     def hunt(self):
#         return f'{self.name} is hunting'

# class Prey(Animal):
#     def flee(self):
#         return f'{self.name} is fleeing'

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Predator, Prey): # `Fish` inherits from both the `Predator` and the `Prey` Classes
#     pass

# rabbit1 = Rabbit('Bugs')
# hawk1 = Hawk('Tony')
# fish1 = Fish('Nemo')

# print(fish1.hunt()) # You can call the `hunt` Method on Objects instantiated with the `Fish` Class, which `Fish` inherits from `Predator`...
# print(fish1.flee()) # ...or the `flee` Method on Objects instantiated with the `Fish` Class, which `Fish` inherits from `Prey`

# # Recap: With Multiple Inheritance you inherit from more than one Parent by simply adding that additional Class to the inheritance list, in this example adding both the `Predator` and `Prey` Classes to the `Fish` Class

# print(hawk1.eat()) # You can call the `eat` Method on Objects instantiated with the `Hawk` Class, because the `Hawk` Class inherits the `eat` Method from the `Animal` Class...
# print(rabbit1.sleep()) # ...or you can call the `sleep` Method on Objects instantiated with the `Rabbit` Class, because the `Rabbit` Class inherits the `sleep` Method from the `Animal` Class

# # Recap: With Multilevel Inheritance you inherit from a Parent which inherits from another Parent, in this case the `Predator` and `Prey `Classes both inherit the `eat` and `sleep` Methods from the `Animal` Class, then the `Rabbit`, `Hawk` and `Fish` Classes all inheriting those Methods from the `Predator` and `Prey` Classes




# # The Super Function - 7:08:04

# # super() = A Function used in a Child Class to call Methods from a Parent Class, also known as the Superclass. It allows you to extend the functionality of inherited Methods. Within a Child Class, you can use it in a Constructor to assign Attributes common to all siblings, and in other Methods to call the Parent Class's method of the same name, which is useful for adding to the functionality of a Parent Class's Method without replacing it.

# from math import pi

# # Here we have four Classes: `Shape`, `Circle`, `Square` and `Triangle`...

# class Shape:  # ...and the ones after this `Shape` Class all share the `color` and `is_filled` Attributes...
#     def __init__(self, color, is_filled): # ...so we can set up the Constructor Function of the `Shape` Class to take the `color` and `is_filled` Attributes...
#         self.color = color
#         self.is_filled = is_filled

#     def describe(self):
#         return f'It is {self.color} and {'filled' if self.is_filled else 'unfilled'}'

# class Circle(Shape): # ...then make a `Circle` Class which inherits the `Shape` Class...
#     def __init__(self, color, is_filled, radius): # ...set up its Constructor Function to take the `Shape` Class's `color` and `is_filled` Attributes, as well as a unique radius Attribute...
#         super().__init__(color, is_filled) # ...and finally use the `super` Function to call the Constructor Function of the `Shape` Class, i.e. the Parent Class aka the Superclass, to pass in the `color` and `is_filled` Attributes...
#         self.radius = radius

#     def describe(self): # ...the `Circle` Class has access to the `Shape` Class's `describe` Method and, though a `describe` Method would be useful, the one inherited from the `Shape` Class isn't very useful so we can simply override it...
#         return f'It is a {self.color}, {'filled' if self.is_filled else 'unfilled'} circle with an area of {self.radius ** 2 * pi}' # ...and here we're using the `radius` Attribute to calculate the area of the circle

# class Square(Shape): # Similarly we make a `Square` Class which inherits the `Shape` Class...
#     def __init__(self, color, is_filled, width): # ...set up its Constructor Function to take the `Shape` Class's `color` and `is_filled` Attributes, as well as a unique `width` Attribute...
#         super().__init__(color, is_filled)
#         self.width = width

#     def describe(self):  # ...the `Square` Class has access to the `Shape` Class's `describe` Method and, though a `describe` Method would be useful, the one inherited from the `Shape` Class isn't perfectly useful so though we could simply override it like we did in the `Circle` class, the gist of this lesson is how to use the `super` Function and, in addition to using it to inherit the `__init__` Method, we can use the `super` Function to modify Functions like the inherited `describe` Method so for example's sake let's modify it...
#         return f'{super().describe()} and it\'s got a width/height of {self.width}'

# class Triangle(Shape): # Similarly we make a `Triangle` Class which inherits the `Shape` Class...
#     def __init__(self, color, is_filled, width, height): # ...set up its Constructor Function to take the `Shape` Class's `color` and `is_filled` Attributes, as well as unique `width` and `height` Attributes...
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height

#     def describe(self): # ...the `Triangle` Class has access to the `Shape` Class's `describe` Method and, though a `describe` Method would be useful, the one inherited from the `Shape` Class isn't perfectly useful to the `Triangle` Class so we could simply override it like we did in the `Circle` Class or simply modify it like we did for the `Square` Class and since this is a lesson on the usefulness of the `super` Function let's do the latter again
#         return f'{super().describe()} and it\'s got an area of {self.width * self.height / 2}'


# # Now we can create Objects from the `Circle`, `Square` and `Triangle` Classes and, for better readability we can even make the Arguments passed to them Keyword Arguments...
# circle1 = Circle(color='red', is_filled=True, radius=5)
# square1 = Square(color='blue', is_filled=False, width=6)
# triangle1 = Triangle(color='green', is_filled=True, width=7, height=8)

#  # ...and finally print out the Attributes of the Objects to make sure they were set correctly
# print(f'Our circle1\'s color is {circle1.color}, it\'s {'filled' if circle1.is_filled else 'unfilled'} and it\'s radius is {circle1.radius}\n')

# print(f'Our square1\'s color is {square1.color}, it\'s {'filled' if square1.is_filled else 'unfilled'} and it\'s width/height are {square1.width}\n')

# print(f'Our triangle1\'s color is {triangle1.color}, it\'s {'filled' if triangle1.is_filled else 'unfilled'} and it\'s width and height are {triangle1.width} and {triangle1.height}, respectively\n')

# print(f'Our circle1 is described as: "{circle1.describe()}"')

# print(f'Our square1 is described as: "{square1.describe()}"')

# print(f'Our triangle1 is described as: "{triangle1.describe()}"')




# # Polymorphism with Class Inheritance - 7:21:10

# # Polymorphism = Greek word that means "to have many forms or faces". Poly means "Many", Morph means "Form". In Python, and in programming in general, it refers to Methods/Functions/Operators with the same name that can be executed on many Objects or Classes (an example of a Python Function that can be used on different Objects is the `len` Function) and it can be achieved through Class Inheritance, as delineated in this lesson, or though Duck Typing, as explained in the next lesson.

# from math import pi
# from abc import ABC, @abstractmethod # `ABC` stands for Abstract Base Class, which is a Python Module that provides the infrastructure for defining Abstract Base Classes (ABCs) in Python, and the `@abstractmethod` Decorator is used to define an Abstract Method in an Abstract Class, which is a Class that cannot be instantiated and is designed to be Subclassed


# class Shape: # This is only to show that the `Shape` Class is an Abstract Base Class, which is a Class that cannot be instantiated and is designed only to be Subclassed...
#     @abstractmethod # ...and this is how you define an Abstract Method in an Abstract Class
#     def area(self):
#         pass


# class Circle(Shape): # This is simply another example of Class inheritance
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return pi * self.radius ** 2
    

# class Square(Shape): # This is simply another example of Class inheritance
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2


# class Triangle(Shape): # This is simply another example of Class inheritance
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5


# class Pizza(Circle): # This is another example of Class inheritance, but also an example of Multilevel Class Inheritance...
#     def __init__(self, topping, radius):
#         super().__init__(radius) # ...as well as use of the `super` Function to get the `area` Method from the `Circle` Class
#         self.topping = topping


# # `circle1`, `square1` and `triangle1` all have the `Shape` Class in common...
# circle1 = Circle(2)
# square1 = Square(1.5)
# triangle1 = Triangle(3, 4)

# shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza('cheese', 8)] # ...and knowing this we can create a List of Class Instantiations and give it the name `shapes`

# # This is simply my generic helper Function to return the Class name and Properties to help with my example
# def get_instance_info(instance):
#     class_name = instance.__class__.__name__
#     properties = vars(instance)
#     return f'{class_name} Properties: {properties}'

# for shape in shapes: # We can iterate over the `shapes` List...
#     print(shape.area()) # ...calling the `area` Method on each `shape`, which is an example of Polymorphism because though `shapes` all have the `area` Method in common it's implemented differently in each Class (except for `Pizza` Class which directly inherits the `area` Method from the `Circle` class)...
#     print(get_instance_info(shape)) # ...and just to show the unique Properties of each `shape` we can call the `get_instance_info` Function on each `shape`




# # Polymorphism with Duck Typing - 7:29:15

# # Duck Typing = Another way to achieve Polymorphism besides Class Inheritance. Object must have the minimum necessary Attributes and/or Methods to be used in a certain context, like the adage "if it walks like a duck and quacks like a duck, then it must be a duck".

# class Animal:
#     alive = True

# class Dog(Animal):
#     def favorite_quote(self):
#         return 'Woof'

# class Cat(Animal):
#     def favorite_quote(self):
#         return 'Meow'

# class Car:
#     def favorite_quote(self):
#         return 'Honk'

# animals = [Dog(), Cat(), Car()] # As an aside, because we don't have necessary Attributes required for either of these Classes we don't need to pass any Arguments to either of the Classes in this List in order to instantiate them

# for animal in animals: # We can simply loop through the List of instantiated Classes...
#     print(animal.favorite_quote()) # ...and call the `favorite_quote` Method, and if we were to stop there we might think that a `Car` is also an `Animal` (i.e. "if it walks like a duck and quacks like a duck, then it must be a duck")...

# for animal in animals: # ...until we try it again...
#     print(animal.favorite_quote())
#     print(animal.alive) # ...this time printing the `alive` Attribute, which is only present in the `Animal` Class, and discover we get the error "AttributeError: 'Car' object has no Attribute 'alive'" then learning that the `Car` Class doesn't have the minimum necessary Attributes and/or Methods to be used in the context of the `Animal` Class, so it's not an `Animal`, even though it shares the `favorite_quote` Method with both the `Dog` and `Cat` Classes (note, if we were to simply set an `alive` Attribute directly in the `Car` Class and make it `False` the `Car` Class, according to Duck Typing, would then technically classify as being also in the `Animal` Class)




# # Static Methods vs Instance Methods - 7:33:34

# # Static Method = A Method that belongs to a Class rather than to any Object from that Class, i.e rather than from any Class Instance. Static Methods do not require an Instance of the Class to be called and are typically used for operations that are relevant to all Instances of the Class or for utility Functions. Static Methods never have the `self` Parameter.

# # Instance Method = A Method that belongs to an Object from a Class, i.e. from a Class Instance. Instance Methods require an instance of the Class to be called and can access and modify the Attributes of the Instance. Instance Methods always have the `self` Parameter.

# class Employee:

#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def get_info(self): # `get_info` is an Instance Method because it takes the `self` Parameter, which is a reference to the Object that is calling the Method
#         return f'{self.name} = {self.position}'

#     @staticmethod # Static Methods take the `@staticmethod` Decorator, a built-in Python Decorator that is used to define a Static Method...
#     def is_valid_position(position): # ...and they don't take the `self` Parameter, meaning they don't have access to the Object's Attributes, thus are used for operations shared by all Instances of the Class
#         valid_positions = ['Manager', 'Cashier', 'Cook', 'Janitor']
#         return position in valid_positions

# # Because Static Methods don't have access to any Instance-specific data you can simply call the Class itself followed by a dot and the name of the Static Method. The Arguments passed to the Static Method can come from anywhere including Instances of the Class, but it's not required.
# is_cook_a_valid_position = Employee.is_valid_position('Cook')
# is_rocket_scientist_a_valid_position = Employee.is_valid_position('Rocket Scientist')

# print(f'It is {is_cook_a_valid_position} that a Cook is a valid position')
# print(f'Is is {is_rocket_scientist_a_valid_position} that a Rocket Scientist is a valid position')

# employee1 = Employee('Eugene', 'Manager')
# employee2 = Employee('Squidward', 'Cashier')
# employee3 = Employee('Spongebob', 'Cook')

# # To call an Instance Method we have to access one of the Instances of the Class in order to use it...

# # ...so to get the employee info on `employee1`, `employee2` and `employee3` we have to access the `get_info` Method on those Instances of the Employee Method
# print(f'{employee1.get_info()}')
# print(f'{employee2.get_info()}')
# print(f'{employee3.get_info()}')

# # Recap: For an Instance Method you must access it through an Object created from a Class, whereas for a Static Method you can access it directly from the Class and don't even need to create any Object(s) from that Class




# # Class Method - 7:39:31

# # Class Methods = Methods that involve Class level data and allow operations related to the Class itself. They take `cls` as the first Parameter which represents the Class itself.

# class Student:

#     count = 0 # `count` and `total_gpa` are a Class Variables
#     total_gpa = 0

#     def __init__(self, name, gpa): # The Constructor Method has two Parameters, `name` and `gpa`, beyond the default `self` Parameter
#         self.name = name
#         self.gpa = gpa

#         Student.count += 1 # The Class Variable called `count` is incremented by 1 each time a new Object is created, which we can do here in the Constructor Method
#         Student.total_gpa += gpa # The Class Variable called `total_gpa` is incremented by the `gpa` of each new Object when one is created, which we can do here in the Constructor Method

#     def get_info(self): # `get_info` is an Instance Method (we know immediately because it takes the `self` Parameter)
#         return f'{self.name} has a GPA of {self.gpa}'

#     @classmethod # Class Methods like `get_count` take the `@classmethod` Decorator above them, a built-in Python Decorator that is used to define a Class Method, and rather than having `self` as the first Parameter they take `cls` as the first Parameter, representing the Class itself
#     def get_count(cls):
#         return f'Total number of students: {cls.count}'

#     @classmethod # `get_average_gpa` is also a Class Method
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f'The average GPA is: {cls.total_gpa / cls.count:.2f}'

# student1 = Student('Spongebob', 3.2)
# student1 = Student('Patrick', 2.0)
# student1 = Student('Sandy', 4.0)

# print(f'What is the total number of students? {Student.get_count()}')
# print(f'What is the average GPA? {Student.get_average_gpa()}')




# # Magic Methods - 7:46:17

# # Magic Methods = Dunder Methods (double underscore Methods) such as `__init__`, `__name__`, `__str__`, `__eq__`, typically found in Classes, which are automatically called using Python's built-in operations. They allow developers to define or customize the behavior of Objects.

# class Book:
#     def __init__(self, title, author, num_pages): # `__init__` is a Dunder Method that allows us to initialize an Object with the Attributes passed in (and it's required to create Objects)
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self): # `__str__` is a Dunder Method that allows us to return a String representation of the Object however we want to, rather than the default memory address, so that doing something like `print(book1)` will return the `title` and `author` of the book rather than something like `<__main__.Book object at 0x1025ad400>`
#         return f'{self.title} by {self.author}'

#     def __eq__(self, other): # `__eq__` is a Dunder Method that allows us to compare two Objects, in this case we're comparing the `title` and `author` of two books to see if they're the same, where the `other` Parameter is the other book (note we're not also comparing `num_pages` in this `__eq__` Magic Method because font sizes might be different between the two books, which would increase `num_pages` of what should be considered the same book)
#         return self.title == other.title and self.author == other.author

#     def __lt__(self, other): # `__lt__` is a Dunder Method that allows us to customize the behavior of the `<` Logical Operator, in this case we're comparing the `num_pages` between two books
#         return self.num_pages < other.num_pages

#     def __add__(self, other): # `__add__` is a Dunder Method that allows us to customize the behavior of the `+` Operator, in this case we're adding the `num_pages` of two books
#         return self.num_pages + other.num_pages

#     def __contains__(self, keyword): # `__contains__` is a Dunder Method that allows us to customize the behavior of the `in` Operator, in this case we're checking if a `keyword` is in the `title` of the book
#         return keyword in self.title

#     def __getitem__(self, key): # `__getitem__` is a Dunder Method that allows us to customize the behavior of the `[]` Operator, in this case we're getting the `title` of the book
#         if key == 'title':
#             return self.title
#         elif key == 'author':
#             return self.author
#         elif key == 'num_pages':
#             return self.num_pages
#         else:
#             return f'{key} not found'

# book1 = Book('The Hobbit', 'J.R.R. Tolkien', 310)
# book2 = Book('The Hobbit', 'J.R.R. Tolkien', 375) # `book2` is intentionally the same as `book1`, but with different `num_pages`, to demonstrate how our `__eq__` Dunder Method works
# book3 = Book('Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 223)
# book4 = Book('The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 172)

# print(book3) # The `title` and `author` of the book will be printed rather than the memory address because we used the `__str__` Dunder Method when creating the `Book` Class

# print(book1 == book2) # `True` will be printed because the Comparison Operator is using the `__eq__` Dunder Method in our `Book` Class, which compares the `title` and `author` of the two books, rather than `False`, which would otherwise happen because the memory addresses are different

# print(book4 < book3) # `True` will be printed because the Comparison Operator is using the `__lt__` Dunder Method in our `Book` Class, which compares the `num_pages` of the two books, rather than getting the error "TypeError: '<' not supported between instances of 'Book' and 'Book'"

# print(book3 + book4) # 395 will be printed because the `+` Operator is using the `__add__` Dunder Method in our `Book` Class, which adds the `num_pages` of the two books, rather than getting the error "TypeError: unsupported operand type(s) for +: 'Book' and 'Book'"

# print('Lion' in book4) # `True` will be printed because the word "Lion" is in the `title` of the book, which is checked by the `__contains__` Dunder Method in our `Book` Class, rather than getting the error "TypeError: argument of type 'Book' is not iterable"

# print(f'Title is: {book2['title']}, Author is: {book2['author']}, Number of Pages are: {book2['num_pages']}, Pizza: {book2['pizza']}') # We get "Title is: The Hobbit, Author is: J.R.R. Tolkien, Number of Pages are: 375, Pizza: pizza not found" because the `[]` Operator is using the `__getitem__` Dunder Method in our `Book` Class, which gets the `key` passed to it and returns the appropriate assigned Attribute, rather than getting the error "TypeError: 'Book' object is not subscriptable"




# # @property Decorator - 7:59:52

# # @property Decorator = The built-in Python `@property` Decorator is used to define a Method as a Property, meaning it can be accessed like an Attribute, which gives the ability to add additional logic when reading, writing or deleting Attributes. It gives us a `getter` Method, a `setter` Method, and a `deleter` Method.

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width # Prefixing an Attribute with an underscore is a convention to indicate that it's a Private Attribute, meaning it should not be accessed externally, i.e from outside the Class (although it still can be)
#         self._height = height

#     @property # The `@property` Decorator can then be used to access a Private Attribute internally, i.e. from inside the Class, and to do something with it first...
#     def width(self): # ...so this `getter` Method of the `@property` Decorator, called `width`...
#         return f'{self._width:.1f}cm' # ..accesses the internal `_width` and returns it as a String with one decimal place

#     @property
#     def height(self):
#         return f'{self._height:.1f}cm'

#     @width.setter # Unlike the `getter` Method (demonstrated above) the `setter` Method must be deliberately called on the Property in question...
#     def width(self, new_width): # ...and we don't want the Parameter name passed to this `width` Method to be the same as the Method name, `width`, that's the only reason we're naming it to something different, i.e `new_width`...
#         if new_width > 0:
#             self._width = new_width
#         else: # ...so now if a user were to instantiate an Object from `Rectangle`, called `rectangle1`, and then try to do `rectangle1.width = 0` to later set the `width` to 0 (or to try and set the `width` to a negative number) the `width` wouldn't set on their Instance of the `Rectangle` class, and instead they'd get this "Width must be greater than zero" message
#             print('Width must be greater than zero') 

#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print('Height must be greater than zero')
          
#     @width.deleter
#     def width(self): # ...no Parameters needed for the `deleter` Method...
#         del self._width # ...this deletes Private `_width`...
#         print('Width has been deleted') # ...but we can still print a confirmation

#     @height.deleter
#     def height(self):
#         del self._height
#         print('Height has been deleted') 


# rectangle1 = Rectangle(3, 4) # Now we can create an Object called `rectangle1` from the `Rectangle` Class with a `width` of 3 and a `height` of 4...

# rectangle1.width = 0 # ...try to later set the `width` to 0 and get the message from the `setter` Method that this won't work...

# rectangle1.width = 5 # ...then try to set the `width` to 5...

# print(rectangle1.width) # ...and print the `width` to see that it does indeed work, and also see that the `@property` Decorator has allowed us to change the raw Attributes...

# print(rectangle1._width) # ...but that we can still access the Attributes...

# del rectangle1.width # ...and finally that we can delete the Attributes...

# print(rectangle1.width) # ...as confirmed here when trying to print the `width` after it's been deleted, which should now throw "AttributeError: 'Rectangle' object has no attribute '_width'. Did you mean: 'width'?"




# # Decorators - 8:07:34

# # Decorator = A Function that extends the behavior of another Function without modifying the Base Function, by passing the Base Function as an Argument to the Decorator.

# def add_sprinkles(func):
#     def wrapper(*args, **kwargs): # The `wrapper` to call the Base Function is crucial to the Decorator Function otherwise the Base Function would be called as soon as we were to apply the Decorator and, if the Base Function takes any Arguments, the `wrapper` should be set up to take any number of Arguments or Keyword Arguments as demonstrated here
#         print('You added sprinkles') # This `wrapper` Function prints that sprinkles were added...
#         func(*args, **kwargs) # ...and then calls the Base Function
#     return wrapper # The Decorator Function returns the `wrapper` Function

# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print('You added fudge')
#         func(*args, **kwargs)
#     return wrapper


# @add_sprinkles # To apply the Decorator to a Function you simply put the `@` symbol followed by the name of the Decorator Function above the Function you want to decorate...
# @add_fudge
# def get_ice_cream(flavor):
#     print(f'Here is your {flavor} ice cream')

# get_ice_cream('vanilla') # ...so calling `get_ice_cream` won't just print "Here is your vanilla ice cream" it will print "You added sprinkles" "You added fudge" "Here is your vanilla ice cream"




# # Exceptions - 8:14:57

# # Exception = An event that interrupts the flow of a program, e.g. ZeroDivisionError, TypeError, ValueError, which you should use `try-except` blocks to handle.

# try:
#     number = int(input('Enter a number: ')) # Exceptions are particularly helpful when accepting user input, since you don't know what that input will be
#     print(1 / number) # In this case we're trying to divide 1 by the `number` the user inputs and, because we know if the user were to input zero that we'd get a ZeroDivisionError...
# except ZeroDivisionError: # ...we can use a `try-except` block to handle that...
#     print('You can\'t divide by zero')
# except ValueError: # ...and we can even chain Exceptions together...
#     print('Please enter only numbers')
# except Exception:  # ...after we've accounted for all the Exceptions we can anticipate we can use the Exception Class to catch all Exceptions (we could also make the entire `try-except` block consist of only this one Exception Class but this is generally not recommended)...
#     print('Something went wrong but it wasn\'t a ZeroDivisionError or a ValueError')
# finally: # ...and the `finally` block is always executed
#     print('The finally block is always executed and is usually used for a cleanup operation, e.g. closing a file or a database connection')




# # File and Folder Detection - 8:20:46

# import os

# file_path_for_test_txt = 'test_file.txt' # This is an example of a Relative File Path, a path relative to the directory from which the script is being run. It can be referenced with simply the file name and extension, not the `./` prefix as is the case in JavaScript. An Absolute File Path would look like `/Users/user-name/Desktop/file-name.extension`, in the event the file were on the user's macOS Desktop.

# if os.path.exists(file_path_for_test_txt): # The `exists` Method, built into Python's native `os.path` Submodule, returns a Boolean and you should make sure you pass the single Argument of the File Path to it otherwise it will return `True` because it would then be merely checking if the `exists` Method of the `os.path` Submodule exists
#     print(f'it exists and its path is {file_path_for_test_txt}')
#     if os.path.isfile(file_path_for_test_txt): # The `isfile` Method, which checks if the path is indeed a file and not a directory, which is also built into Python's native `os.path` Submodule, also returns a Boolean and you must pass the single Argument of the File Path to it otherwise it will return `True` because it would then be merely checking if the `isfile` Method of the `os.path` Submodule exists
#         print('moreover, its indeed a file, not a directory')
#     elif os.path.isdir(file_path_for_test_txt): # The `isdir` Method, which checks it the path is indeed a directory and not a file, which is also built into Python's native `os.path` Submodule, also returns a Boolean and you must pass the single Argument of the File Path to it, otherwise it will return `True` because it would then be merely checking if the `isdir` Method of the `os.path` Submodule exists
#         print('moreover, its actually a directory, not a file')

# else:
#     print(f'test.txt doesn\'t exist')




# # Writing `txt` Files - 8:27:47

# txt_str_data = 'I like pizza!!' # This is an example of a String of text data that we want to write to a `txt` file

# txt_name_list_data = ['Eugene', 'Squidward', 'Spongebob', 'Patrick'] # This is an example of a List of names that we want to write to a `txt` file, through which we'll have to loop in order to do so

# file_path = 'test_output.txt' # This is an example of a Relative File Path, i.e. a path relative to the directory from which the script is being run

# with open(file=file_path, mode='w') as file: # This is an example of how to write a `txt` file, where `mode` is set as a Default Argument to `w` for "write" and the file is opened with Python's native `open` Function, which takes the `file` (the File Path, as as a Default Argument in this example) and the `mode` as Arguments. The `with` Statement preceding the `open` Function is a context manager which facilitates closing the file when we're done so we don't have to worry about doing that manually. We don't need to specify the Arguments as Default Arguments, I'm just doing so for the example. The `open` Function returns a file Object, the first Parameter being the `file` (the File Path), the second Parameter being the `mode`, which can be set to `w`, `x`, `a` or `r`, where `x` will throw an error if the file already exists and `w` will work, regardless. The keyword `as` signifies instantiation of the Object which, in this case, is Python's built-in `file` Object (which just happens to be in lowercase, though it is indeed a Class)
#     file.write(txt_str_data)
#     for name in txt_name_list_data:
#         file.write('\n' + name)
#     print(f'txt file of {file_path} was created')


# try: # This demonstrates a `try-except` block with the `x` mode, which will knowingly throw the FileExistsError because the file already exists from the previous operation...
#     with open(file=file_path, mode='x') as file:
#         pass
# except FileExistsError: # ...but we can still append data to it if we want to do so here in the `except` block
#     with open(file=file_path, mode='a') as file:
#         file.write('\n' + txt_str_data)
#     print('...but we can still add more data to it if we want to here in the except block')




# # Writing `json` Files - 8:36:03

# import json # In order to write a `json` file we have to import Python's built-in `json` Module

# json_name_dictionary_data = { # This is an example of a Dictionary of data for which we had to import Python's built-in `json` Module in order to write it to a `json` file
#     'name': 'Spongebob',
#     'age': 30,
#     'job': 'cook'
# }

# file_path = 'test_output.json' # This is an example of a Relative File Path to a `json` file

# try:
#     with open(file_path, 'x') as file:
#         json.dump(json_name_dictionary_data, file, indent=4) # Use the `dump` Method of Python's built-in `json` Module to convert our Dictionary to a `json` String to output it, which takes two mandatory Arguments, the `json` Object and the File Path, and the optional `indent` Argument to signify by how many spaces to indent each key:value pair
#         print(f'json file {file_path} was created')
# except FileExistsError: # If the file already exists, indicate as such
#     print('That file already exists! Try again with the "w" mode instead of the "x" mode')




# # Writing `cvs` Files - 8:38:20

# import csv # In order to write a `csv` file we have to import Python's built-in `csv` Module

# csv_name_dictionary_data = [
#                                 ['Name', 'Age', 'Job'],
#                                 ['Spongebob', 30, 'Cook'],
#                                 ['Patrick', 37, 'Unemployed'],
#                                 ['Sandy', 30, 'Scientist']
#                             ]

# file_path = 'test_output.csv'

# try:
#     with open(file_path, 'x', newline='') as file: # Pass an empty String to the `newline` Argument to prevent the `writer` Method of Python's built-in `csv` Module from adding an extra newline character (which is the default) to the end of each row
#         writer = csv.writer(file) # Use the`writer` Method of Python's built-in `csv` Module to write to the `csv` file, which takes the file Object as an Argument
#         for row in csv_name_dictionary_data: # Loop through the data...
#             writer.writerow(row) # ...writing each row to the `csv` file...
#         print(f'csv file {file_path} was created') # ...printing a confirmation message...
# except FileExistsError: # ...and if the file already exists, indicate as such
#     print('That file already exists! Try again with the "w" mode instead of the "x" mode')




# # Reading `txt` Files - 8:41:35

# file_path = 'test_read.txt' # Here's a Relative File Path

# with open(file_path, 'r') as file: # Precede the `open` Function with the `with` context manager to facilitate closing the file after reading, because not closing a file after opening it is bad practice and can lead to instabilities, then pass the Relative File Path as `file_path` and `mode` as `r` to the `open` Function which returns a file Object, which we nickname simply as `file`...
#     content = file.read() # ...which returns one long String we can access with the `read` Method and save to a variable called `content`...
#     print(content) # ...then print it to the console


# file_path = 'nonexistent_file.txt' # For example's sake, in order to simulate the chance that a file couldn't be found, if we were to deliberately have a path to a file that doesn't exist...

# try: # ...we could use a `try-except` block to handle that...
#     with open(file_path, 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError: # ...knowing that the FileNotFoundError error is what would be thrown...
#     print(f'The file with path "{file_path}" doesn\'t exist')
# except PermissionError: # ...and if the file were to exist but didn't have read permissions we could also catch the PermissionError error
#     print(f'The file with path "{file_path}" isn\'t allowed to be read')




# # Reading `json` Files - 8:45:37

# import json # Import the `json` Module

# file_path = 'test_read.json' # Here's a Relative File Path

# with open(file_path, 'r') as file:
#     content = json.load(file) # Reading a `json` file is almost the same as reading a `txt` file except we have to use the `json` Module's `load` Method passing it the file Object returned by the `open` Function rather than the `read` Method from the file Object itself...
#     print(content)
#     print(content['word_4']) # ...and we can also access the data in the `json` file as we would a Dictionary


# file_path = 'test_read_bad_format.json' # Here's a Relative File Path

# try: # `json` files have their own unique errors for which we can wrap in `try-except` block...
#     with open(file_path, 'r') as file:
#         content = json.load(file)
#         print(content)
# except json.decoder.JSONDecodeError: # ...for instance if the `json` file is not formatted correctly
#     print(f'The file with path "{file_path}" is not formatted correctly')




# # Reading .csv Files - 8:46:44

# import csv # Import the `csv` Module

# file_path = 'test_read.csv' # Here's a Relative File Path

# with open(file_path, 'r') as file:
#     content = csv.reader(file) # Reading a `csv` file is almost the same as reading a `txt` file except we have to use the `csv` Module's `reader` Method passing it the file Object returned by the `open` Function rather than the `read` Method from the file Object itself...
#     print(content) # ...and printing that gives us a memory address because the way to read a `csv` file is line by line...
#     for line in content: # ...so we have to loop through each `line` in the `contents` of a `csv` file to access each line...
#         print(line)
#         print(line[2]) # ...within which we can also access a specified column within a row as we would access an element in a List




# # Dates and Times - 8:48:30

# import datetime # This native Python Module allows us to work with dates and times using our system clock

# date = datetime.date(2025, 1, 2) # Creating a Variable named `date` and calling the `date` Method on the `datetime` Module passing it a year, numeric month and numeric day...
# print(date) # ...gives us 2025-01-02

# today = datetime.date.today() # Creating a Variable named `today` and calling the `today` Method on the `date` Class of the `datetime` Module...
# print(today) # ...gives us the current date in the same YYYY-MM-DD format (note that `date` from `datetime` is a Class, not a Submodule as is `path` from the `os` Module)

# time = datetime.time(12, 30, 0) # Creating a Variable named `time` and calling the `time` Method on the `datetime` Module passing it the hours, minutes and seconds formats those Parameters like HH:MM:SS...
# print(time) # ...gives 12:30:00 in this example

# now = datetime.datetime.now() # Creating a Variable named `now` and calling the `now` Method on the `datetime` Class of the `datetime` Module...
# print(now) # ...gives us the current date and time in the YYYY-MM-DD HH:MM:SS format where the seconds are at six decimal places, i.e microseconds

# now = now.strftime('%H:%M:%S %m-%d-%Y') # `datetime` Objects have a `strftime` Method, which stands for "String format time", which allows us to format the date and time in a way that we want to see it, so here we can reassign our `datetime` Object called `now`, call the `strftime` Method on it and pass it a String of Format Specifiers to specify how we want the date and time to be formatted
# print(now)

# target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1) # Creating a Variable named `target_datetime` and calling the `datetime` Method on the `datetime` Module passing it a year, numeric month, numeric day, hours, minutes and seconds is done like this

# current_datetime = datetime.datetime.now() # Creating a Variable named `current_datetime` and calling the `now` Method on the `datetime` Class of the `datetime` Module is done like this

# if target_datetime < current_datetime: # An `if` Statement can compare them to see if the target date and time has passed
#     print('The target date and time has passed')
# else:
#     print('The target date and time has not passed')




# # Alarm Clock Program - 8:54:47

# import time
# import datetime
# import pygame # This Module allows us to work with sound effects. If it's not already installed try doing `pip3 install pygame`. If that doesn't work it's likely because `homebrew`, the unofficial package manager for macOS, is restricting it in which case you must install `pygame` in a virtual environment. The way to do this is to first create a virtual environment with `python3 -m venv <folder-name-for-virtual-environment>`, where `python3 -m venv venv` is usually the convention, which creates a new directory named `venv` containing the virtual environment. Then, in order to activate the virtual environment, do `source venv/bin/activate`. And finally, to install `pygame` in the virtual environment, do `pip3 install pygame`

# # Every time a `pygame` is imported it prints a message to the console "pygame 2.6.1 (SDL 2.28.4, Python 3.13.0) Hello from the pygame community. https://www.pygame.org/contribute.html", which is annoying. To to suppress that we have to go to the `venv` folder, find the ` lib/python3.13/site-packages/pygame/__init__.py` file and comment out the `if` Statement that begins with `if "PYGAME_HIDE_SUPPORT_PROMPT" not in os.environ`


# def set_alarm(alarm_time): # This is a Function that takes an `alarm_time` as an Argument...
#     print(f'Alarm set for {alarm_time}') # ...confirms the `alarm_time`...
#     sound_file = 'assets/rooster_crowing.mp3' # ...sets the `sound_file` to be played when the alarm goes off...

#     is_running = True # ...sets an `is_running` Boolean to `True`...

#     while is_running: # ...and while `is_running`...
#         current_time = datetime.datetime.now().strftime('%H:%M:%S') # ...gets the `current_time`...
#         print(current_time) # ...prints it...

#         if current_time == alarm_time: # ...and when the `current_time` equals the `alarm_time`
#             print('Wake up!! 😣😵‍💫') # ...prints "Wake up!! 😣😵‍💫"...

#             pygame.mixer.init() # ...initializes the `mixer` Class of the `pygame` Module...
#             pygame.mixer.music.load(sound_file) # ...passes the `sound_file` to the `load` Method of the `music` Class of the `mixer` Class of the `pygame` Module...
#             pygame.mixer.music.play() # ...calls the `play` Method of the `music` Class of the `mixer` Class of the `pygame` Module...

#             while pygame.mixer.music.get_busy(): # ...and, so the alarm doesn't stop playing immediately, calls the `get_busy` Method of the `music` Class of the `mixer` Class of the `pygame` Module to reference when the alarm is playing, and while it's playing...
#                 time.sleep(1) # ...sleeps for one second...

#             is_running = False # ...otherwise breaks out of the While Loop by setting `is_running` to False...

#         time.sleep(1) # ...otherwise if `current_time` does not equal `alarm_time` it sleeps for one second and loops back to the top of the While Loop


# if __name__ == '__main__': # Place a Main Guard on the program to ensure it runs only when executed directly
#     alarm_time = input('Enter the alarm time (HH:MM:SS): ')
#     set_alarm(alarm_time)




# # Multithreading  - 9:05:04

# # Multithreading = Is used to perform multiple tasks concurrently (multitasking), which is good for I/O bound tasks like reading files or fetching data from APIs, similar to `async/await` in JavaScript. It's used by accessing the `threading` Module and then calling the `Thread` Constructor on it and passing in the `target` Function. For example `threading.Thread(target=my_function)`.

# import threading # Import the `threading` Module
# import time # Import the `time` Module (to help us simulate a chore taking a specified amount of time to complete)

# def walk_dog():
#     time.sleep(8) # Make this Function take 8 seconds to complete
#     print('You finish walking the dog')

# def take_out_trash():
#     time.sleep(2) # Make this Function take 2 seconds to complete
#     print('You finish taking out the trash')

# def get_mail(location): # Make this Function take an Argument called `location` and take 4 seconds to complete
#     time.sleep(4) #
#     print(f'You finish getting the mail from {location}')

# # If you were to do...

# # walk_dog()
# # take_out_trash()
# # get_mail('Locust Street Post Office')

# # ...it would print...

# # You finish walking the dog
# # You finish taking out the trash
# # You finish getting the mail from Locust Street Post Office

# # ...with each chore taking 8, 2 and 4 seconds respectively, the total time to complete all three chores being 14 seconds because all three functions are running on the same Thread (the Main Thread)...

# # ...so to Multithread these...

# chore1 = threading.Thread(target=walk_dog) # ...create a new Thread called `chore1` and call the `Thread` Constructor on the `threading` Module passing in the `walk_dog` Function, which must be a Keyword Argument...
# chore1.start() # ...then call the `start` Method on the `chore1` Thread, then do the same for the `take_out_trash` and `get_mail` Functions...
# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()
# chore3 = threading.Thread(target=get_mail, args=('Locust Street Post Office',)) # ...and if the Function takes a Parameter, like this `get_mail` Function, you have to pass it as a Tuple to the `args` Parameter and, in order to correctly designate it as a Tuple, when there's only one `arg` you have to put a comma after the Parameter...
# chore3.start()

# chore1.join() # ...then call the `join` Method on each of the Threads to wait for them to finish before moving on to the next Thread...
# chore2.join()
# chore3.join()

# print('All chores are complete!') # ...and finally print "All chores are complete!", which will only print after all three Threads have finished running because the `join` Method was called on each of them...


# # This should print...

# # You finish taking out the trash
# # You finish getting the mail from Locust Street Post Office
# # You finish walking the dog
# # All chores are complete!

# # ...with each chore taking 2, 4 and 8 seconds respectively, completing in a different order than they were executed, where the total time to complete all three chores is merely equal to the time it takes to complete the longest chore (`walk_dog` of 8 seconds) because each chore is running on its own Thread




# # Connect to an API - 9:13:47

# import requests # See comments next to "import pygame" in the Alarm Clock Program lesson for how to install this `requests` Module, which installs the same way, and how to activate a virtual environment

# base_url = 'https://pokeapi.co/api/v2/' # Define the base URL for the API

# def get_pokemon_info(name): # Create a Function called `get_pokemon_info` that takes a `name` Parameter...
#     url = f'{base_url}/pokemon/{name}' # ...accordingly sets up the correct URL to use...
#     response = requests.get(url) # ...calls the `get` Method on the `requests` Module, passing it the `url` Parameter and assigns the response to a Variable called `response`...

#     if response.status_code == 200: # ...and, checking the `status_code` of the response, if it's 200, i.e. if it's successful...
#         pokemon_data = response.json() # ...calls the `json` Method on it to parse it as JSON and assigns that to a Variable called `pokemon_data`...
#         return pokemon_data # ...and returns that `pokemon_data`...
#     else: # ...otherwise...
#         print(f'Failed to retrieve data with {response.status_code} error') # ...prints that retrieving data failed


# pokemon_name = 'pikachu' # Define a `pokemon_name`...
# pokemon_info = get_pokemon_info(pokemon_name) # ...pass it to the `get_pokemon_info` Function and assign the response to a `pokemon_info` Variable...

# if pokemon_info: # ...and if info is returned the Properties of the response should be able to be printed according to the below `print` Statements...
#     print(f'The Pokemon\'s name is {pokemon_info['name'].capitalize()}')
#     print(f'The Pokemon\'s ID is #{pokemon_info['id']}')
#     print(f'The Pokemon\'s height is {pokemon_info['height']}')
#     print(f'The Pokemon\'s weight is {pokemon_info['weight']}')
# else: # ...otherwise...
#     print('There\'s no info to display') # ...it should "There's no info to display"




# # PyQt5 GUIs - 9:22:19

# import sys # `sys` is a built-in Python Module that provides access to some Variables used or maintained by the interpreter and to Functions that interact with the interpreter, and we'll use it to exit the application
# from PyQt5.QtWidgets import QApplication, QMainWindow # See comments next to "import pygame" in the Alarm Clock Program lesson for how to install this `PyQt5` Module, which installs the same way and from which we'll import the `QApplication` and `QMainWindow` Classes from the `QtWidgets` Submodule, and how to activate a virtual environment
# from PyQt5.QtGui import QIcon # We'll use the `QIcon` Class from the `QtGui` Submodule so that we can set the `window_icon`

# window_icon = 'assets/cool_image.png' # Define the `window_icon` with its Relative File Path

# class MainWindow(QMainWindow): # Create a Class called `MainWindow` that inherits from `QMainWindow`...
#     def __init__(self): # ...set up the Constructor...
#         super().__init__() # ...`super` is a built-in Python Function that returns a temporary Object of the Superclass that allows us to call the Superclass's Methods, and here we're calling the Superclass's `__init__` Method...
#         self.setWindowTitle('My cool first GUI') # ...set the window title with the `setWindowTitle` Method...
#         self.setGeometry(20, 210, 500, 300) # ...set the position and dimensions of the window with the `setGeometry` Method whose Parameters are x position, y position, width and height, the names of which are `ax`, `ay`, `aw`, and `ah`, respectively, per `print(self.setGeometry)`...
#         self.setWindowIcon(QIcon(window_icon)) # ...and finally set the `window_icon` using the `setWindowIcon` Method, passing it the `QIcon` Class with the Relative File Path to the `window_icon` file (for some reason this part is not working)
# def main():
#     app = QApplication(sys.argv) # Create an Object, an Instance of the `QApplication` Class, which is the main application Object, and pass it `argv` of the `sys` Module, which allows `PyQt5` to process any Terminal Arguments intended for it (if we didn't do this we'd have to pass an empty List like `[]` because `QApplication` needs some Argument)...
#     window = MainWindow() # ...create a `window` Object from the `MainWindow` Class...
#     window.show() # ...call the `show` Method on it to display the `window`...
#     sys.exit(app.exec_()) # ...and in order to keep the `window` open rather than having it close immediately we have to call the `exit` Method of the `sys` Module and pass it the `exec_` Method of the `app` Object so that it runs the application's event loop, i.e. the loop that listens for events and executes code based on those events...

# if __name__ == '__main__': # Place a Main Guard on the program to ensure it runs only when executed directly
#     main()




# # PyQt5 Labels - 9:31:28

# # See the "PyQt5 GUIs" lesson to understand what's going on in the boilerplate part of the below for which there are no comments

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel # See comments next to "import pygame" in the Alarm Clock Program lesson for how to install this `PyQt5` Module, which installs the same way and from which we'll import the `QApplication`, `QMainWindow` and `QLabel` Classes from the `QtWidgets` Submodule, and how to activate a virtual environment
# from PyQt5.QtGui import QFont # Import the `QFont` Class from the `QtGui` Submodule of the `PyQt5` Module
# from PyQt5.QtCore import Qt # Import the `QT` Class from the `QtCore` Submodule of the `PyQt5` Module (this `QT` Class is used for alignments)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)

#         label = QLabel('Hello', self)
#         label.setFont(QFont('Arial', 40)) # Call the `setFont` Method, and within that Method call the `QFont` Constructor, passing it the `name` and `size` of the font as Arguments
#         label.setGeometry(0 ,0, 500, 100) # Call the `setGeometry` Method on the `label` passing it the x position, y position, width and height
#         label.setStyleSheet('color: #292929;' # `PyQt5` has style properties that are a lot like CSS
#                             'background-color: #6fdcf7'
#                             'font-weight: bold;'
#                             'font-style: italic;'
#                             'text-decoration: underline;')
#         # label.setAlignment(Qt.AlignTop) # Call the `setAlignment` Method on the `label` passing it the `Qt.AlignTop` Argument to align to the top...
#         # label.setAlignment(Qt.AlignBottom) # ...or bottom...
#         # label.setAlignment(Qt.AlignVCenter) # ...or vertical center (which is the default)...
#         # label.setAlignment(Qt.AlignHCenter) # ...or horizontal center...
#         # label.setAlignment(Qt.AlignRight) # ...or horizontal right...
#         # label.setAlignment(Qt.AlignLeft) # ...or horizontal left...
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # ...or horizontal center and top, which is ironically depicted using the `|` operator rather than the `and` operator...
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # ...or horizontal center and bottom...
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # ...or vertical center and horizontal center...
#         label.setAlignment(Qt.AlignCenter) # ...which can also be done like this
        

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()




# # PyQt5 Images - 9:40:23

# # See the "PyQt5 GUIs" lesson to understand what's going on in the boilerplate part of the below for which there are no comments

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel # See comments next to "import pygame" in the Alarm Clock Program lesson for how to install this `PyQt5` Module, which installs the same way and from which we'll import the `QApplication`, `QMainWindow` and `QLabel` Classes (the most common and straight forward approach to displaying an image is to add an image to a label) from the `QtWidgets` Submodule, and how to activate a virtual environment
# from PyQt5.QtGui import QPixmap # Import the QPixmap Class from the `QtGui` Submodule of the `PyQt5` Module (used for loading, manipulating and displaying images)

# window_image = 'assets/cool_image.png' # Define the `window_image` with its Relative File Path

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)

#         label = QLabel(self) # Create a `label` Object and pass it the `self` Argument...
#         label.setGeometry(0, 0,  250, 250)

#         pixmap = QPixmap(window_image) # ...load our image to a `QPixmap` Object,...
#         label.setPixmap(pixmap) # ...then add this `QPixmap` Object to the label

#         label.setScaledContents(True) # Must call the `setScaledContents` Method on the `label` and pass it `True` so that the image scales to the size of the label

#         label.setGeometry((self.width() - label.width()) // 2, # Double forward slashes represent integer division (as opposed to standard division) which rounds down to the nearest whole number
#                             (self.height() - label.height()) // 2,
#                             label.width(),
#                             label.height()) # This is how you center the image in the window

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()




# # PyQt5 Layouts - 9:46:29

# # See the "PyQt5 GUIs" lesson to understand what's going on in the boilerplate part of the below for which there are no comments

# import sys
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout) # See comments next to "import pygame" in the Alarm Clock Program lesson for how to install this `PyQt5` Module, which installs the same way and from which we'll import the `QApplication`, `QMainWindow`, `QLabel`, `QWidget`, `QV`, `QVBoxLayout`, `QHBoxLayout` and `QGridLayout` Classes from the `QtWidgets` Submodule, and how to activate a virtual environment

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.initUI()

#     def initUI(self): # Create a discrete Function for initializing the UI
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         label1 = QLabel('Label #1', self)
#         label2 = QLabel('Label #2', self)
#         label3 = QLabel('Label #3', self)
#         label4 = QLabel('Label #4', self)
#         label5 = QLabel('Label #5', self)

#         label1.setStyleSheet('background-color: red;')
#         label2.setStyleSheet('background-color: yellow;')
#         label3.setStyleSheet('background-color: green;')
#         label4.setStyleSheet('background-color: blue;')
#         label5.setStyleSheet('background-color: purple;')

#         # vbox = QVBoxLayout() # To create a box with labels stacked vertically create a `QVBoxLayout` Object from the `QVBoxLayout` Class...

#         # vbox.addWidget(label1) # ...add all 5 labels to the box...
#         # vbox.addWidget(label2)
#         # vbox.addWidget(label3)
#         # vbox.addWidget(label4)
#         # vbox.addWidget(label5)

#         # central_widget.setLayout(vbox) # ...and set the layout of the `central_widget` to the box

#         # hbox = QHBoxLayout() # To create a box with labels stacked horizontally create a `QHBoxLayout` Object from the `QHBoxLayout` Class..

#         # hbox.addWidget(label1) # ...add all 5 labels to box...
#         # hbox.addWidget(label2)
#         # hbox.addWidget(label3)
#         # hbox.addWidget(label4)
#         # hbox.addWidget(label5)

#         # central_widget.setLayout(hbox) # ...and set the layout of the `central_widget` to the box


#         grid = QGridLayout() # To create a box with labels in a grid create a `QGridLayout` Object from the `QVBoxLayout` Class...

#         grid.addWidget(label1, 0, 0) # ...add all 5 labels to the box, but for `QGridLayout` must specify a row and a column after the label...
#         grid.addWidget(label2, 0, 1)
#         grid.addWidget(label3, 1, 0)
#         grid.addWidget(label4, 1, 1)
#         grid.addWidget(label5, 1, 2)

#         central_widget.setLayout(grid) # ...and set the layout of the `central_widget` to the box 

        
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()




# # PyQt5 Push Button Widgets - 9:53:07

# # See the "PyQt5 GUIs" lesson to understand what's going on in the boilerplate part of the below for which there are no comments

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton # See comments next to "import pygame" in the Alarm Clock Program lesson for how to install this `PyQt5` Module, which installs the same way and from which we'll import the `QApplication`, `QMainWindow`, `QLabel` and `QPushButton` Classes from the `QtWidgets` Submodule, and how to activate a virtual environment

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.button = QPushButton('Click me!', self) # Create a button Object by calling the `QPushButton` Constructor and passing it the text to display on the button (you don't have to place this within the Constructor Method but it's recommended)
#         self.label = QLabel('Hello', self) # Create a `label` Object by calling the `QLabel` Constructor (you don't have to place this within the Constructor Method but it's recommended)
#         self.initUI()

#     def initUI(self):
#         self.button.setGeometry(150, 200, 200, 100)
#         self.button.setStyleSheet('font-size: 30px;')
#         self.button.clicked.connect(self.on_click) # Take the `clicked` signal and connect it to a slot

#         self.label.setGeometry(150, 300, 200, 100)
#         self.label.setStyleSheet('font-size: 50;')

#     def on_click(self):
#         print('Button has been clicked')
#         self.button.setText('Clicked') # Because we don't want `button` or `label` to be considered local to this` on_click` Method we have to prefix them with `self` wherever we reference them from within the `on_click` Method so that they remain associated with the `MainWindow` Class
#         self.label.setText('Goodbye')
#         self.button.setDisabled(True) # Disable the button after clicked


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# # Recap: With buttons you need a signal that's connected to a slot. The signal is an event. The slot is an action that the widget is going to take when the signal occurs.




# # PyQt5 Checkboxes - 10:00:12

# # See the "PyQt5 GUIs" lesson to understand what's going on in the boilerplate part of the below for which there are no comments

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox # See comments next to "import pygame" in the Alarm Clock Program lesson for how to install this `PyQt5` Module, which installs the same way and from which we'll import the `QApplication`, `QMainWindow` and `QCheckBox` Classes from the `QtWidgets` Submodule, and how to activate a virtual environment
# from PyQt5.QtCore import Qt # The `QtCore` Submodule contains non-GUI Classes relevant to `PyQt5` applications

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.checkbox = QCheckBox('Do you like food', self) # Create a checkbox called `checkbox` within the Constructor of `MainWindow` by calling the Constructor of the `QCheckBox` Class passing it Arguments for the text we want to display and the parent widget, which of course is `self`
#         self.initUI()

#     def initUI(self):
#         self.checkbox.setGeometry(10, 0, 500, 100) # Set the dimensions and style it
#         self.checkbox.setStyleSheet('font-size: 30px;'
#                                     'font-family: Arial;'
#                                     'color: red;'
#                                     )
#         self.checkbox.setChecked(False) # If we were to set this to `True` it would make the initial state that `checkbox` should be checked (the default is `False`)
#         self.checkbox.stateChanged.connect(self.checkbox_changed) # Connect a signal, which is the `stateChanged` Method, to a slot, in this case our `checkbox_changed` Method, using the `connect` Method

#     def checkbox_changed(self, state): # We create a slot, which we'll make a Method within our `MainWindow` Class though it could exist elsewhere, named`checkbox_changed` and we'll call it when the state of `checkbox` changes. The value of the `state` Parameter is provided to us when we interact with `checkbox`
#         if state == Qt.Checked: # `Qt.Checked` is an an enum that represents the state of the checkbox when it's checked, which is otherwise 0 or 2, so `Qt.Checked` does nothing more than make it more readable
#             print('You like food')
#         else:
#             print('You don\'t like food')
        

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()




# # PyQt5 Radio Buttons - 10:06:42

# # See the "PyQt5 GUIs" lesson to understand what's going on in the boilerplate part of the below for which there are no comments

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup # See comments next to "import pygame" in the Alarm Clock Program lesson for how to install this `PyQt5` Module, which installs the same way and from which we'll import the `QApplication`, `QMainWindow`, `QRadioButton` and `QButtonGroup` Classes from the `QtWidgets` Submodule, and how to activate a virtual environment

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.radio1 = QRadioButton('Visa', self) # Construct 5 radio buttons within the Constructor of our `MainWindow` Class from the `QRadioButton` Class passing them first a Parameter for the text and second the `self`
#         self.radio2 = QRadioButton('Mastercard', self)
#         self.radio3 = QRadioButton('Gift Card', self)
#         self.radio4 = QRadioButton('In-Store', self) 
#         self.radio5 = QRadioButton('Online', self)

#         self.button_group1 = QButtonGroup(self) # The default behavior of `PyQt5` is that all radio buttons, unless explicitly stated, are part of the same group and so only one can be selected at a time unless we use the `QButtonGroup` Class to group them
#         self.button_group2 = QButtonGroup(self)

#         self.initUI()


#     def initUI(self):
#         self.radio1.setGeometry(0, 0, 300, 50)
#         self.radio2.setGeometry(0, 50, 300, 50)
#         self.radio3.setGeometry(0, 100, 300, 50)
#         self.radio4.setGeometry(0, 150, 300, 50)
#         self.radio5.setGeometry(0, 200, 300, 50)

#         self.setStyleSheet('QRadioButton{' # This is how we style multiple radio buttons at once, i.e. passing the entire `QRadioButton` Class as the selector to the `setStyleSheet` Method where each line of our Object is in its own quotes
#                             'font-size: 40px;'
#                             'font-family: Arial;'
#                             'padding: 10;'
#                             'psdding: 10px;'
#                         '}')

#         self.button_group1.addButton(self.radio1) # This is how we use the `QButtonGroup` Class to group the radio buttons
#         self.button_group1.addButton(self.radio2)
#         self.button_group1.addButton(self.radio3)
#         self.button_group2.addButton(self.radio4)
#         self.button_group2.addButton(self.radio5)

#         self.radio1.toggled.connect(self.radio_button_changed) # This is how we connect the `toggled` signal of the radio buttons to a slot, in this case our `radio_button_changed` Method
#         self.radio2.toggled.connect(self.radio_button_changed)
#         self.radio3.toggled.connect(self.radio_button_changed)
#         self.radio4.toggled.connect(self.radio_button_changed)
#         self.radio5.toggled.connect(self.radio_button_changed)


#     def radio_button_changed(self):
#         radio_button = self.sender() # The `sender` Method which is a Method of the `QObject` Class, which is the parent Class of all `PyQt5` Classes, returns a pointer to the object that sent the signal, i.e. the radio button that was clicked, so we can store what it returns as `radio_button`...
#         if radio_button.isChecked(): # ...use the `isChecked` Method to check if the radio button is checked...
#             print(f'{radio_button.text()} is selected') # ...and if it is print the text of the radio button that was clicked

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()




# # PyQt5 Line Edit Widgets (aka Text Boxes) - 10:15:56

# # See the "PyQt5 GUIs" lesson to understand what's going on in the boilerplate part of the below for which there are no comments

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton # See comments next to "import pygame" in the Alarm Clock Program lesson for how to install this `PyQt5` Module, which installs the same way and from which we'll import the `QApplication`, `QMainWindow`, `QLineEdit` and `QPushButton` Classes from the `QtWidgets` Submodule, and how to activate a virtual environment

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.line_edit = QLineEdit(self) # Create an Instance of the `QLineEdit` Class, which requires one Argument which is the parent widget, `self`, and assign it to the `line_edit` Attribute of the `MainWindow` Class
#         self.button = QPushButton('Submit', self) # Create an Instance of the `QPushButton` Class, which requires two Arguments, the first being the text to display on the button, and a second Argument which is the parent widget, `self`, and assign it to the `button` Attribute of the `MainWindow` Class
#         self.initUI()

#     def initUI(self):
#         self.line_edit.setGeometry(10, 10, 200, 40) # Set the geometry on the `line_edit`
#         self.line_edit.setStyleSheet('font-size: 25px;' # Set the styles on the `line_edit`
#                                     'font-family: Aerial;'
#                                     )
#         self.button.setGeometry(210, 10, 200, 40) # Set the geometry on the `button`
#         self.button.setStyleSheet('font-size: 25px;' # Set the styles on the `button`
#                             'font-family: Aerial;'
#                             )
#         self.line_edit.setPlaceholderText('Enter your name') # Use the `setPlaceholderText` of the `QLineEdit` Class to set a placeholder text

#         self.button.clicked.connect(self.submit) # Connect the `clicked` signal of the `button` to the `submit` Method

#     def submit(self): # Create a `submit` Method that takes no Arguments
#         text = self.line_edit.text()
#         print(f'Hello {text}')

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()




# # PyQt5 StyleSheets - 10:22:55

# # See the "PyQt5 GUIs" lesson to understand what's going on in the boilerplate part of the below for which there are no comments

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout # See comments next to "import pygame" in the Alarm Clock Program lesson for how to install this `PyQt5` Module, which installs the same way and from which we'll import the `QApplication`, `QMainWindow`, QPushButton, QWidget and QHBoxLayout Classes from the `QtWidgets` Submodule, and how to activate a virtual environment

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # self.setGeometry(700, 300, 500, 500) # In previous lessons we've used the `setGeometry` of the `QMainWindow` Class to set the position and dimensions of the window, but this time we're using the QHBoxLayout layout manager
#         self.button1 = QPushButton('#1', self) # Create 3 button widgets from the Constructor of the `QPushButton` Class, passing them the text to display, and because we're using a layout manager we don't need to additionally pass parent widget, `self`
#         self.button2 = QPushButton('#2', self)
#         self.button3 = QPushButton('#3', self)
#         self.initUI()

#     def initUI(self):
#         central_widget = QWidget() # Create a `central_widget` from the Constructor of the `QWidget` Class...
#         self.setCentralWidget(central_widget) # ...then call the `setCentralWidget` Method to set the central widget of the `MainWindow` to the `central_widget`

#         hbox = QHBoxLayout() # Now we can create a layout manager, we'll call it `hbox`, by calling the Constructor of the QHBoxLayout Class...

#         hbox.addWidget(self.button1) # ...and add the 3 buttons to the layout manager using the `addWidget` Method...
#         hbox.addWidget(self.button2)
#         hbox.addWidget(self.button3)

#         central_widget.setLayout(hbox) # ...and finally call the `setLayout` Method on our `central_widget` and pass it our layout manager

#         self.button1.setObjectName('button1') # Give each button a unique identifying String with the `setObjectName` Method
#         self.button2.setObjectName('button2')
#         self.button3.setObjectName('button3')

#         # There are a lot of CSS-like styles to write so we can use triple quotes to pass them as a multi-line String, where the styles shared among the 3 buttons are ascribed to the entire `QPushButton` Class, then individual styles are ascribed to the individual buttons by first calling the `setObjectName` Method on each of them and passing a unique identifying String (above), then using those Strings with `#` to map to them, and pseudo-classes are used to style the buttons when they're hovered over
#         self.setStyleSheet('''
#             QPushButton{
#                 font-size: 40px;
#                 font-family: Arial;
#                 padding: 15px 75px;
#                 margin: 25px;
#                 border: 3px solid;
#                 border-radius: 15px;
#             }
#             QPushButton#button1{
#                 background-color: red;
#             }
#             QPushButton#button2{
#                 background-color: green;
#             }
#             QPushButton#button3{
#                 background-color: blue;
#             }
#             QPushButton#button1:hover{
#                 background-color: pink;
#             }
#             QPushButton#button2:hover{
#                 background-color: lightgreen;
#             }
#             QPushButton#button3:hover{
#                 background-color: lightblue;
#             }
#         ''')

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()




# # PyQt5 Digital Alarm Clock Program - 10:32:48

# import sys # This Module provides Variables used and maintained by the Python interpreter
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout # Widgets are the building blocks of a GUI application. From the `PyQt5` Module we access the `QtWidgets` Submodule to import the `QApplication`, `QWidget`, `QLabel` and `QVBoxLayout` Classes, where `QVBoxLayout` is our layout manager
# from PyQt5.QtCore import QTimer, QTime, Qt # From the `PyQt5` Module we access the QtCore Submodule to import the `QTimer`, `QTime` and `Qt` Classes, where `QTimer` is a Class that provides repetitive and single-shot timers, `QTime` is a Class that provides clock time Functions, and `Qt` is a Class that provides a set of common non-GUI functionality
# from PyQt5.QtGui import QFont, QFontDatabase # From the `PyQt5` Module we access the `QtGui` Submodule to import the `QFont` and `QFontDatabase` Classes, where `QFont` is a Class that specifies a font used for drawing text, and `QFontDatabase` is a Class for managing and querying fonts available to the application

# # Note, if installing `PyQt5 doesn't work it's likely because `homebrew`, the unofficial package manager for macOS, is restricting it in which case you must install `PyQt5` in a virtual environment. The way to do this is to first create a virtual environment with `python3 -m venv <folder-name-for-virtual-environment>`, where `python3 -m venv venv` is usually the convention, which creates a new directory named `venv` containing the virtual environment. Then, in order to activate the virtual environment, do `source venv/bin/activate`. And finally, to install `PyQt5` in the virtual environment, do `pip3 install PyQt5`

# path_to_ds_digital_font = 'assets/ds_digital_font/DS-DIGIT.TTF'
 
# class DigitalClock(QWidget): # Instead of inheriting from the `QMainWindow` Class like we did in previous lessons, we'll inherit from the `QWidget` Class, which is a base Class to create our own widgets
#     def __init__(self): # Here in the Constructor is where we construct all of the different entities for the clock
#         super().__init__() # If there are any arguments passed to the Parent Class, `QWidget`, we will call the Constructor of the Parent, the Superclass here, to capture those Arguments
#         self.time_label = QLabel(self) # Using the `QLabel` Class we create a `time_label` Object and pass it the `self` Argument, which is the parent widget, and make the it one of our Attributes here in the Constructor by placing it here and prefixing it with `self`
#         self.timer = QTimer(self)  # Using the `QTimer` Class we create a `timer` Object and pass it the `self` Argument, which is the parent widget, and make it one of our Attributes here in the Constructor by placing it here and prefixing it with `self`
#         self.initUI() # We create a dedicated Function call here in the Constructor for initializing the UI, since initializing the UI has a lot of different steps and requires a lot of code

#     def initUI(self): # The layout of the digital clock gets designed here
#         self.setWindowTitle('Digital Clock') # Set the window title with the `setWindowTitle` Method which our `DigitalClock` Class inherits from the `QWidget` Class
#         self.setGeometry(600, 400, 300, 100) # Set the position and dimensions of the window with the `setGeometry` Method which our `DigitalClock` Class inherits from the `QWidget` Class, and whose Parameters are x position, y position, width and height, the names of which are `ax`, `ay`, `aw`, and `ah`, respectively, per `print(self.setGeometry)`

#         vbox = QVBoxLayout() # Create a layout manager with the Constructor within the `QVBoxLayout` Class, which will display all our widgets vertically
#         vbox.addWidget(self.time_label) # Add our label to our vertical layout manager by passing our `self.time_label` Object to it
#         self.setLayout(vbox) # Then to set the layout on our layout manager call the `setLayout` Method, inherited from the `QWidget` Class, and pass it our `vbox` layout manager

#         self.time_label.setAlignment(Qt.AlignCenter) # Call the `setAlignment` Method on the `time_label` Object, which it inherits from the `QLabel` Class, and pass it the `Qt.AlignCenter` Argument, which is a flag, to center the text
#         self.time_label.setStyleSheet('font-size: 150px;' # Call the `setStyleSheet` Method on the `time_label` Object, which it inherits from the `QLabel` Class, and pass it a multi-line String with the CSS-like styles we want to apply to the `time_label` Object
#                                         'color: rgb(114,241,77);'
#         )
#         self.setStyleSheet('background-color: rgb(0,0,40);') # Call the `setStyleSheet` Method on the `self` Object, which is the `DigitalClock` Object and which it inherits from the `QWidget` Class, and pass it a multi-line String with the CSS-like styles we want to apply to the `DigitalClock` Object, in this case just our `background-color`

#         font_id = QFontDatabase.addApplicationFont(path_to_ds_digital_font) # `QFontDatabase` is a Class for managing and querying fonts available to the application, and its `addApplicationFont` Method allows us to add a font using a File Path to it

#         # The following commented out code should work to apply the font, but doesn't for some reason (possibly because I'm running in a venv):

#         # font_family = QFontDatabase.applicationFontFamilies(font_id)[0] # The `applicationFontFamilies` Method of the `QFontDatabase` Class returns the font family name of the font that was added, and we store that in a `font_family` Variable, and the `[0]` gets the first element of the font family
#         # my_font = QFont(font_family, 150) # Using the `QFont` Class we create a `my_font` Object by calling the Constructor and passing it the `font_family` and a font size of our choice
#         # self.time_label.setFont(my_font) # Call the `setFont` Method on the `time_label` Object, which it inherits from the `QLabel` Class, and pass it our `my_font` Object


#         self.timer.timeout.connect(self.update_time) # In order to get our clock to update every second we need to connect our `timer` widget to a slot, using the `timeout` signal, which is emitted every time the `timer` times out, and the `connect` Method, which is a Method of the `QTimer` Class, passing it our `update_time` Method...
#         self.timer.start(1000) # ...which we create with the `start` Method of the `timer` Object, which is a Method of the `QTimer` Class, and pass it the number of milliseconds we want to wait before the `timer` times out, in this case 1000 milliseconds

#         self.update_time() # Call the `update_time` Method to update the time

#     def update_time(self):
#         current_time = QTime.currentTime().toString('hh:mm:ss AP') # Create a `current_time` Variable and assign it the current time derived using the `currentTime` Method of the `QTime` Class which returns the current time, and then call the `toString` Method on it and pass that a Formatted String, 'hh:mm:ss AP', which will format the time as hours, minutes, seconds, and provide AM/PM using the AP flag, which stands for Ante Meridiem
#         self.time_label.setText(current_time)

    
# def main():
#     app = QApplication(sys.argv) # Create an instance of the `QApplication` Class, which is the main application Object, and pass it `sys.argv`, which allows `PyQt5` to process any Terminal Arguments intended for it (no Terminal arguments need to be passed to our application, but this is boilerplate for good measure in case we ever want to pass any in the future)
#     clock = DigitalClock() # Create a `clock` Object by calling the Constructor of the `DigitalClock` Class (no arguments need to be passed) and upon running our app the widget, our `clock` Object created from the `DigitalClock` Class, won't display unless...
#     clock.show() # ...we call the `show` Method on our `clock` Object, which it inherits from the `QWidget` Class, and even still it will only appear for a brief moment unless...
#     sys.exit(app.exec_()) # ...we pass a call to the `exec_` Method, which starts the main event loop of the application, to the `exit` Method of the `sys` Module, which handles user interaction, and which allows us to have a running widget that stays in place until we exit the widget itself

# if __name__ == '__main__': # Place a Main Guard on the program to ensure it runs only when executed directly
#     main()




# # PyQt5 Stopwatch Program - 10:48:38

# import sys # `sys` obviously means "system". This Module provides Variables used and maintained by the Python interpreter
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout # From the `PyQt5` Module we access the `QtWidgets` Submodule to import the `QApplication`, `QWidget`, `QLabel`, `QPushButton`, `QVBoxLayout` and `QHBoxLayout` Classes where `QVBoxLayout` and `QHBoxLayout` are layout managers that together work like CSS Flexbox
# from PyQt5.QtCore import QTimer, QTime, Qt # From the `PyQt5` Module we access the QtCore Submodule to import the `QTimer`, `QTime` and `Qt` Classes, where `QTimer` is a Class that provides repetitive and single-shot timers, `QTime` is a Class that provides clock time Functions, and `Qt` is a Class that provides a set of common non-GUI functionality

# # Note, if installing `PyQt5 doesn't work it's likely because `homebrew`, the unofficial package manager for macOS, is restricting it in which case you must install `PyQt5` in a virtual environment. The way to do this is to first create a virtual environment with `python3 -m venv <folder-name-for-virtual-environment>`, where `python3 -m venv venv` is usually the convention, which creates a new directory named `venv` containing the virtual environment. Then, in order to activate the virtual environment, do `source venv/bin/activate`. And finally, to install `PyQt5` in the virtual environment, do `pip3 install PyQt5`

# class Stopwatch(QWidget): # We construct a Class named Stopwatch that inherits from the QWidget Class, meaning Stopwatch is a Subclass of QWidget and gains all its Properties and Methods
#     def __init__(self): # We create a Constructor Method for our Stopwatch Class, which doesn't need any Arguments besides `self`
#         super().__init__() # If we have any Arguments that we have to pass to the Parent of QWidget we call the Superclass, the Parent, and call the Constructor of the Parent, i.e. `__init__`, which currently has no Arguments
#         self.time = QTime(0, 0, 0, 0) # In the Constructor of our Stopwatch we create a `time` Object from the Constructor within the Class of `QTime` and pass it Arguments for hours, minutes, seconds and milliseconds
#         self.time_label = QLabel('00:00:00.00', self) # In the Constructor of our Stopwatch we create a `time_label` Object from the Constructor within the Class of `QLabel` and pass it Arguments for the text to display and the Parent widget, `self`
#         self.start_button = QPushButton('Start', self) # In the Constructor of our Stopwatch we create a `start_button` Object from the Constructor within the Class of `QPushButton` and pass it Arguments for the text to display and the Parent widget, `self`
#         self.stop_button = QPushButton('Stop', self) # In the Constructor of our Stopwatch we create a `stop_button` Object from the Constructor within the Class of `QPushButton` and pass it Arguments for the text to display and the Parent widget, `self`
#         self.reset_button = QPushButton('Reset', self) # In the Constructor of our Stopwatch we create a `reset_button` Object from the Constructor within the Class of `QPushButton` and pass it Arguments for the text to display and the Parent widget, `self`
#         self.timer = QTimer(self) # In the Constructor of our Stopwatch we create a `timer` Object from the Constructor within the Class of `QTimer` and pass it the Parent widget, `self`

#         self.initUI() # We create a dedicated Function call here in the Constructor for initializing the UI, since initializing the UI has a lot of different steps and requires a lot of code

#     def initUI(self): # We design the UI with this Method
#         self.setWindowTitle('Stopwatch') # Set the window title with the `setWindowTitle` Method which our `Stopwatch` Class inherits from the `QWidget` Class

#         vbox = QVBoxLayout() # Create a layout manager with the Constructor within the `QVBoxLayout` Class, which will display all our widgets vertically
#         vbox.addWidget(self.time_label) # Add our label to our vertical layout manager by passing our `self.time_label` Object to it

#         self.setLayout(vbox) # Then to set the layout on our layout manager call the `setLayout` Method, inherited from the `QWidget` Class, and pass it our `vbox` layout manager

#         self.time_label.setAlignment(Qt.AlignLeft) # Call the `setAlignment` Method on the `time_label` Object, which it inherits from the `QLabel` Class, and pass it the `Qt.AlignLeft` Argument, which is a flag, to left-align the text

#         hbox = QHBoxLayout() # Create a layout manager with the Constructor within the `QHBoxLayout` Class, which will display all our widgets horizontally

#         hbox.addWidget(self.start_button) # Add our buttons to our horizontal layout manager by passing our `self.start_button` Object to it
#         hbox.addWidget(self.stop_button) 
#         hbox.addWidget(self.reset_button)

#         vbox.addLayout(hbox) # Add our horizontal layout manager to our vertical layout manager, which the CSS Flexbox equivalent of this is to nest a flex container within a flex container

#          # There are a lot of CSS-like styles to write so we can use triple quotes to pass them as a multi-line String, where the styles shared between the `QPushButton` and QLabel Classes are designated by listing `QPushButton, QLabel` horizontally separated by a comma, and the individual styles applied separately to each of them are done so by simply listing the Class name followed by the styles
#         self.setStyleSheet('''
#             QPushButton, QLabel{
#                 padding: 20px;
#                 font-weight: bold;
#                 font-family: calibri;
#             }
#             QPushButton{
#                 font-size: 50px;
#             }
#             QLabel{
#                 font-size: 120px;
#                 background-color: hsl(200, 100%, 85%);
#                 border-radius: 20px;    
#             }
#         ''')

#         self.start_button.clicked.connect(self.start) # Use the `connect` Method of the `clicked` signal of the `start_button` Object to connect it to a slot, which we make our `start` Method
#         self.stop_button.clicked.connect(self.stop) # Use the `connect` Method of the `clicked` signal of the `stop_button` Object to connect it to a slot, which we make our `stop` Method
#         self.reset_button.clicked.connect(self.reset) # Use the `connect` Method of the `clicked` signal of the `reset_button` Object to connect it to a slot, which we make our `reset` Method

#         self.timer.timeout.connect(self.update_display) # Use the `connect` Method of the `timeout` signal of the `timer` Object to connect it to the `update_display` Method


#     def start(self): # Create a `start` Method that takes no Arguments except for `self`, which is has to because it's a Method of our `Stopwatch` Class...
#         self.timer.start(10) # ...which simply calls the `start` Method of the `timer` Object passing it `10`, signifying the number of milliseconds to wait before the `timer` times out, to start the timer

#     def stop(self): # Create a `stop` Method that takes no Arguments except for `self`, which it has to because it's a Method of our `Stopwatch` Class...
#         self.timer.stop() # ...which simply calls the `stop` Method of the `timer` Object to stop the timer

#     def reset(self): # Create a `reset` Method that takes no Arguments except for `self`, which it has to because it's a Method of our `Stopwatch` Class...
#         self.timer.stop() # ...which calls the `stop` Method of the `timer` Object to stop the timer
#         self.time = QTime(0, 0, 0, 0) # ...resets the `time` Attribute in our Constructor back to all zeros...
#         self.time_label.setText(self.format_time(self.time)) # ...and calls the `setText` Method of the `time_label` Object, which it inherits from the `QLabel` Class, and passes it the `format_time` Method passing it what is returned from our call to our `format_time` Method when that's passed the `self.time`


#     def format_time(self, time): # Create a `format_time` Method which takes the `time` Argument, which is a `QTime` Object, and returns a Formatted String according to our format specifications
#         hours = time.hour()
#         minutes = time.minute()
#         seconds = time.second()
#         centiseconds = time.msec() // 10 # Use integer division to divide the milliseconds by 10 so that it gives us centiseconds, which looks better for a stopwatch
#         return f'{hours:02}:{minutes:02}:{seconds:02}.{centiseconds:02}'

#     def update_display(self): # Create an `update_display` Method that takes no Arguments except for `self`, which it has to because it's a Method of our `Stopwatch` Class...
#         self.time = self.time.addMSecs(10) # ...which calls the `addMSecs` Method of the `time` Object, which is a Method of the `QTime` Class, and passes it `10` to add 10 milliseconds to the `time` Object
#         self.time_label.setText(self.format_time(self.time)) # ...and calls the `setText` Method of the `time_label` Object, which it inherits from the `QLabel` Class, and passes it the `format_time` Method passing it what is returned from our call to our `format_time` Method when that's passed the `self.time`


# def main():
#     app = QApplication(sys.argv) # Create an instance of the `QApplication` Class, which is the main application Object, and pass it `sys.argv`, the Arguments of our system, `sys`, which allows `PyQt5` to process any Terminal Arguments intended for it (no Terminal arguments need to be passed to our application, but this is boilerplate for good measure in case we ever want to pass any in the future)
#     stopwatch = Stopwatch() # Create a `stopwatch` Object by calling the Constructor of the `Stopwatch` Class (no arguments need to be passed) and upon running our app the widget, our `stopwatch` Object created from the `Stopwatch` Class, won't display unless...
#     stopwatch.show() # ...we call the `show` Method on our `stopwatch` Object, which it inherits from the `QWidget` Class, and even still it will only appear for a brief moment unless...
#     sys.exit(app.exec_()) # ...we pass a call to the `exec_` Method, which starts the main event loop of the application, to the `exit` Method of the `sys` Module, which handles user interaction, and which allows us to have a running widget that stays in place until we exit the widget itself

# if __name__ == '__main__': # Place a Main Guard on the program to ensure it runs only when executed directly, i.e. if the `__name__` Variable is equal to '__main__' it means we're executing the script directly and not importing it as a Module, so the Python interpreter will execute the code following the `if` statement, namely the call to our `main` Function
#     main()




# # PyQt5 Weather App - 11:06:05

# import sys # `sys` obviously means "system". This Module provides Variables used and maintained by the Python interpreter
# import requests # The `requests` Module allows us to send HTTP requests using Python
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout # From the `PyQt5` Module we access the `QtWidgets` Submodule to import the `QApplication`, `QWidget`, `QLabel`, `QLineEdit`, `QPushButton` and `QVBoxLayout` Classes, where `QVBoxLayout` is the layout manager (we only need a vertical layout manager for this Weather App, there's no need for a horizontal layout manager)
# from PyQt5.QtCore import  Qt # From the `PyQt5` Module we access the `QtCore` Submodule to import the `Qt` Class, which is a Class that provides a set of common non-GUI functionality

# # Note, if installing `PyQt5 doesn't work it's likely because `homebrew`, the unofficial package manager for macOS, is restricting it in which case you must install `PyQt5` in a virtual environment. The way to do this is to first create a virtual environment with `python3 -m venv <folder-name-for-virtual-environment>`, where `python3 -m venv venv` is usually the convention, which creates a new directory named `venv` containing the virtual environment. Then, in order to activate the virtual environment, do `source venv/bin/activate`. And finally, to install `PyQt5` in the virtual environment, do `pip3 install PyQt5`

# class WeatherApp(QWidget): # We construct a Class named `WeatherApp` that inherits from the `QWidget` Class, meaning `WeatherApp` is a Subclass of `QWidget` and gains all its Properties and Methods

#     def __init__(self): # We create a Constructor Method for our `WeatherApp` Class, which doesn't need any Arguments besides `self`
#         super().__init__() # If we have any Arguments that we have to pass to the Parent of `QWidget` we call the Superclass, the Parent, and call the Constructor of the Parent, i.e. `__init__`, which currently has no Arguments. `super()` is used to call a Method from a Parent Class. In this case the Method we're calling (which we're "chaining" on) is `__init__`, namely the Constructor of `QWidget` itself, i.e. the Constructor of the Parent Class of `WeatherApp`. When we create a Class that inherits from a Parent Class we often want to initialize the Parent Class as well because it might have some important setup code that needs to run. The `super()` Function returns a temporary Object of the Superclass that allows us to call its Methods, and the the `__init__` Method, the special Method in Python Classes known as a Constructor, is automatically called when an instance of the Class is created. In this case, `super().__init__()` is calling the Constructor of `QWidget`, which currently has no Arguments. This ensures that any initialization code in `QWidget` is executed before we add our own initialization code in `WeatherApp`. This is important to avoid potential issues that might arise if the Parent Class is not properly initialized. In summary, `super().__init__()` is used to ensure that the Parent Class, `QWidget`, is properly initialized before we proceed with the initialization of our own `WeatherApp` class
#         self.city_label = QLabel('Enter city name: ', self) # We create a `city_label` Attribute here in the Constructor of our `WeatherApp` Class, and we create it from the Constructor of the `QLabel` Class by passing it two Arguments: The first one for the text to display and second one for a reference to our Parent widget itself, `self`
#         self.city_input = QLineEdit(self) # We create a `city_input` Attribute here in the Constructor of our `WeatherApp` Class, and we create it from the Constructor of the `QLineEdit` Class by passing it a reference to our Parent widget itself, `self`
#         self.get_weather_button = QPushButton('Get Weather', self) # We create a `get_weather_button` Attribute here in the Constructor of our `WeatherApp` Class, and we create it from the Constructor of the `QPushButton` Class by passing it two Arguments: The first one for the text to display and second one for a reference to our Parent widget itself, `self`
#         self.temperature_label = QLabel(self) # We create a `temperature_label` Attribute here in the Constructor of our `WeatherApp` Class, and we create it from the Constructor of the `QLabel` Class by passing it a reference to our Parent widget itself, `self`
#         self.emoji_label = QLabel(self) # We create an `emoji_label` Attribute here in the Constructor of our `WeatherApp` Class, and we create it from the Constructor of the `QLabel` Class by passing it a reference to our Parent widget itself, `self`
#         self.description_label = QLabel(self) # We create a `description_label` Attribute here in the Constructor of our `WeatherApp` Class, and we create it from the Constructor of the `QLabel` Class by passing it a reference to our Parent widget itself, `self`. 
        
#         # We create all these Attributes here in the Constructor because we want to make them available to all the Methods of our `WeatherApp` Class

#         self.initUI() # Finally we call a `initUI` Method, defined below, to initialize the UI of our `WeatherApp` Class. It's better to separate the initialization of the UI from the Constructor because the UI initialization has a lot of different steps and requires a lot of code


#     def initUI(self): # We define a `initUI` Method

#         self.setWindowTitle('Weather App') # Use the `setWindowTitle` Method, which our `WeatherApp` Class inherits from the `QWidget` Class, to set the window title

#         vbox = QVBoxLayout() # We create an Object called `vbox` which is a generic (no Arguments passed) Instance of the `QVBoxLayout` Class. This gives us access to the Methods and Properties of the `QVBoxLayout` Class which we'll need to add the subwidgets to this vertical layout manager, which works like CSS Flexbox

#         # Using the `addWidget` Method which our `vbox` Object inherited from the `QVBoxLayout` Class, we add each of the subwidgets, which all exist as Attributes we defined in our Constructor, to the vertical layout manager
#         vbox.addWidget(self.city_label)
#         vbox.addWidget(self.city_input)
#         vbox.addWidget(self.get_weather_button)
#         vbox.addWidget(self.temperature_label)
#         vbox.addWidget(self.emoji_label)
#         vbox.addWidget(self.description_label)

#         self.setLayout(vbox) # Using the `setLayout` Method which our `self` Object inherited from the `QWidget` Class, we set the layout of our `WeatherApp` Class to the vertical layout manager, i.e. the `vbox` Object we just created

#         # For 5 of our 6 subwidgets we set the alignment to center using the `setAlignment` Method, which each of them inherited from either the `QLabel` or `QLineEdit` Classes, respectively, passing the `Qt.AlignCenter` Argument, which is an enum from the `Qt` Class. We can't call a `setAlignment` Method on our `self.get_weather_button` because it's an instance of the `QPushButton` Class which, unlike `QLabel` and `QLineEdit` Classes, doesn't have built-in support for text alignment hence lacks a `setAlignment` or similar Method. We don't need to center it because it's the widest subwidget we have so it already takes up the entire width of the window, but if we'd needed to we'd have to use a horizontal layout manager, i.e. QHBoxLayout
#         self.city_label.setAlignment(Qt.AlignCenter)
#         self.city_input.setAlignment(Qt.AlignCenter)
#         self.temperature_label.setAlignment(Qt.AlignCenter)
#         self.emoji_label.setAlignment(Qt.AlignCenter)
#         self.description_label.setAlignment(Qt.AlignCenter)

#         # For all 6 of our subwidgets we use the `setObjectName` Method, which each of the subwidgets inherited from either the `QLabel`, `QLineEdit` or `QPushButton` Classes, respectively, to give them an id` so we can style them individually using CSS-like styles
#         self.city_label.setObjectName('city_label')
#         self.city_input.setObjectName('city_input')
#         self.get_weather_button.setObjectName('get_weather_button')
#         self.temperature_label.setObjectName('temperature_label')
#         self.emoji_label.setObjectName('emoji_label')
#         self.description_label.setObjectName('description_label')

#         # We use the `setStyleSheet` Method, which our `WeatherApp` Class inherited from the `QWidget` Class, to apply CSS-like styles, which will style all the subwidgets within it. We want all instances of `QLabel` and `QPushButton` to share `font-family: calibri`, and for the rest of the subwidgets we identify them by adding their id` to the respective Parent Class from which they were created to style them individually. Note, we technically don't need to prefix each id with the Parent Class name but it's good practice to make it clear that we're using an id selector. (Also note, the `Segoe UI emoji` font in `QLabel#emoji_label` isn't working and, from previous lessons "PyQt5 Labels" and "PyQt5 Digital Alarm Clock Program" wherein we tried to apply a custom font with the `QFont` Class imported from the `QtGui` Submodule of `PyQt5`, I imagine even if we were to deliberately download and add it locally to the project it wouldn't work)
#         self.setStyleSheet('''
#             QLabel, QPushButton{
#                 font-family: calibri;               
#             }
#             QLabel#city_label{
#                 font-size: 40px;
#                 font-style: italic;               
#             }
#             QLineEdit#city_input{
#                 font-size: 40px;
#                 min-height: 50px;
#             }
#             QPushButton#get_weather_button{
#                 font-size: 30px; 
#                 font-weight: bold;
#             }
#             QLabel#emoji_label{
#                 font-size: 100px;
#                 font-family: Segoe UI emoji;
#             }
#             QLabel#description_label{
#                 font-size: 50px;
#             }
#         ''')


#         self.get_weather_button.clicked.connect(self.get_weather) # We use the `connect` Method of the `clicked` signal of the `get_weather_button` Object to connect it to a slot, which we make our `get_weather` Method, defined below


#     def get_weather(self): # We define a `get_weather` Method

#         api_key = 'eb2c2639c0a87540eb8554d54fefa773' # Note, this is a dummy API key. Go to `https://openweathermap.org ` to create a free account and generate your own
#         city = self.city_input.text() # We create a `city` Variable and assign it the text entered in the `city_input` Object, which is a `QLineEdit` Object, by calling the `text` Method on it, which it inherits from the `QLineEdit` Class
#         url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}' # We use a Formatted String to structure our URL with the necessary Parameters passed on the Query String, namely `city` and `api_key`, according to the docs at `https://openweathermap.org/current#name`

#         try: # We set up a `try-except` block with a response to handle any HTTP errors that might occur when we send a request to the API
#             response = requests.get(url) # The `get` Method of the `requests` Module sends a GET request to the specified URL and returns a `Response` Object, which we save as a Variable called `response`
#             response.raise_for_status() # We have to call the `raise_for_status` Method on the `response` Object to raise an exception if the request returned an unsuccessful status code, which is any code greater than or equal to 400. We have to do this if we want to handle any HTTP errors (our `try-except` block won't automatically do this so we have to add this here)
#             data = response.json() # We then use the `json` Method of the `response` Object, which is an instance of a Class from the `requests` Module, to convert the JSON data into a Python Dictionary, which we save as a Variable called `data`

#             if data['cod'] == 200: # Then if the `cod` key in the parsed `data` Dictionary is 200, which means the request was successful...
#                 self.display_weather(data) # ...we can display the data by calling our `display_weather` Method (defined further below)

#         except requests.exceptions.HTTPError as http_error: # If not successful we create an exception with a Match Case Statement of cases, each of which call our `display_error` Method (defined further below) with the appropriate text String for each of the possible HTTP errors that might occur, and call the exception `http_error` so we can surface it in the default, i.e. `_`, case
#             match response.status_code:
#                 case 400:
#                     self.display_error('Bad Request:\nPlease check your input')
#                 case 401:
#                     self.display_error('Unauthorized:\nIs your API key valid?')
#                 case 403:
#                     self.display_error('Forbidden:\nAccess denied')
#                 case 404:
#                     self.display_error('Not Found:\nCity not found')
#                 case 500:
#                     self.display_error('Internal Server Error:\nPlease try again later')
#                 case 502:
#                     self.display_error('Bad Gateway:\nInvalid response from the server')
#                 case 503:
#                     self.display_error('Service Unavailable:\nServer is down')
#                 case 504:
#                     self.display_error('Gateway Timeout:\nNo response from the server')
#                 case _:
#                     self.display_error('HTTP Error Occurred:\n{http_error}')

#         # For the other, non HTTP, errors that could occur we create other exceptions
#         except requests.exceptions.ConnectionError:
#             self.display_error('Connection Error:\nCheck your internet connection')

#         except requests.exceptions.Timeout:
#             self.display_error('Timeout Error:\nThe request timed out')

#         except requests.exceptions.TooManyRedirects:
#             self.display_error('Too many Redirects:\nCheck the URL')

#         except requests.exceptions.RequestException as req_error:
#             self.display_error(f'Request Error:\n{req_error}')


#     def display_error(self, message): # We define the `display_error` Method

#         self.temperature_label.setStyleSheet('font-size: 32px;') # Which first reduces the font-size of our `temperature_label` Attribute
#         self.temperature_label.setText(message) # Then uses it to display the error message
#         self.emoji_label.clear() # Clears the `emoji_label` Attribute
#         self.description_label.clear() # Clears the `description_label` Attribute


#     def display_weather(self, data): # We define a `display_weather` Method

#         self.temperature_label.setStyleSheet('font-size: 64px') # Which first increases the font-size of our `temperature_label` Attribute
#         temperature_k = data['main']['temp'] # Accesses the temperature from the `data` Dictionary, which the API provides in Kelvin
#         temperature_C = temperature_k - 273.15 # Converts Kelvin to Celsius
#         temperature_f = (temperature_k * 9/5) - 459.67 # Concerts Kelvin to Fahrenheit

#         weather_id = data['weather'][0]['id'] # Accesses the weather ID from the `data` Dictionary

#         weather_description = data['weather'][0]['description'] # Accesses the weather description from the `data` Dictionary

#         # To display the temperature, weather emoji and weather description we use the `setText` Method, which each our `temperature_label`, `emoji_label` and `description_label` inherit from the `QLabel` Class
#         self.temperature_label.setText(f'{temperature_f:.0f}°F / {temperature_C:.0f}°C')
#         self.emoji_label.setText(self.get_weather_emoji(weather_id))
#         self.description_label.setText(f'{weather_description}')


#     @staticmethod # Because this Method doesn't rely on any Class data or Instance data, namely it doesn't use the `self` Parameter, we can define it as a Static Method (by preceding it with `@staticmethod`), which is a Method that belongs to a Class itself and not to any particular Instance of a Class, i.e. is used more as a utility Function...
#     def get_weather_emoji(weather_id): # ...and then define this `get_weather_emoji` to simply return an emoji based on the weather ID passed to it
        
#         if 200 <= weather_id <= 232: # Situating a Variable between to conditions that it shares is a shorthand technique unique to Python, and is equivalent to `weather_id >= 200 and weather_id <= 232`. The shorthand can't be done in JavaScript and so has to read `weather_id >= 200 && weather_id <= 232` with `weather_id` mentioned twice
#             return '⛈️'
#         elif 300 <= weather_id <= 321:
#             return '🌤️'
#         elif 500 <= weather_id <= 531:
#             return '🌧️'
#         elif 600 <= weather_id <= 622:
#             return '❄️'
#         elif 700 <= weather_id < 741:
#             return '🌫️'
#         elif weather_id == 762:
#             return '🌋'
#         elif weather_id == 771:
#             return '💨'
#         elif weather_id == 781:
#             return '🌪️'
#         elif weather_id == 800:
#             return '🌞'
#         elif 801 <= weather_id <= 804:
#             return '🌥️'
#         else: 
#             return ''


# def main():
#     app = QApplication(sys.argv) # Create an instance of the `QApplication` Class, which is the main application Object, and pass it `sys.argv`, the Arguments of our system, `sys`, which allows `PyQt5` to process any Terminal Arguments intended for it (no Terminal arguments need to be passed to our application, but this is boilerplate for good measure in case we ever want to pass any in the future)
#     weather_app = WeatherApp() # Create a `weather_app` Object by calling the Constructor of the `WeatherApp` Class (no arguments need to be passed) and upon running our app the widget, our `weather_app` Object created from the `WeatherApp` Class, won't display unless...
#     weather_app.show() # ...we call the `show` Method on our `weather_app` Object, which it inherits from the `QWidget` Class, and even still it will only appear for a brief moment unless...
#     sys.exit(app.exec_()) # ...we pass a call to the `exec_` Method, which starts the main event loop of the application, to the `exit` Method of the `sys` Module, which handles user interaction, and which allows us to have a running widget that stays in place until we exit the widget itself

# if __name__ == '__main__': # Place a Main Guard on the program to ensure it runs only when executed directly, i.e. if the `__name__` Variable is equal to '__main__' it means we're executing the script directly and not importing it as a Module, so the Python interpreter will execute the code following the `if` statement, namely the call to our `main` Function
#     main()




# # PyQt5 Boilerplate (This is simply an example of how to set up a PyQt5 app window that's ready for styling and functionality to be hammered in)

# import sys # `sys` obviously means "system". This Module provides Variables used and maintained by the Python interpreter
# import requests # The `requests` Module allows us to send HTTP requests using Python
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout # From the `PyQt5` Module we access the `QtWidgets` Submodule to import the `QApplication`, `QWidget`, `QLabel`, `QPushButton`, `QVBoxLayout` and `QHBoxLayout` Classes where `QVBoxLayout` and `QHBoxLayout` are layout managers that together work like CSS Flexbox
# from PyQt5.QtCore import  Qt # From the `PyQt5` Module we access the QtCore Submodule to import the `Qt` Class, which is a Class that provides a set of common non-GUI functionality

# # Note, if installing `PyQt5 doesn't work it's likely because `homebrew`, the unofficial package manager for macOS, is restricting it in which case you must install `PyQt5` in a virtual environment. The way to do this is to first create a virtual environment with `python3 -m venv <folder-name-for-virtual-environment>`, where `python3 -m venv venv` is usually the convention, which creates a new directory named `venv` containing the virtual environment. Then, in order to activate the virtual environment, do `source venv/bin/activate`. And finally, to install `PyQt5` in the virtual environment, do `pip3 install PyQt5`

# class BoilerPlateApp(QWidget): # We construct a Class named BoilerPlateApp that inherits from the QWidget Class, meaning BoilerPlateApp is a Subclass of QWidget and gains all its Properties and Methods
#     def __init__(self): # We create a Constructor Method for our BoilerPlateApp Class, which doesn't need any Arguments besides `self`
#         super().__init__() # If we have any Arguments that we have to pass to the Parent of QWidget we call the Superclass, the Parent, and call the Constructor of the Parent, i.e. `__init__`, which currently has no Arguments

# def main():
#     app = QApplication(sys.argv) # Create an instance of the `QApplication` Class, which is the main application Object, and pass it `sys.argv`, the Arguments of our system, `sys`, which allows `PyQt5` to process any Terminal Arguments intended for it (no Terminal arguments need to be passed to our application, but this is boilerplate for good measure in case we ever want to pass any in the future)
#     boilerplate_app = BoilerPlateApp() # Create a `boilerplate_app` Object by calling the Constructor of the `BoilerPlateApp` Class (no arguments need to be passed) and upon running our app the widget, our `boilerplate_app` Object created from the `BoilerPlateApp` Class, won't display unless...
#     boilerplate_app.show() # ...we call the `show` Method on our `boilerplate_app` Object, which it inherits from the `QWidget` Class, and even still it will only appear for a brief moment unless...
#     sys.exit(app.exec_()) # ...we pass a call to the `exec_` Method, which starts the main event loop of the application, to the `exit` Method of the `sys` Module, which handles user interaction, and which allows us to have a running widget that stays in place until we exit the widget itself

# if __name__ == '__main__': # Place a Main Guard on the program to ensure it runs only when executed directly, i.e. if the `__name__` Variable is equal to '__main__' it means we're executing the script directly and not importing it as a Module, so the Python interpreter will execute the code following the `if` statement, namely the call to our `main` Function
#     main()