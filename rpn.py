import operator
import readline
from termcolor import colored


OPERATORS = {
		'+' : operator.add,
	    '-' : operator.sub,
	    '*' : operator.mul,
	    '/' : operator.truediv,
	    '^' : operator.pow
	    }


def calculate(arg, ops):
    stack = []


    for operand in arg.split():
        try:
            operand = float(operand)
            stack.append(operand)
        except:
            arg2 = stack.pop()
            arg1 = stack.pop()
            operator_fn = OPERATORS[operand]
            result = operator_fn(arg1, arg2)
            stack.append(result)
            ops.append(arg1)
            ops.append(arg2)
            ops.append(operand)

    return stack.pop()


def main():
    while True:
        ops = []
        result = calculate(input('rpn calc> '), ops)

        if ops[0] < 0:
        	print(colored(str(ops[0]), 'red'), end="")
        else:
        	print(colored(str(ops[0]), 'green'), end="")

        print(colored(str(ops[2]), 'blue'), end="")

        if ops[1] < 0:
        	print(colored(str(ops[1]), 'red'), end="")
        else:
        	print(colored(str(ops[1]), 'green'), end="")

        print((colored("=", 'blue')), end="")

        if result < 0:
            result = colored(result, 'red')
        else:
            result = colored(result, 'green')

        print(result)


if __name__ == '__main__':
    main()
