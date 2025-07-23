

"""
import random
num = random.randint(1,100)
attempts = 0

while True:
    user = input("Gues a numer (1-100) q to quit:")

    if user.lower() == "q":
        print("Okay!")
        break
    else:

        try:
            guess = int(user)
            attempts += 1

            if guess == num:
                print(f"Your Right!{num} is the correct answer!")
                print(f"You got it in {attempts} attempts!")

                user =input("Want to play again?(y/n): ")
                if user.lower() == "y":
                    num = random.randint(1, 100)
                    attempts = 0
                    continue
                else:
                    break

            elif guess > num:
                print(f"{user} is not the right answer, lower please.")
            elif guess < num:
                print(f"{user} is not the correct answer. Higher please!")
            else:
                print("Invalid input!")
        except ValueError:
                print("Invalid Input.")

"""

"""
import random

num = random.randint(1,100)

attempts = 0

while True:
    user = input("Guess the secret number q to quit: ")
    if user.lower() == "q":
        print("Okay! Thanks for playing.")
        break
    else:
        try:
            guess = int(user)
            attempts += 1

            if guess == num:
                print(f"Your are right! {user} is the correct answer!")
                print(f"You got it in {attempts} attempts!")

                user = input("Play again? (y/n): ")
                if user == "y":
                  continue
                break
            elif guess > num:
                print(f"Almost there {user} is a bit higher!")
            elif guess < num:
                print(f"Keep trying! {user} is a bit lower!")

            else:
                print(f"{user} Invalid Input!")
        except ValueError:
            print("Error please try again.")
"""
"""
while True:
    try:
        user = int(input("Enter a number for FizzBuzz: "))

        if user % 3 == 0 and user % 5 == 0:
            print("FizzBuzz")
        elif user % 3 == 0:
            print("Fizz")
        elif user % 5 == 0:
            print("Fizz")
        else:
            print(user)
    except ValueError:
        print("Invalid Input. Please tyr again.")

"""
"""
for user in range (1,101):

        if user % 3 == 0 and user % 5 == 0:
            print("FizzBuzz")
        elif user % 3 == 0:
            print("Fizz")
        elif user % 5 == 0:
            print("Buzz")
        else:
            print(user)
"""

"""
import random
secret = random.randint(1,100)

attempts = 0

while True:

    user = input("Guess the secret number q to quit: ")

    if user.lower() == "q":
        print("Thanks for playing.")
        break
    else:
        try:
            guess = int(user)
            attempts += 1

            if guess == secret:
                print(f"Your are right! {guess} is the secret number!")
                print(f"You guess it in {attempts} attempts!")

                user = input("Want to play again? y/n: ")
                if user.lower() == "y":
                    secret = random.randint(1,100)
                    attempts = 0
                    continue
                else:
                    print("Thanks for playing!")
                    break
            elif guess > secret:
                print(f"You got this {guess} is a bit higher!")
            elif guess < secret:
                print(f"Keep trying! {guess} is a bit lower!")
        except ValueError:
            print("Invalid Input!")

"""
"""
def greet(name):
    print(f"Hi {name}")

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Mosh")
print(message)

"""
"""
odd = 0
even = 0
while True:
    user = input("Enter a number(q to quit): ")
    if user.lower() == "q":
         total = odd + even
         print("Okay!")
         print(f"Odd numbers: {odd}")
         print(f"Even numbers: {even}")
         print(total)
         break
    else:
        try:
            num = int(user)

            if num % 2 == 0:
                print(f"{num} is even.")
                even += 1
            else:
                print(f"{num} is odd.")
                odd += 1
        except ValueError:
            print("Invalid Input!")
            
"""
"""
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Invalid 3 Attempts!")
    """

#for x in range (5):
  #  print(x)
"""
shopping_cart = ["mark", "micah"]

for item in shopping_cart:
    print(item)

"""
"""
even_num = 0

for i in range(1, 10):
    if i %2 == 0:
        even_num += 1
        print(i)
print(f"We have {even_num} even numbers")

"""
"""
birth_year = int(input('Birth year: '))
age = 2025 - birth_year
print(age)
"""
"""
word = "hello world"
vowels = "aeiou"
total = 0

for char in word:
    if char.lower() in vowels:
        total += 1
        print(f"We Found: {char}")

print(f"The total number of vowels is {total}!")
"""
"""
all_numbers = [3, 15, 7, 22, 9, 10, 18, 4]

new_num = []

for num in all_numbers:
    if num > 10:
        new_num.append(num)
print(f" Original list {all_numbers} ")
print(f"Numbers greater that 10: {new_num}")

"""
"""
sentence = "Programming is awesome in Python"
target = 'o'
total = 0

for o in sentence:
    if o.lower() in target:
        total += 1
print(f"The character 'o' appears {total} times in the sentence.")
"""
"""
original_string = "Python"
Reversed_string = ""

for i in range(len(original_string) -1,-1,-1):
    Reversed_string += original_string[i]
print(Reversed_string)
"""
"""
import random

secret_num = random.randint(1,100)

guess_count = 0

guess_limit = 10

while True:

    user = input("Enter a guess between 1 and 100 (q to quit): ").strip()
    if user.lower() == "q":
        print("Thanks for playing.")
        break
    else:

        try:
            num = int(user)
            guess_count += 1

            if num < 1 or num > 100:
                print("Out of range! Please enter a number between 1 and 100.")
                continue

            elif num == secret_num:
                print("===========================================")
                print(f"You are right! {secret_num} is the answer! ")
                print(f"You guessed it in {guess_count} attempts!  ")
                print("===========================================")
                break
            elif num > secret_num:
                print(f"Keep trying! {num} is a bit higher.")
                print(f"You have {guess_limit - guess_count} guesses left")
            else:
                print(f"You almost there! {num} is a bit lower.")
                print(f"You have {guess_limit - guess_count} guesses left")

            if guess_count == guess_limit:
                print("You hit the limit! Please try again.")
                print(f"The secret number was {secret_num}")

                play_again = input("Want to play again? (Y/N): ").strip(
                )
                if play_again.lower() == "y":
                    secret_num = random.randint(1, 100)
                    guess_count = 0
                    continue
                else:
                    break
        except ValueError:
            print(f"Invalid input. Please enter a number.")


"""
"""
start = False
while True:
    command = input("> ").lower()
    if command == "start":
        if start:
            print("Car is already started!")
        else:
            start = True
            print("Car is running...")
    elif command == "stop":
        if not start:

            print("Car is already stopped!")
        else:
            start = False
            print("Car stopped.")
    else:
        print("")
        break

"""

"""
my_list = ["apple","orange","pineapple","banana"]
my_list.remove("apple")
print(my_list, end=" ")
"""

"""
price = [10,20,30]

total = 0
for prices in price:
    total += prices

print(total)
"""
"""
for x in range(4):
    for y in range(3):
        print(f'{x},{y}')
"""
"""
numbers = [2,2,2,2,5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
"""
"""
name = ['John','Bob','Mosh','Sarah','Mary']
name[0] = 'Mark'
print(name[0:5])

"""
"""
numbers = [3,19,2,22,4,10]
max = numbers[0]

for number in  numbers:
    if number > max:
        max = number
print(max)
"""

"""
#1
numbers = [7, 15, 3, 9, 20, 1, 6]
small = numbers [0]

for number in numbers:
    if number < small:
        small = number
print(small)
"""
"""
#2
numbers = [4, 7, 10, 13, 8, 6, 5]
total = 0
for even in numbers:
    if even %2 == 0:
        total += 1
print(total)
"""
"""
#3
user = input("Enter a word: ")
print(user[::-1])
"""
"""
#4
numbers = [2, 5, 8, 3]
total = 0
for number in numbers:
    total += number
print(total)

"""

"""
numbers = []

max_attempt = 5

for i in range(max_attempt):

    user = int(input("Enter 5 random numbers: "))
    numbers.append(user)

max_num = numbers[0]

for number in numbers:
    if number > max_num:
        max_num = number
print(f"The greatest number is: {max_num}")

"""
"""
numbers = []
max_attempt = 5

for i in range(max_attempt):
    user = int(input(f"Enter number {i+1}: "))
    numbers.append(user)

max_num = numbers[0]
min_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number

print(f"The smallest number is :{min_num}")
print(f"The largest number is: {max_num}")
"""
"""
odd = 0
even = 0
num_list = []
max_attempt = 7

for i in range(max_attempt):
    user = int(input(f"Enter number {i+1}: "))
    num_list.append(user)

    if user %2 == 0:
        even += 1

    else:
        odd += 1

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
"""
"""

numbers = []
duplicates = []
max_attempt = 7


for i in range(max_attempt):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)



for number in numbers:
    if numbers.count(number)>1 and number not in duplicates:
        duplicates.append(number)

if duplicates:
        print("Duplicates:", ', '.join(map(str, duplicates)))
else:
        print("No duplicates found.")

"""
"""
numbers = []
even = 0
odd = 0
max_attempt = 5
for i in range(max_attempt):
    while True:
        try:
            user = int(input(f"Enter number {i+1}: "))
            numbers.append(user)

            if user %2 == 0:
                even += 1
            else:
                odd += 1
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

max_num = numbers[0]
min_num = numbers[0]

for number in numbers:
    if number > max_num:
        max_num = number
    elif number < min_num:
        min_num = number
average = sum(numbers) / len(numbers)

print(f"Average: {average}")
print(f"Largest: {max_num}")
print(f"Smallest: {min_num}")
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
"""
"""
while True:
    try:
        user = input(f"Choose operator (+ - * /) q to quit: ").lower()

        if user == "q":
            print("Thanks for playing.")
            break
        elif user not in ["+", "-", "*", "/"]:
            print("Invalid operator. Please choose from +, -, *, or /.")
            continue

        num1 = int(input("Enter first number: ").strip())
        num2 = int(input("Enter second number: ").strip())

        if user == "+":
            total = num1 + num2
            print(total)
        elif user == "-":
            total = num1 - num2
            print(total)
        elif user == "*":
            total = num1 * num2
            print(total)
        elif user == "/":
            if num2 == 0:
                print("Cannot be divide by zero. Please enter valid number.")
                continue
            total = num1 / num2
            print(total)
    except ValueError:
        print(f"Invalid input. Please try again.")
"""
"""
def format_result(result):
    if result == int(result):  # Check if result is whole number
        return int(result)     # Convert to int (remove .0)
    else:
        return result
while True:
    try:
        user = input("Choose operator ( + - * / ) q to quit: ").lower().strip()

        if user == "q":
            print("Thanks for playing.")
            break

        elif user not in ["+","-","*","/"]:
            print(f"{user} is invalid. Please choose valid operator.")
            continue

        num1 = float(input("Enter first number: ").strip())
        num2 = float(input("Enter second number: ").strip())

        if user == "+":
            total = num1 + num2
            print(f"Result: {format_result(total)}")
        elif user == "-":
            total = num1 - num2
            print(f"Result: {format_result(total)}")
        elif user == "*":
            total = num1 * num2
            print(f"Result: {format_result(total)}")
        elif user == "/":
            if num2 == 0:
                print(f"Cannot divide by zero. Please input valid number.")
                continue
            total = num1 / num2
            print(f"Result: {format_result(total)}")
    except ValueError:
        print(f"Invalid input. please try again.")
"""
"""

def format_result(value):
    if value == int(value):
        return int(value)
    else:
        return value

def add_number (x, y):
    return x + y

def subtract_number (x, y):
    return x - y

def multiply_number (x, y):
    return x * y

def divide_number (x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y
def thanks():
    return "Thanks for playing."

while True:
    user = input("Choose operator (+ - * /) q to quit: ").lower().strip()
    if user == "q":
        print(thanks())
        break
    elif user not in ["+", "-", "*", "/"]:
        print("Invalid operator.")
        continue

    try:
        first = float(input("Enter first number: ").strip())
        second = float(input("Enter second number: ").strip())

        if user == "+":
            results = add_number(first, second)
        elif user == "-":
            results = subtract_number(first, second)
        elif user == "*":
            results = multiply_number(first, second)
        elif user == "/":
            results = divide_number(first, second)
        results = None

        if isinstance(results, str):
            print(results)
        elif isinstance(results, (int, float)):
            print(f"Result: {format_result(results)}")
    except ValueError:
        print("Invalid input. Please try again.")

"""
"""
import random
def guess_game():
    secret_number = random.randint(1,50)
    attempts = 0
    guesses = []
    while True:
            guess = int(input("Enter guess (1, 20): "))

            if guess < 1 or guess > 20:
                print("Invalid input. Please enter number (1, 20)")
                continue
            guesses.append(guess)
            attempts += 1
            try:
                if guess < secret_number:
                    print(f"{guess} is too low. Try lower")
                elif guess > secret_number:
                    print(f"{guess} is too high, Try higher")
                else:
                    print(f"You are right! {guess} is the correct answer!")
                    print(f"You guessed it in {attempts} attempts!")
                    print(f"Your guesses: {guesses}")
                    break
            except ValueError:
                print("Invalid input. Please try again.")

guess_game()
"""
"""
numbers = []
evens = []
odds = []
def even():
    print("Even")
def odd():
    print("Odd")
while True:
    user = input("Enter a number (q to quit): ").strip().lower()


    if user == "q":
        print("================THANKS================")
        print(f"Entered numbers: {numbers}")
        print("")
        print(f"Even numbers: {evens}")
        print("")
        print(f"Odd numbers: {odds}")
        break
    try:
        num = int(user)
        numbers.append(num)
        if num %2 == 0:
            evens.append(num)
            even()

        else:
            odds.append(num)
            odd()

    except ValueError:
        print("Invalid input, please try again.")
"""
"""

numbers = []

attempts = 5

for i in range (attempts):
    user = int(input(f"Enter number {i+1}: "))
    numbers.append(user)
max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num =number
print(f"The largest number is: {max_num}")

"""
"""
def vowels_count(text):

    vowels = "aeiou"
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return count

print(vowels_count("Mark"))
print(vowels_count("Hello"))
print(vowels_count("ayala malls"))
"""
"""
import random
def guessing_game():
    secret_num = random.randint(1,20)
    attempts = 0
    max_attempts = 15
    guesses = []

    for i in range(max_attempts):
        user = input("Guess the number (q to quit): ").lower().strip()
        if user == "q":
            print("Thanks for playing!")
            break
        else:
            try:
                guess = int(user)
                if guess <1 or guess > 20:
                    print("Please enter (1,20)")
                    continue
                attempts += 1
                guesses.append(guess)
                if guess > secret_num:
                    print(f"Too high, try lower.")
                elif guess < secret_num:
                    print(f"Too low, try higher")

                else:
                    print(f"You are right! {guess} is the right answer!")
                    print(f"You guessed it in {attempts} attempts!")
                    print(f"Your guesses: {guesses}")
            except ValueError:
                print("Invalid input! please try again.")
    if attempts == max_attempts and (not guesses or guess[-1] != secret_num):
        print(f"Sorry, you've used all {max_attempts} attempts.")

"""

