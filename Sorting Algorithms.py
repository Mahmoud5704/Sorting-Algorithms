import time
import random


# In bubble sort we repeatedly compare adjacent elements and swap them if they are in the wrong order.
# For example, in the first iteration, we compare the first and second elements and swap them if they are in the wrong order.
# Then we compare the second and third elements and swap them if they are in the wrong order, and so on until we reach the end of the array.
# After the first iteration, the largest element will be in its correct position at the end of the array.
# In the second iteration, we repeat the process for the remaining unsorted part of the array, and so on until the entire array is sorted.
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False    
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:    
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True        
        if not swapped:
            break   

# In selection sort we have 2 part sorted and unsorted.
# we repeatedly select the smallest element from the unsorted part of the array and swap it with the first unsorted element.
# For example, in the first iteration, we find the smallest element in the entire array and swap it with the first element. 
# In the second iteration, we find the smallest element in the remaining unsorted part of the array and swap it with the second element, and so on.
# This process is repeated until the entire array is sorted.
def selectsort(arr):
    n=len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

# Here we sort the array by picking each element and finding its correct position in the already sorted portion.
# We save the current element as 'key', then shift all larger elements in the sorted portion one position to the right.
# This makes room for the key to be inserted at its correct position.
# This process is repeated for all elements in the array until the entire array is sorted.
def insertsort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  
            j -= 1
        arr[j + 1] = key

def split_merge(array,first,mid,last):
    #calculate size of each side and add 1 only to the array will take mid  
    left_size=mid-first+1
    right_size=last-mid
    #copy in another left and right array and there is from the disadvantges of merge sort(consume memory)
    left_array=[0]*left_size;right_array=[0]*right_size
    for i in range(left_size):  left_array[i]=array[first+i]
    for i in range(right_size): right_array[i]=array[mid+i+1]
    #now start comparison
    i=j=0
    k=first #not k equal 0,bec when we send indecies we send depend on its real position in original array 
    while(i<left_size and j<right_size):
      if(left_array[i]<right_array[j]):
         array[k]=left_array[i];i=i+1;k=k+1
      else:
          array[k]=right_array[j];j=j+1;k=k+1
    #look if there is any remained elements in any of them 
    #not bec one larger than one but it can be all elements of one them are samller than the other, so that there is remained elements
    while(i<left_size): array[k]=left_array[i];i=i+1;k=k+1
    while(j<right_size):array[k]=right_array[j];j=j+1;k=k+1

def merge_rec(array,first,last,limit):
    if(first<last):
        if(last-first+1<=limit and limit !=-1):
            copy=array[first:last+1]
            selectsort(copy)
            array[first:last+1]=copy
        else:
            mid=(last+first)//2  # plus not minus bec first_index not always equal 0 for ex. if we send 2,5 mid is 3 but is we use minus it will be 1 !!!
            merge_rec(array,first,mid,limit)
            merge_rec(array,mid+1,last,limit)
            split_merge(array,first,mid,last)

def hyprid_merge(array,first,last,limit):
    merge_rec(array,first,last,limit)

def merge_sort(array,first,last):
    merge_rec(array,first,last,-1)



def main():
    arr=[9,8,7,6,5,4,3,2,1]
    #merge_sort(arr,0,8)
    #hyprid_merge(arr,0,8,3)
    #selectsort(arr)

main()







"""
sizes = [10000,25000,50000,75000,100000,125000]

for size in sizes:
    print("testing for size: ", size)
    #generate random array of the given size
    #make copies of it for each sorting algorithm to ensure that they all sort the same data.
    original = [random.randint(0, size) for _ in range(size)]
    arr_bubble=original.copy()
    arr_select=original.copy()
    arr_insert=original.copy()
    # measure the time taken by each sorting algorithm 
    start = time.time()
    bubblesort(arr_bubble)
    end = time.time()
    t=end - start
    print(f"runtime of the bubble program is: {t} seconds")

    start = time.time()
    selectsort(arr_select)
    end = time.time()
    t=end - start
    print(f"runtime of the selection program is: {t} seconds")

    start = time.time()
    insertsort(arr_insert)
    end = time.time()
    t = end - start
    print(f"runtime of the insertion program  is: {t} seconds")
"""