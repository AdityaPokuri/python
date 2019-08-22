#read and write code

with open('data.txt', 'r') as f:
    data = f.read()

with open('data.txt', 'w') as f:
    data = 'insert the textdata file'
    f.write(data)

##csv
import csv 

filename = "aapl.csv"
fields = [] 
rows = [] 
with open(filename, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile) 
	fields = csvreader.next()
    for row in csvreader:
        rows.append(row) 

	 
	print("no. of rows: %d"%(csvreader.line_num))
    print('Field names :' + ', '.join(field for field in fields))
    print('\nFirst 5 rows :\n')
    for row in rows[:5]:
        for col in row: 
            print("%10s"%col),
            print('\n')

            

##(https://www.rath.org/on-the-beauty-of-pythons-exitstack.html)

with ExitStack() as cm:
    res1 = acquire_resource_one()
    cm.callback(release_resource, res1)
    # do stuff with res1
    res2 = acquire_resource_two()
    cm.callback(release_resource, res2)
    # do stuff with res1 and res2