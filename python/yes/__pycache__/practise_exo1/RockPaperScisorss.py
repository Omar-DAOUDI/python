''' Rock Paper Scissors '''

usr_command = True

while usr_command : 
    player1= input ("player 1 enter a play   : ")
    
    while player1 != "Scissors" and  player1 !="Paper"and  player1 !="Rock"  :
            player1= input ("player 1 enter a play   : ")
    player2= input ("player 2 enter a play   : ")
    while player2!="Scissors" and player2!="Paper" and  player2!="Rock":
            player2= input ("player 2 enter a play   : ")
    

    if player1 == player2: 
            print("it s draw ")
    elif player1 == "Rock" :
        if  player2 == "Scissors":
            print("player 1 is winner ")
        elif player2 == "Paper" :
            print("player 2 is winner ")
    elif player1 == "Scissors " :
        if  player2 == "Rock":
            print("player 2 is winner ")
        elif player2 == "Paper" :
            print("player 1 is winner ")
    
    elif player1 == "Paper" :
        if  player2 == "Rock":
            print("player 1 is winner ")
        elif player2 == "Scissors" :
            print("player 2 is winner ")
    
    usr_command = input("Enter your command: ")
    if usr_command == "quit":
      break


    
