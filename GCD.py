#--------------------------------------------
# Author: Chelsie Martinear
# Date: 4 Dec 2015
# Purpose: The purpose of this program is to 
# find the greatest common divisor (GCD) of 
# two integers (input by the user) using the
# Euclidean algorithm
#--------------------------------------------


#!/usr/bin/env python


#intializes and prompts user for inputs
int1String = input("Please enter the first integer: ")
int1 = int(int1String)
int2String = input("Please enter the second integer: ")
int2 = int(int2String)

#initialize variables
a,b,q,r = (0,0,0,0)

print("") #prints new line

#Finds the greatest common divisor using
#Euclidean algorithm
if int1 > int2:
	a = int1
	b = int2
	q = int(a/b)
	r = a - b*q
	print(a," = ",b,"*",q," + ",r)
else:
	a = int2
	b = int1
	q = int(a/b)
	r = a - b*q
	print(a," = ",b,"*",q," + ",r)

#loops until remainder is equal to zero
while r != 0:
	a = b
	b = r
	q = int(a/b)
	r = a - b*q
	print(a," = ",b,"*",q," + ",r)

gcd = b

#prints the greatest common divisor
print("GCD: ",gcd)

import os
os.system("pause")
