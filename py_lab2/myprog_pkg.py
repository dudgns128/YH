#!/usr/bin/python
import my_pkg
import my_pkg

if __name__=='__main__':
	while True:
		print("Select menu: 1)conversion 2)union/intersection 3)exit?")
		n=int(input())
		if n==1:
			(my_pkg.g1())
		elif n==2:
			(my_pkg.g2())
		else:
			print("exit program")
			break
