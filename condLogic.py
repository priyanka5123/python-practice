x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Write a program where the user has to guess a secret number between 1 and 10. 
# The program should provide feedback if the guess is too high or too low and congratulate the user if they guess correctly.
import random
no = random.randint(1, 10)
userno = int(input("Guess the number: "))
if userno == no:
    print("Congratulations, You guessed the secret number!")
elif userno < no:
    print("Too Low!")
else:
    print("Too high!")