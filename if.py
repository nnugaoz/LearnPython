# Filename:if.py
number = 23
guess = int(input("Enter an integer:"))
if guess == number:
    print("Congratulations! You guessed it.")
    print("but, you don't win any prizes!")
elif guess > number:
    print("the number is less than",guess)
else:
    print("this number is higher than",guess)
print("Done!")
