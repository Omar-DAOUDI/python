
''' EXO 1 character input '''
def century():
    name = input("enter ur name : ")
    age =int( input ("enter ur age : "))
    n =int( input ("enter ur number  : "))
    res= (100-age)+2023
   
    return n*("u will turn 100 on :" + str(res) +"\n")


''' EXO 2 odd or even '''

def odd_even():
    n =int( input ("enter ur number  : "))
    if n%2==0 :
        if n%4 == 0 :
            print("the number is a multiplication of 4 ")
        else:
            print("the number is even")
    else :
        print("the number is odd")
'''bonus '''
def devidable ():
    num =int( input ("enter a number  : "))
    check =int( input ("enter the check  number  : "))
    if num%check==0 :
        print("the : "+ str(num)+ " is a multiplaction of :"+str(check))
    else :
        print("the : "+ str(num)+ " is not a multiplaction of :"+str(check))
'''EXO 3  List Less Than Ten'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_mini=[]
for i in a :
    if i < 5 :
        a_mini.append(i)
#in one line :  a_mini=[i for i in a if i<5]


def less_than(number):
    return [x for x in a if x<number]

'''EXO 4  List Divisor'''
def divisor():
    num =int( input ("enter a number  : "))
    xs = list(range(1,num+1))
    list_res=[]
    for x in xs :
        if num%x==0 :
            list_res.append(x)
    print(list_res)


'''EXO 8  Rock paper scisors'''

player1= input ("player 1 enter a play   : ")
print(player1)
while player1 or "Scissors" or  player1 !="Paper" or player1 !="Rock" :
        player1= input ("player 1 enter a play   : ")
player2= input ("player 2 enter a play   : ")
while player2!="Scissors"or player2!="Paper" or player2!="Rock":
        player2= input ("player 2 enter a play   : ")

if player1 == "Rock" :
    if  player2 == "Scissors":
        print("player 1 is winner ")
    elif player2 == "Paper" :
        print("player 2 is winner ")
elif player1 == "Scissors " :   
    if  player2 == "Rock":
        print("player 2 is winner ")
    elif player2 == "Paper" :
        print("player 1 is winner ")
elif player1 == player2: 
        print("it s draw ")
elif player1 == "Paper" :
    if  player2 == "Rock":
        print("player 1 is winner ")
    elif player2 == "Scissors" :
        print("player 2 is winner ")

