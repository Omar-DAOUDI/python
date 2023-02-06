import random
'''
a = [1, 16, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,16]'''
'''generating list a using list range method'''
a = random.sample(range(87,99), 5)
print("the a list is :")
print(a)
"generating list b using random method "
b=[]
for  i in range(0,4):
    n=random.randint(87,99)
    b.append(n)
print("the b list is :")
print(b)
c=[]
''' old code 
for j in b :
    if j in a :
        c.append(j)
'''
'''code updated in one line '''
print("the c list is :")
c= [j for j in b if j in a ]
print(c)
'''exo 10 updated version of the code '''
print("the c list without duplicate is :")

c= [j for j in b if j in a ]

'''by turning the list to dictionnary we can remove duplicates since they can t have duplicates
then we we convert back the dictionnary to a list'''
c=list(dict.fromkeys(c))
print(c)

'''exo 7'''
'''mixed = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even=[c for c in a if c%2==0]
print(even)'''