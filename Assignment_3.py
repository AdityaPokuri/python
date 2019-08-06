##question1
sentence = 'This is a sentence'
word=""
for w in sentence :
    if w.isalpha():
        word=word+w

    elif not w.isalpha():
      print(word)
      word=""
print(word)


##question1.2
def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))


list_test = ['i','love','to','code',' in','python']
quicksort(list_test)

##question1.3

##question3
#bubble sort
mylist = [8,5,99,48,12, 5, 13, 8, 9, 65]

def bubble(unsortedlist):
    length = len(unsortedlist) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if unsortedlist[i] > unsortedlist[i+1]:
                sorted = False
                unsortedlist[i], unsortedlist[i+1] = unsortedlist[i+1], unsortedlist[i]

bubble(mylist)
print(mylist) 

#Quick sort

def quicksort(data):
        if(len(data) < 2):
                return data
        else:
                pivot = data[0]
                
                re = data[1:]
                low = [each for each in re if each < pivot]
                high = [each for each in re if each >= pivot]
                return quicksort(low) + [pivot] + quicksort(high)

items=[2,77,9,40,0,4,9,11,2,0] 
print(quicksort(items))


##Selection sort
arr = [5,4,3,1,6,5,66,75,36,8,10,9]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if(arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

print(arr)

##merge sort


def mergesort(sqnce):
    
    if len(sqnce) < 2:
        return sqnce

    mid = len(sqnce) // 2 

    left_sequence = mergesort(sqnce[:mid])
    right_sequence = mergesort(sqnce[mid:])

    return merge(left_sequence, right_sequence)

def merge(left, right):
    
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output += left[i:]
    output += right[j:]

    return output


print(mergesort([1,4,6,3,2,5,78,4,2,1,4,6,8]))