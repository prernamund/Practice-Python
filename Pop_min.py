x = [5, 20, 10, 50, 40];
y = len(x);
for i in range (0, y-1):
	if x[i] < x[i+1]:
		temp = x[i];
		x[i] = x[i+1];
		x[i+1] = temp;
		print(x);
	print(x[y-1], "is the minimum number")

	