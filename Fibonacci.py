# -*- coding: utf-8 -*-
# ****************************************************************************************************
# Module functionality: Provides the solution to generate the Fibonocci sequence to a specific place *
# without using a loop.                                                                              *
# Author: Sai Priya Sudhi Reddy                                                                      *
# Version Number: 0.1                                                                                *
# Date of Creation:  1/07/2017                                                                       *                                                               
# ****************************************************************************************************

fibList=[]
def fibonocci(n):
    if n<2:
        return n
    return fibonocci(n-2) + fibonocci(n-1)

n=int(input("Enter the number to generate Sequence :"))

for i in range(n):
    fibList.append(str(fibonocci(i)))

print ", ".join(fibList)
