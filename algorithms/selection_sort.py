import time

def algo(arr):
    start = time.time()
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i, n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i], arr[mini] = arr[mini], arr[i]
    time_taken = time.time() - start
    return time_taken