#!/usr/bin/python

def fib(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fib(n-1)+fib(n-2)		
n=int(input("input: "))

for i in range(1,n+1):
	print("%d "%fib(i))
print("F%d = %d"%(n, fib(n)))
	

