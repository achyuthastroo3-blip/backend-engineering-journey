t=int(input())
for i in range(t):
    a,b,c=map(int,input().split(" "))
    ans=a+b+c
    print("YES" if ans==180 else "NO")

