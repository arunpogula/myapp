def pairs(k,arr):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]-arr[j]==k or arr[j]-arr[i]==k:
                count+=1
    print(count)
pairs(3  ,[2,3,4,5,6,8])
                