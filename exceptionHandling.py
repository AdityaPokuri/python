a = int(input(" a:"))  
b = int(input(" b:"))  
c = (a/b);  
print("a/b = %d"%c)  

try:  
    a = int(input(" a:"))  
    b = int(input(" b:"))  
    c = a/b;  
    print("a/b = %d"%c)  
except Exception:  
    print("thats impossible")  
else:  
    print("block")   

