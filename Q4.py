
l1 = []
# creating empty list  

# Taking input number of elements  user wants to put in list 
num = int(input("Enter number of elements in list: ")) 
  
 
for i in range(1, num + 1):   #Append elements in list 
    ele = int(input("Enter elements: ")) #taking user input and adding to the list 
    l1.append(ele) 

print("Largest element is:", max(l1))# print maximum element of list 
