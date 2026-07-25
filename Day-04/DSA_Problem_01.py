t=int(input())
for _ in range(t):
    x,y,x1,y1=map(int,input().split(" "))
    
    alex=x*x+y*y 
    bob=x1*x1+y1*y1
    
    if alex>bob:
        print("ALEX")
    elif bob>alex:
        print("BOB")
    else:
        print("EQUAL")


#Tip: when we want to compare the distance of two points from the origin, we can use the formula for distance which is sqrt(x^2 + y^2). However, since we are only comparing distances, we can skip the square root and just compare x^2 + y^2 for both points. This will give us the same result without the need for calculating the square root. 