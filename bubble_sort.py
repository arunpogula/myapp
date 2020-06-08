x=[3,2,5,4]

l=len(x)


for i in range(l):
    for j in range(i+1,l):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
            print(x)
    