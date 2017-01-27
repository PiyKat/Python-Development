#! python3
# Bubble Sort(runs in O(n^2) worst case)

def insert_sort():

    array = [2,18,19,13,9,5,23,4,6,8,10,1,16,20,11]

    for i in range(1,len(array)):

        curr = array[i]
        j = i
        while(j > 0 and array[j-1] > curr):
            array[j-1] = array[j]
            j-=1
        array[j]= curr

    print(array)

insert_sort()


