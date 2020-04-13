#!/usr/bin/python

sum=0
n=int(input("input: "))
for i in range(0,n):
	num=float(input("%dth score: "%(i+1)))
	sum=sum+num
avr=sum/n
print("average: %f"%avr)

