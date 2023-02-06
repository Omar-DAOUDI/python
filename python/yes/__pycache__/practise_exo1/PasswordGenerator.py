import random
import string

def password_Generator():
    print("Welcome to password generator :  ")
    while True :
        ans=input("type yes  to generate a new password \ntype exit to stop the program \n")
        if ans=="yes":
            choix =int(input("1-strong password \n2-weak password \n choose : "))
            if choix==1:
                num=int(input("how much character u want \n "))
                password= "".join(random.choices((string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation),k=num))
                print("the password generated i s: "+str(password))
            else :
                weak_Password=["test","zest","ka7loch","hmar","azerty"]
                password=random.choice(weak_Password)
                print("the password generated i s: "+str(password))
            
        elif ans == "exit":
            break
password_Generator()