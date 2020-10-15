def highest_even(li):
	high = 0
	for i in li:
		if i%2 == 0:
			if i>high:
				high = i
	return high

print(highest_even([10,1,2,11,13]))