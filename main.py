from passwordGen import *
import pyperclip

password = RandomGen()

password.RandomLength()
print(password.finalPass)


def Copy():
    print("copy password ? (y/n)")
    inp = input()
    if inp == "y":
        pyperclip.copy(password.finalPass)
    elif inp == "Y":
        pyperclip.copy(password.finalPass)
    elif inp == "n":
        exit()
    elif inp == "N":
        exit()
    else:
        Copy()

Copy()
