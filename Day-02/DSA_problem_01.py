a=int(input())
for i in range(a):
    x,y,z=map(int,input().split(" "))
    print(2*min(y,z))

