import time
import random


##############################################################################################################

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

def selectsort(arr):
    n=len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

def insertsort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  
            j -= 1
        arr[j + 1] = key

###############################################################################################################

def split_merge(array,tmp,first,mid,last):
    #start comparison
    i=k=first
    j=mid+1
    while(i<=mid and j<=last):
      if(array[i]<array[j]):
          tmp[k]=array[i];i=i+1
      else:
          tmp[k]=array[j];j=j+1
      k+=1
    #look if there is any remained elements in any of them 
    while(i<=mid):  tmp[k]=array[i];i+=1;k+=1
    while(j<=last): tmp[k]=array[j];j+=1;k+=1
    for i in range(first, last+1):
     array[i] = tmp[i]

def merge_rec(array,tmp,first,last,limit):
     if(first<last):
        if(last-first+1<=limit):
            copy=array[first:last+1]
            selectsort(copy)
            array[first:last+1]=copy
        else:
            mid=(last+first)//2  # plus not minus bec first_index not always equal 0 for ex. if we send 2,5 mid is 3 but is we use minus it will be 1 !!!
            merge_rec(array,tmp,first,mid,limit)
            merge_rec(array,tmp,mid+1,last,limit)
            split_merge(array,tmp,first,mid,last)

def hyprid_sort(array,first,last,limit):
    tmp=[0]*len(array)
    merge_rec(array,tmp,first,last,limit)

def merge_sort(array,first,last):
    tmp=[0]*len(array)
    merge_rec(array,tmp,first,last,-1)

###############################################################################################################

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    # choose the pivot
    pivot = arr[high]

    # index of smaller element and indicates
    # the right position of pivot found so far
    i = low - 1

    # traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1

# the QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)

        # recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def kth_smallest(arr, k):
        low = 0
        high = len(arr) - 1

        while True:
            pos = partition(arr, low, high)

            if pos == k - 1:
                return arr[pos]
            elif pos > k - 1:
                high = pos - 1
            else:
                low = pos + 1

###############################################################################################################    




def main():
    arr=[9,8,7,6,5,4,3,2,1]
    #merge_sort(arr,0,8)
    #hyprid_sort(arr,0,8,3)
    #selectsort(arr)
    print(arr)

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