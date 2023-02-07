
a = [1, 1,1, 2, 89, 5, 55, 13, 21,55, 55, 89]
def rd1(n):
    
    return list(set(n))

def rd2(n):
    i=0
    while i < len(n):
        j=i+1
        while j<len(n):
            if n[i]==n[j]:
                
                n.remove(n[i])
                
                
            j+=1
        i+=1
    return n
