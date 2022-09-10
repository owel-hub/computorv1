import re

testCase1 = "10 * x^0 + 5 * x^1 - 3 * x^2 = 5 * x^0 + 3 * x^1"

preinput = testCase1.replace(" ", "").replace("*", "")

zero = one = two = 0

def calcu(num, isReverse = 1):
    global zero, one, two

    split = num.split("x^")
    if split[1] == '0':
        zero += int(split[0]) * isReverse
    elif split[1] == '1':
        one += int(split[0]) * isReverse
    elif split[1] == '2':
        two += int(split[0]) * isReverse

def convert():
    global zero
    global one
    global two

    if zero == 0:
        zero = ""

    if one == 0:
        one = ""
    elif one > 0:
        one = "+ " + str(one)
    elif one < 0:
        one *= -1
        one = "- " + str(one)

    if two == 0:
        two = ""
    elif (two > 0):
        two = "+ " + str(two)
    elif two < 0:
        two *= -1
        two = "- " + str(two)

tokenIndex = 0
equalFlag = False
for index, item in enumerate(preinput):
    isEnd = 0
    if re.search("^\\+|-|=$", item) or index == len(preinput) - 1:
        if index == len(preinput) - 1:
            isEnd = 1
        if (equalFlag == True):
            calcu(preinput[tokenIndex:index + isEnd], -1)
        else:
            calcu(preinput[tokenIndex:index + isEnd])
        tokenIndex = index
        if item == '=':
            equalFlag = True
            tokenIndex = index + 1
convert()

print(f'\"{zero} * X^0 {one} * X^1 {two} * X^2 = 0\"')