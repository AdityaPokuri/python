## Assignment 1
#question 1

x_1 = 'Hello My name is "Rishabh". I love Coding'
print (x_1)

x_2 = "This is 'my first program'"
print(x_2)

x,y,z = input("Enter your values:").split()
print(("value_1= :",x))
print(("value_2= :",y))
print(("value_3= :",z))


##question_2
q_2= ['Hello! My name is XYX', '"Hello I am a candidate"','"234.56"', '"34"','a+3j']
print(*q_2, sep= "\n")

##question_3
x= 10+20*(45+67.0)
(print(x))
type(x)

x= (True and False) or False
print((x))
type(x)

x= (True or True) and ((not False) and True)
print(x)
type(x)

x= (3>89) or (34>32)
print(x)
type(x)

x= (not True) and False
print(x)
type(x)


##question 4
num1=int(input("Enter Number:"))
if((num1%3==0) & (num1%5==0) ):
    print("Hurray it is what I am looking for")
else:
    print("wrong input")


##question 5

n = int(input('enter a number:'))
if n in range(10, 50):
    print("Yes I am in the range")
else:
    print("oops")