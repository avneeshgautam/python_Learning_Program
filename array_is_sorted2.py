def isSorted(arr,n):
    for i in range(1,n):
        if(arr[i-1]>arr[i]):
            return False
    return True


arr=[2,4,1,5,7,3]
print(isSorted(arr,6))

a=[1,2,3,4]
print(isSorted(a,len(a)))
