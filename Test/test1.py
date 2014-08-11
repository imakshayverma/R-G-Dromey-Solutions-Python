f =open("test.txt", "w+")
for i in range(10):
	f.write("%d \n" %i)
f.close()
