m=int(input())
l=list(map(int,input().split()))
n=int(input())
l1=[]
for i in range(n):
    e=int(input())
    l1.append(e)
#print(l1)    
for i in range(n):
    print(l.pop(l1[i]-1))
