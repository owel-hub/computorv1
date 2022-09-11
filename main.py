import re
import sys

def getMaxDegree():
    max_degree = -1
    for key in dict_degree.keys():
        key_int = int(key)
        if key_int > max_degree:
            max_degree = key_int
    return max_degree

def printOutput():
    print("Reduced form: ", end="")
    for key, value in dict_degree.items():
        print(f'{value} * X^{key}', end=" ")
    print("= 0")

    if (getMaxDegree() == -1):
        raise Exception("Degree is invalid")
    print(f'Polynomial degree: {getMaxDegree()}')

def parseConfficient(num, sign):
    split = num.split("X^")
    if len(split) == 1:
        return

    if split[0].find(".") == -1:
        num = int(split[0]) * sign
    else:
        num = float(split[0]) * sign

    if dict_degree.get(split[1]):
        dict_degree[split[1]] += num
    else:
        dict_degree[split[1]] = num

def createOutput():
    for degree in dict_degree.keys():
        num = ""
        if dict_degree[degree] >= 0 and degree != "0":
            num += "+"
        num += str(dict_degree[degree])
        if degree != "0":
            num = num[:1] + " " + num[1:]
        dict_degree[degree] = num

def preprocessInput(_input):
    if len(sys.argv) != 2:
        raise SyntaxError("Argument error")
    return _input[1].replace(" ", "").replace("*", "")

def computorv1():
    global dict_degree
    dict_degree = {}

    try:
        _input = preprocessInput(sys.argv);
        start = 0
        sign = 1
        for i in range(len(_input)):
            if not re.search("^\\+|-|=$", _input[i]) and i != len(_input) - 1:
                continue
            num = ""
            if i == len(_input) - 1:
                num += _input[start:i + 1]
            else:
                num += _input[start:i]
            parseConfficient(num, sign)
            start = i
            if _input[i] == '=':
                sign = -1
                start += 1
        createOutput()
        printOutput()
    except SyntaxError as error:
        print(error.args[0])

if __name__ == '__main__':
    computorv1()