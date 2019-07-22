##question1


##question2

for i in range(1,21):
    print(i, i+2)

##questin3

from collections import Counter
x=Counter('hello&*$$world')
print(x)

##question4
lower=int(input("Enter the lower limit for the range:"))
upper=int(input("Enter the upper limit for the range:"))
for i in range(lower,upper+1):
  if(i*i*i in range(lower,upper+1)):
    print(i)

##question5


##question6
s = "Hello world I am learning python"
x=[len(x) for x in s.split()]
print (x)

##question7
test = input("Enter Valur: ")
if test.isdigit() == True:
   print("True")
else:
   print("False")