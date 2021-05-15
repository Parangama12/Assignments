a=int(input())
m=[]
arr1=[]

for i in range(a):
    n=input().split(" ")
    m.append(n)
    arr1.append(input().split(" "))
    
for i in range(a):
    n=m[i]
    arr=arr1[i]
    for i in range(len(arr)):
        arr[i]=int(arr[i])
        
    arr.reverse()
    print(arr)