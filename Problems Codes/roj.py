test = int(input())

while test>0:
	test = test-1
	health = int(input())
	power = int(input())
	while health>0 and power>0:
		health = health - power
		power = int(power/2)
	if health <= 0:
		print('1')
	if health >0:
		print('0')