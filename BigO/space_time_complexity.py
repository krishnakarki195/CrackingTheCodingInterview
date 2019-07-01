# Big O notation references

def f(n):
	for i in range(0,n):
		print(i)

# O(n)


def f1(n):
	if n <= 1:
		return 1
	return f(n-1) + f(n-1)
# O(2^n)


def f2(n):
	for i in range(0,n):
		for j in range(i+1,n):
			print(j)

# (n-1) + (n-2) + (n-3) + .... + 1
# n(n-1)/2
# O(n^2)


def f3(n,m):
	for i in range(0,n):
		for j in range(0,m):
			print(j)

# O(n*m)


def f4(n):
	for i in range(0,n):
		for j in range(0,1000):
			print(j)

# O(n)

def sum(node):
	if node == null:
		return 0
	sum(node.left) + node.vlaue + sum(node.right)

#for binary tree O(branches^depth)
#binary tree depth is roughly lon n
# O(2^lon n) => O(n)
# therefore the runtime of this code is O(n), where n is number of nodes

def isPrime(n):
	for i in range(2,math.sqrt(n)):
		if n % i == 0:
			return False
# O(sqrt(n))

def factorial(n):
	if n < 0 :
		return -1
	elif n == 0 :
		return 1
	else:
		return n * factorial(n-1)

# O(n)

def fibonacci(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

"""
O(n+p), where p < n/2 => O(n)
O(2n) => O(n)
O(n + log n) => O(n)
O(n + m) => O(n + m)
"""
