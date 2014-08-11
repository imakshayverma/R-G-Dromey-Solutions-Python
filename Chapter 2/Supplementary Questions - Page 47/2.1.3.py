#!/usr/bin/env python

#Design an algorithm that makes the following exchanges A -> B -> C -> A


def swap(var_A,var_B, var_C, var_D):	
	temp = var_D
	var_D = var_C
	var_C = var_B
	var_B = var_A
	var_A = temp
	return var_A ,var_B , var_C, var_D

print "After Swapping" +  str(swap(1,2,3,4))
