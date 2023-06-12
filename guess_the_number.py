import random

# you input a range for a random number to be generated within
low = int(input("Please enter the minimum value for the range of numbers: "))
high = int(input("Please enter the maximum value for the range of numbers: "))
secret_number = random.randint(low, high)

count = 0
# keeps looping until the number is guessed correctly
while True:
    guess = int(input(f"Please guess a number between {low} and {high}: "))
    if(guess == secret_number):
        count = count + 1
        print(f"You guessed the number in {count} tries")
        break
    else:
        count = count + 1
