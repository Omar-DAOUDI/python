import random

print("welcome to the guessing game [1,9]")
g=0
while True : 
    rn=int(random.randint(1,9))
    a=float(input("Enter ur guessing "))
    if a==rn:
        print ("U guessed right\nThe game  end ")
    elif a>rn:
        print ("U guessed too high ")
    elif a<rn:
        print ("U guessed too low ")
    g=g+1
    print("You took "+ str(g)+" guesses")
    usr_command = input("Enter your command: ")
    if usr_command == "exit":
        print("The game  end")
        break
