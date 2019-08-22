### question 1
circle_ls = [1,2,3,4, 5, 6, 7,8,9,10] 
 
print ("The original list is : " + str(circle_ls)) 
  
K = 19

res = [x + K for x in circle_ls] 

  
print ("The list after adding pillow number to each element : " +  str(res))

for a in res:
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)

###question 2

list_a = [ 'Maria', 'Kenya', 'Amee', 'Angelina']
list_b = ['John' , 'Harry' , 'Peter', 'Mark']
finalList = list(zip(list_a, list_b))
print(finalList)

##question3
salary=100
leaves = 10
workedHours= 8
leavesTaken= 1
noOfDays= 20
dailyWage= workedHours*salary

totalSalary= workedHours*salary*noOfDays 

if leaves>leavesTaken:
    print(totalSalary)
else:
    print(totalSalary-dailyWage)


###question4
x = ['a','b','c','d','f','g','h']

for index,y in enumerate(x):
    print(index,y)
a

list1=range[1,7]
x['a','b','c','d','f','g','h'] += 1

##
for x in ['a','b','c','d','f','g','h']:
    for i in ['a','b','c','d','f','g','h']:
        if x % i == 0:
            break
    else:
        print(x),
        print('Done')