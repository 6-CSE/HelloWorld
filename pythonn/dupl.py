some_list = ['a','b','c','d','b','m','n','n']
empty_list1 = []
empty_list2 = []
for item in some_list:
	i =0
	for new_item in empty_list1:
		if item == new_item:
			i =1
			break
		else:
			i = 0
	if i == 0:
		empty_list1.append(item)
	else:
		empty_list2.append(item)

print(empty_list2)