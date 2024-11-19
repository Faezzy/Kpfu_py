from os import setns
from resource import struct_rusage
from unittest import removeResult


# age = 19
# name = (input("Her "))
# print(name + "string")
# print(name.upper())
# print(name.lower())
# print(name.find("a"))
# print(name.replace("z", "zz"))
# print(f"Name: {name}")
# str_template = "User information: {0} - {1}"
# print(str_template.format(name, age))
# lst = [1,2,3];
# # print(lst[-1]);
# # list.append();
# # list.remove();
# list_console = input("Enter list without spaces: ")
# numbers = list_console.split(" ")
# # print(print(numbers))
# # tup = (1,2,3)
# # print(tup)
# # print(tup[0])
# first, second, third = tup
# eng_rus_duct = {"cat" : "кот", }
# set_from_list = set(lst)
# set_example = {1, 2, 3}
# print(set_example)
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

