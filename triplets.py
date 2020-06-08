x=[2,5,3,4,8,7,8]

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]<x[j]:
            x[i],x[j]=x[j],x[i]
print(x)