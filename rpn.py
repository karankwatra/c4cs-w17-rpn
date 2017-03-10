#!/usr/bin/env python3
import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
}

def calculate(arg):
    stack = list()
    for operand in arg.slit():
        try:
            operand = float(operand)
            stack.append(operand)
        except:
            arg2 = stack.pop()
            arg1 = stack.pop()
            operator_fn = OPERATORS[operand]
            result = operator_fn(arg1, arg2)

            stack.append(result)

def main():
    while True:
        result = calculate(input('rpn calc> '))

if __name__ == '__main__':
    main()
