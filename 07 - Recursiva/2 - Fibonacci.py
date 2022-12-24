def fibonacci(num: int):
	if num <= 1:
		return 1 
	else:
		 return fibonacci(num-1)+fibonacci(num-2)

for i in range(0,10):
	print(fibonacci(i))