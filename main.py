import re

testCase1 = "-10 * x^0 + 5 * x^1 - 3 * x^2 = 5 * x^0 + 3 * x^1"
preinput = testCase1.replace(" ", "").replace("*", "")

degree = {
    "0": 0,
    "1": 0,
    "2": 0
}

def calcu(num, sign):
    split = num.split("x^")
    if len(split) == 1:
        return
    for key in degree.keys():
        if split[1] == key:
            degree[key] += int(split[0]) * sign

def convert():
    for key in degree.keys():
        num = ""
        if degree[key] > 0 and key != "0":
            num += "+"
        num += str(degree[key])
        if key != "0":
            num = num[:1] + " " + num[1:]
        degree[key] = num

start = 0
sign = 1
for i in range(len(preinput)):
    if re.search("^\\+|-|=$", preinput[i]) or i == len(preinput) - 1:
        num = ""
        if i == len(preinput) - 1:
            num += preinput[start:i + 1]
        else:
            num += preinput[start:i]
        calcu(num, sign)
        start = i

        if preinput[i] == '=':
            sign = -1
            start += 1
convert()

print(f'\"{degree["0"]} * X^0 {degree["1"]} * X^1 {degree["2"]} * X^2 = 0\"')