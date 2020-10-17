# Uses python3
import sys

def gcd_euclid(a, b):
	if a == 0 :       #base case
		return b
	return gcd_euclid(b%a, a) # recursive case

#Test cases:
print('GCD of 5,5 is '+str(gcd_euclid(5,5)))
print('GCD of 8,24 is '+str(gcd_euclid(8,24)))
print('GCD of 57,21 is '+str(gcd_euclid(57,21)))
