



def elementSearch(l,n):
    i=0
    if n in l :
        return True 
    return False

'''using binary search '''
def find(l,n):
    si=0
    ei=len(l)
    while True:
        mi=(ei+si)//2 
        if mi < si or mi > ei or mi <  0:
            return False
        else :    
            middle_element=l[mi]
            if middle_element== n:
                return True
            elif middle_element>n:
                ei=mi-1
            elif middle_element<n:
                si=mi+1
if __name__=="__main__":
  l = [2, 4, 6, 8, 10]
  print(find(l, 5)) # prints False
  print(find(l, 10)) # prints True
  print(find(l, -1)) # prints False
  print(find(l, 2)) # prints True