n = int(input())
k = int(input())
lsa = []
for i in range(0,n):
	i = int(input())
	lsa.append(i)
lsq = []
for j in range(0,k):
	j = int(input())
	lsq.append(j)
for x in lsq:
	flag = 0
	for y in lsa:
		if x == y:
			flag =1
			break
	if flag ==1:
		print('YES')
	else:
		print('NO')