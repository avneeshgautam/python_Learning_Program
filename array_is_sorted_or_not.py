def isSorted(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                return False
    return True

arr=[3,2,5,1,7]
n=5
print(isSorted(arr,n))

arr2=[1,2,3,4,5]
n=5
print(isSorted(arr2,n))
