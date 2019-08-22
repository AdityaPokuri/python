###multithreading

import threading 
  
def print_cube(num): 
    """ 
    printing cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    printing square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=print_square, args=(10,)) 
    t2 = threading.Thread(target=print_cube, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!")



###fibanoccie

a = int(input('Give amount: '))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(a)))

###Serilization

import marshal
peson = {"name":"gr", "age":234, "marks":[45,56,78]}
data = marshal.dumps(peson)
obj = marshal.loads(data)
print (obj)

## min max

def minimaxe (x):
     
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum: 
            minimum = i 
        else: 
            if i > maximum: maximum = i
    return (minimum,maximum)

print(minimaxe([9,8,23424,45,235,5235,23523,325235,5211,16,17,18,19]))
print(minimaxe([1]))
print(minimaxe([2, 23,34,5,66,7,77,1,-2]))