import random
import string
'''i did it on th pc '''
sec_num=list("".join(random.choices((string.digits),k=4)))
print(sec_num)

i =0
j=0
b=0
numberguess=0
while j!=4 :
    num=list(input("enter  a 4 digit number "))
    while i<len(sec_num):
        
        if num[i]==sec_num[i]:
            j+=1
        else :
            b=b+1
        i+=1
    print(str(b))
    if j== 1 :
        print (" 1 cow,")
        print (str(b)+ " bulls")
    elif b==1:
        print ("1 bull")
        print (str(j)+ " cows")
    numberguess+=1
print(str(b)+"hello git")
print ("you win you used  "+str(numberguess))