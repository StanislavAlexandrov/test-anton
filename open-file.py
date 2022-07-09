import os
import sys
# f=open("c:/Users/anlyn/test-anton/my-text.txt","rt")
file = os.path.join(sys.path[0],"my-text.txt")
f=open(file,"rt")

print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
rline = (f.readline())
f.close

f=open(file,"at")

f.write("NNN"+rline+"new line")
f.close

