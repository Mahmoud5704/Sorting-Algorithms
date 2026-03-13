def build_heap(A,n):
    n = len(A)
    for i in range(n//2,0,-1):

        heapify(A,n,i)

def heapify(A,n,i):
    largest=i
    left=2*i
    right=2*i+1
    if left<n and A[left]>A[largest]:
        largest=left
    if right<n and A[right]>A[largest]:
        largest=right
    if largest !=i:
        A[i],A[largest]=A[largest],A[i]
        heapify(A,n,largest)
def heap_sort(A):
    n=len(A)-1 #start from index 1
    build_heap(A,n)
    for i in range (n,1,-1):
        A[1],A[i]=A[i],A[1]
        heapify(A,i-1,1)


A = [0, 4, 10, 3, 5, 1]
heap_sort(A)
print(A[1:])


