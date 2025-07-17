from random import randrange

rand = randrange(0, 10)
print(rand)
not_guessed=True
if not isinstance(rand, int):
    print("You need to put an integer!")
while not_guessed:
    user_guess=input("Guess a number(from 0 to 9): ")
    try:
        number=int(user_guess)
        if int(user_guess) == rand:
            not_guessed = False
    except ValueError:
        print(f"Its not an integer!")




print("Guessed correctly!")

