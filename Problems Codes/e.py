t = int(input())
li = []
for i in range(0,t):
	i = input()
	li.append(i)
print("OK")
j =0
for x in li:
	flag = 0
	counts =0
	nl = li[:j:]
	if j==0:
		j = j+1
		continue
	else:
		for i in range(0,j):
			if x == li[i]:
				flag = 1
				break
		if flag == 0:
			print("OK")
		else:
			counts = nl.count(x)
			print(f'{x}{counts}')
		j = j+1