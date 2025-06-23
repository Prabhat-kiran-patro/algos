import time

# for functions that do not return anything
def time_lapsed(func):
    def wrapper(*args, **kwargs):
        execution_time=0
        start_time=time.perf_counter_ns()
        func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        execution_time = end_time - start_time
        return execution_time
    return wrapper

# for functions that return something
def time_lapsed_re(func):
    def wrapper(*args, **kwargs):
        execution_time=0
        start_time=time.perf_counter_ns()
        value = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        execution_time = end_time - start_time
        return execution_time, value
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

class Searching():
    index = -1

    @time_lapsed_re
    def lin_search(arr, n):
        for i in range(len(arr)):
            if arr[i]==n:
                return i
        else:
            return f"{n} not found!"
    
    def binary_search(self, arr, n, l, r):
        if l>=r:
            return
        m=(l+r)//2
        if arr[m]>n:
            self.binary_search(arr, n, l, m-1)
        elif arr[m]<n:
            self.binary_search(arr, n, m+1, r)
        else:
            self.index=m
            return
    
    @time_lapsed_re
    def bin_search(self, arr, n):
        self.binary_search(arr, n, 0, len(arr)-1)
        return self.index

class TowerOfHanoi():
    def __init__(self):
        self.steps_to_take = []
    def steps(self, n, s='A', h='B', d='C'):
        if n==0:
            return
        self.steps(n-1, s, d, h)
        self.steps_to_take.append(s+" -> "+d)
        self.steps(n-1, h, s, d)
    @time_lapsed_re
    def towofh(self, n):
        self.steps(n)
        return self.steps_to_take