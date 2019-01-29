# Filename:break.py
while True:
    s = input("Please enter something:")
    if s == "quit":
        break
    else:
        print("The length of",s,"is",len(s))
