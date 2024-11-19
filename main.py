from os import setns
from resource import struct_rusage
from unittest import removeResult

from wx.lib.masked import control


def calc():
    hist = {"+": [], "-":[], "*": [], "/": []}
    while True:
        try:
            num1 = float(input())
            num2 = float(input())
            operate = input().strip()
            if operate == "+":
                ans = num1 + num2
                hist["+"].append(f"{int(num1) if num1.is_integer() else num1} + {int(num2) if num2.is_integer() else num2} = {int(ans) if ans.is_integer() else ans}")
            elif operate == "-":
                ans = num1 - num2
                hist["-"].append(f"{int(num1) if num1.is_integer() else num1} - {int(num2) if num2.is_integer() else num2} = {int(ans) if ans.is_integer() else ans}")
            elif operate == "*":
                ans = num1 * num2
                hist["*"].append(f"{int(num1) if num1.is_integer() else num1} * {int(num2) if num2.is_integer() else num2} = {int(ans) if ans.is_integer() else ans}")
            elif operate == "/":
                if num2 != 0:
                    ans = num1 / num2
                    hist["/"].append(f"{int(num1) if num1.is_integer() else num1} / {int(num2) if num2.is_integer() else num2} = {int(ans) if ans.is_integer() else ans}")
                else:
                    print("Zero division!")
                    continue
            else:
                print("Incorrect operation")
                continue
            print(f"{int(num1) if num1.is_integer() else num1} {operate} {int(num2) if num2.is_integer() else num2} = {int(ans) if ans.is_integer() else ans}")
            for operations in hist:
                if hist[operations]:
                    print(f"{operations} {hist[operations]}")
        except ValueError:
            print("Incorrect Values")
calc()
