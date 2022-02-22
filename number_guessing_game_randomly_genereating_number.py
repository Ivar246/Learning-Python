from mimetypes import guess_all_extensions
import random          #required for generating random number
n = 20
to_be_guessed = int(n * random.random())+1     #This generates random number
guess = 0
guess_limit = 3
guess_count = 0

print('''.......Alert!..........
.....You have three chances.....\n
      ''')

while guess != to_be_guessed and guess_count < guess_limit:
    guess = int(input("Enter your guess number: "))
    if guess > to_be_guessed:
        print("guess is larger.")
    elif guess < to_be_guessed:
        print("Your guess is smaller")
    else:
        print("Hurrah! you won..")
    guess_count += 1
    print('\n')
else: 
        print("sorry, chances up...\nyou lose... \nTry Again!")

