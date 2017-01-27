#! python3
# Bubble Sort(runs in O(n^2) worst case)

def bubble_sort():

    array = [2,18,19,13,9,5,23,4,6,8,10,1,16,20,11]

    for i in range(len(array)):

        for j in range(i+1,len(array)):

            if array[i] > array[j] :

                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    print(array)

bubble_sort()


