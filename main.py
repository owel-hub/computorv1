import re
import sys
import traceback

def parseConfficient(num, sign):
    split = num.split("X^")
    if len(split) == 1:
        return
    for key in dict_degree.keys():
        if split[1] == key:
            try:
                dict_degree[key] += int(split[0]) * sign
            except:
                dict_degree[key] += float(split[0]) * sign

def createOutput():
    for degree in dict_degree.keys():
        num = ""
        if dict_degree[degree] >= 0 and degree != "0":
            num += "+"
        num += str(dict_degree[degree])
        if degree != "0":
            num = num[:1] + " " + num[1:]
        dict_degree[degree] = num
    print(f'Reduced form: \"{dict_degree["0"]} * X^0 {dict_degree["1"]} * X^1 {dict_degree["2"]} * X^2 = 0\"')

def preprocessInput(_input):
    if len(sys.argv) != 2:
        raise SyntaxError("Argument error")
    print(sys.argv)
    return _input[1].replace(" ", "").replace("*", "")

def computorv1():
    global dict_degree
    dict_degree = {
        "0": 0,
        "1": 0,
        "2": 0
    }
    try:
        _input = preprocessInput(sys.argv);
        start = 0
        sign = 1
        for i in range(len(_input)):
            if not re.search("^\\+|-|=$", _input[i]) and not i == len(_input) - 1:
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
    except SyntaxError as error:
        print(error.args)


if __name__ == '__main__':
    computorv1()