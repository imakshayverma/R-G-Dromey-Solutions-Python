#!/usr/bin/env python

#Given Two variables of integer type A and B, exchange their values without using a third temporary Variable.


def swap(var_A,var_B):	
	var_A = var_A + var_B
	var_B = var_A - var_B
	var_A = var_A - var_B
	return var_A ,var_B 

print "After Swapping" +  str(swap(1,2))
