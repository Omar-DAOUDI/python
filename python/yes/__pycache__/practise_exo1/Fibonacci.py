import random

num=int(input("how many Fibaonnaci numbers to generate "))


def Fibonnaci():
    xn=0 
    xnp=0
    xnn=1
    result=[]
    for i in range(0,num):
        if i==1:
            result.append(i)
        xn=xnp+xnn
        xnp=xnn
        xnn=xn
        result.append(xn)
    return result

def fibo(n):
    if n<=1 :
        return n
    return fibo(n-1)+fibo(n-2)

resultat=[]
i=1
while i<num :

    resultat.append(fibo(i))
    i+=1
print(resultat)

'''

def Fibonnaci(n):
    i=1
    res=0
    previous=0
    next=1
    if n<=1 :
        return n
    while i<n:
        res=next+previous
        previous=next
        next=res       
        i+=1
    return res
'''