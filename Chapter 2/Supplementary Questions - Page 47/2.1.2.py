#!/usr/bin/env python

#Design an algorithm that makes the following exchanges A -> B -> C -> A

var_A = 5
var_B = 10
var_C = 15

temp = var_C
var_C = var_B
var_B = var_A
var_A = temp

print var_A ,var_B , var_C
