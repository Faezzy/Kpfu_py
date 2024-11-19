from os import setns
from resource import struct_rusage
from unittest import removeResult

def calc():
    num1 = float(input())
    num2 = float(input())
    operate = input()
    if operate == "+":
        ans = num1 + num2
    elif operate == "-":
        ans = num1 - num2
    elif operate == "*":
        ans = num1 * num2
    elif operate == "/":
        if(num2 != 0):
            ans = num1 / num2
        else:
            ans = "Zero division!"
    else:
        ans = "Unknown operation!"
    print(f"Result: {ans}")

