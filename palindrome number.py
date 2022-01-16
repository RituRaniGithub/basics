i=int(input("enter numbrer:"))       #the reverse of number is the given number itself
rev=0
x=i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if(x==rev):
    print("palindrome number")
else:
    print("not palindrome")
