file=open("Example.txt","r")
print(file.readline())
file.close()

file=open("Example.txt","w")
file.write("Namastey")
file.close()

file=open("Example.txt","a")
file.write("Bagunarra")
file.close()
