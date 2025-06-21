import time
def algo(arr):
    start=time.time()
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
    time_taken = time.time() - start
    return time_taken