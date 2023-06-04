import random
name=input("what is your name? \n")
print(f"well {name} i was thinking of a number between 1 and 15")
secret_number=random.randint(1,15)
for guessestaken in range(0,6):
    guess=int(input(f"enter a number {name}\n"))
    if guess < secret_number:
        print("try a higher number")
    elif guess > secret_number:
        print("try a lower number")
    else:
        break
if guess==secret_number:
    print("you chose the correct number, you have won the game.")
else:
    print("you could not choose the correct number, try again.")
    print(f"the correct number was {secret_number}")
          
    
