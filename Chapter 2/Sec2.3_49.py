

def calc():
	print 
	stu_num = int(raw_input("Enter the number of students -"))
	pass_count = stu_num
	i=0
	while i < stu_num :
		i=i+1
		temp_marks = int(raw_input("Please enter your marks - "))
		if temp_marks <= 33:
			pass_count = pass_count-1

	print "Total Number of students Passed - " + str(pass_count)

calc()
