
'''methode 1'''
def rvrword(s):
    return " ".join(s.split(" ")[::-1])


'''methode 2'''
s="My name is Michele"
res=s.split()
res.reverse()
print(" ".join(res))