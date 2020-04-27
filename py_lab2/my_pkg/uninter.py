#!/usr/bin/python
import re
def g2():

	print("1st list: ")
	a=input()
	rea=[int(s) for s in re.findall(r"\b\d+\b",a)]
	print("2nd list: ")
	b=input()
	reb=[int(s) for s in re.findall(r"\b\d+\b",b)]
	set1=list(set(rea)|set(reb))
	set2=list(set(rea)&set(reb))

	print("=> union ",set1)
	print("=> intersection ",set2)



