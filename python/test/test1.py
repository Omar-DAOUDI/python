##list
friends = ["t","d","a"]
l = [1,59,68,89]
friends.append("creed")

##tuple
'''cordinates=(4,5)##tuple can ' tbe changed
print(cordinates[1])'''
#differnec between a lis and a tuple
#list are editable tuples are not
#tuples data that we don ' t want to change it

''' function '''
#functions have to be intendend in order to work

def cube(num):
    return num*num*num
''' If statment'''
'''is_male = True
is_tall= False
if is_male and  is_tall :
    print("you are a male and* tall  ")
elif is_male and not (is_tall):
    print("you are NOT  a male and* tall  ")
else:
    print("you are a female or short")'''
def max_num (n1,n2,n3):
    int(n1)
    int(n2)
    int(n3)
    res=0
    if n1>n2 and n1>n3:
        res=n1
    elif n1>n2 and n1<n3:
        res=n3
    elif n1<n3 and n1<n2:
        if n2>n3 :
            res=n2
        else:
            res=n3

    return res

mc={
    1:"january",
    2:"february",
    3:"march"
}
''' while statment'''
s="test"
n= len(s)
#u=input("enter a word of  :  "+str(n)+" characters")
def wileloop():
    while s!= u:
        print("error try agaun ")
        u = input("enter a word of " + str(n) + "characters")

''' for  statment'''
'''
b=int (input("enter the base"))
p=input("input the power ")
p=int(p)
res = 1
for i in range (p):
    res=res*b
print(res)
'''

'''2d List '''
'''
num_grid=[[1,6,8],
          [4,5,6],
          [2,8,9]]

for row in num_grid:
      for col in row:
        print(row)
'''
'''basic translator  '''
'''
def translate (phrase):
    translation =""
    for letter in phrase :
        if letter.lower() in "aeiou":
            translation=translation+"g"
        else :
            translation=translation+letter
    return translation
print(translate("test"))
'''

'''Try/Except  '''
''' try :
    ##value=10/0
    n=int(input("enter a number"))
    print(n)
except ValueError as err:
    print(err  )
except ZeroDivisionError as zrr:
    print(zrr)
    '''


''' files   '''
'''text = open("index .html","w")#r stand for read / w for writing a line to a txt file (it delet everything and write only the new line)/a for append(add items at the end )/r+ read and write
text.write(" <p> This is HTMl<p> ")


text.close()
'''

''' Modules and pip   '''
import main
print(main.roll_dice(10 ))
