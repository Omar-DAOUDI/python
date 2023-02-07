
'''word="123456789"
print(word[0:10:step]) print element from list passing by step '''
word=input("enter a word ")
word=str(word)
'''print a  word backword'''
rvs=word[::-1]
if rvs == word:
    print("it s a palindrome  ")
else :
    print("it s not a palindrome  ")

