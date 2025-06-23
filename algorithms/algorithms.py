import time

def time_lapsed(func):
    execution_time=0
    def wrapper(*args, **kwargs):
        start_time=time.perf_counter_ns()
        func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        execution_time = end_time - start_time
        return execution_time
    return wrapper


class Sorting():

    @time_lapsed
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(n-1-i):
                if(arr[j]>arr[j+1]):
                    arr[j+1], arr[j] = arr[j], arr[j+1]
    
    @time_lapsed
    def insertion_sort(arr):
        n = len(arr)
        for i in range(1, n):
            j=i-1
            key=arr[i]
            while j>=0 and arr[j]>key:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key
    
    @time_lapsed
    def merge_sort(arr):
        def merge(arr, l, m, r):
            temp=[]
            left = l
            right = m+1
            while left<=m and right<=r:
                if arr[left]<=arr[right]:
                    temp.append(arr[left])
                    left+=1
                else:
                    temp.append(arr[right])
                    right+=1
            while left<=m:
                temp.append(arr[left])
                left+=1
            while right<=r:
                temp.append(arr[right])
                right+=1
            for i in range(l, r+1):
                arr[i] = temp[i-l]
        def msort(arr, l, r):
            if l>=r:
                return
            m = (l+r)//2
            msort(arr, l, m)
            msort(arr, m+1, r)
            merge(arr, l, m, r)
    
    @time_lapsed
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            mini = i
            for j in range(i, n):
                if arr[j]<arr[mini]:
                    mini=j
            arr[i], arr[mini] = arr[mini], arr[i]
            

