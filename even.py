def even_no(x):
	return_list = []
	y=len(x)
	for i in range(0, y):
		if x[i]%2==0:
			return_list.append(x[i])
		
	return(return_list)

x = [1, 20, 18, 33, 19, 13, 22]
print(even_no(x), "contains only even_nos")