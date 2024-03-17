def findMin(x):
	y = len(x);
	for i in range (0, y-1):
		if x[i] < x[i+1]:
			temp = x[i];
			x[i] = x[i+1];
			x[i+1] = temp;
		else:
			print(x);
	print(x[y-1], x, "is the minimum number")
	return x[y-1]


x = [5, 20, 10, 50, 40];
min_number = findMin(x)
print(min_number,"is the minimum number");
