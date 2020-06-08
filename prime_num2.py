
num=20

for i in range(1,num+1):
    n=0
    for j in range(1,i+1):
        if i%j==0:
            n+=1
            
    if n==2:
        print(i)
            