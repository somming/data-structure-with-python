def factorial(n):
	if n <= 1:
		return 1


	return factorial(n-1)*n

def fibonacci(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1

	return fibonacci(n-2) + fibonacci(n-1)

if __name__ =="__main__":
	#n=3
	#res = factorial(n)
	#print("The factorial of {} is {}".format(n,res))

	n = 10
	for i in range(1,n+1):
		print(fibonacci(i),end=' ')