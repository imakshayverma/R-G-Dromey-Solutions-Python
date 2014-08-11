f=open("test.txt",'w')
for i in range(10):
    f.write(str(i)+"\n")

f.close()

o=open("test.txt",'r')
t=o.read()
print t
o.close()
