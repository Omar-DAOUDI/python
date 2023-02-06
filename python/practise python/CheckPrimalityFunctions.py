
def prime():
    num =int( input ("enter a number  : "))
    xs = list(range(1,num+1))
    list_res=[]
    for x in xs :
        if num%x==0 :
            list_res.append(x)
    if len(list_res) == 2 :
        print("this number is  prime")   
    else :
            print("this number is not prime")   
    return list_res
print(prime())