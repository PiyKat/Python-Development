#! python3

# A binary search algorithm using recursion

def binary_list(data,target,low,high):
    mid = int((low + high)/2)
    if(data[mid] == target):
        print("The element " + str(target) + " found at " + str(mid+1) + "th position")
    elif(data[mid] > target):
        
        binary_list(data,target,low,mid-1)
    else:

        binary_list(data,target,mid+1,high)
        


search_list = [2,4,5,7,8,9,12,14,17,19,22,25]
x = int(input("Enter the element that needs to be searched : "))

low = 0
high = len(search_list)-1

binary_list(search_list,x,low,high)
    
