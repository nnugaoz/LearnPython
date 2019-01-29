# Filename:while.py
number = 25
running = True
while running:
    guess = int(input("Enter an integer:"))
    if guess == number:
        print("Congratulations! You guessed it.")
        print("But,you do not win any prizes.")
        running = False

    elif guess > number:
        print("The number is a litter lower than", guess)
    else:
        print("The number is a little higher than", guess)
print("Done!")
