arr=list(map(int,input().split())) # creating a list of integers from user input
count=0 # The problem want to find the number of elements greater than or equal to 10. So we will initialize a counter variable count to 0. 
for i in range(4):
    if arr[i]>=10:
        count+=1
print(count)

