def bubble_sort(elements):
    size=len(elements)
    for i in range(size-1):
        swap=False
        for j in range(size-1-i):
            if elements[j]>elements[j+1]:
                elements[j], elements[j+1]= elements[j+1], elements[j]
                swap=True
        if not swap:
            break
     

elements=[]
size = int(input("Enter the size of array: "))
for i in range(size):
    value=int(input("Enter the elements in array: "))
    elements.append(value)

bubble_sort(elements)
print("Sorted Array: ")
for i in range(size): 
     print(elements[i], end=' ') 