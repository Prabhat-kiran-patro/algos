import time

def algo(arr):
    start = time.time()
    n = len(arr)
    for i in range(1, n):
        j=i-1
        key=arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    time_taken = time.time() - start
    return time_taken