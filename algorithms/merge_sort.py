def algo(arr):
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
    
    import time
    start = time.time()
    msort(arr, 0, len(arr)-1)
    time_taken = time.time() - start
    return time_taken