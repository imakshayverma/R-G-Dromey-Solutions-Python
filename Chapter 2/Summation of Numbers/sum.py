
#Program to calculate the sum of user entered numbers
def calc_sum(total_count):
    i = 0
    sum = 0
    while i< total_count:
        temp_var = int(raw_input("Enter the number - "))
        sum = sum + temp_var
        i=i+1

    print "The sum of numbers is - " + str(sum)



t = int (raw_input("Enter the Total numbers you want to calculate - "))
calc_sum(t)
