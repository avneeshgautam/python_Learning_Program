arr=[1,5,3,7]
max=0
temp=0
for i in range(4):
    temp=max
    if(arr[i]> arr[max]):
        max=i
print(arr[temp])

