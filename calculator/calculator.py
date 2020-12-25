"""
    1. Calculator in polish notation
    Create a calculator with following requirements:
        * support following mathematical operations: + - * /
        * operations can be specified both with signs and names (add: +; sub: -; mul: *; div: /),
        * operands can be both integers and floats,
        * the operations must be written in polish notation: + 2 3,
        * user must be prompted for a single input containing the expression in polish notation,
        * operators and the operands can be separated by arbitrary number of spaces,
        * all inputs must be in strict format (everything must be checked and validated),
        * usage of exceptions is prohibited.
        * create logging directory and file in that directory
        1. for exceptions text must be "{system datetime} :: ERROR :: {exception message} :: {input parameters}"
        2. for information text must be "{system datetime} :: INFO :: {input parameters} :: {result}"
    * print report about logs after result
    Example:
        Expression: + 2 3
        Result: 5
        Report: INFO-1, ERROR-0
        Expression: a b
        ERROR: Invalid expression
        Report: INFO-1, ERROR-1
"""

from datetime import datetime
from pathlib import Path


class Logging:

    def __init__(self, file_name):
        with open(Path(file_name), 'w') as file:
            pass
        self.__file_name = file_name
        self.__info = 0
        self.__error = 0

    def error(self, message):
        with open(Path(self.__file_name), 'a+') as file:
            file.write(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} :: ERROR :: {message}\n')
        self.__error += 1

    def info(self, message):
        with open(Path(self.__file_name), 'a+') as file:
            file.write(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} :: INFO :: {message}\n')
        self.__info += 1

    def __str__(self):
        self.info(f'Report: INFO-{self.__info}, ERROR-{self.__error}')
        with open(Path(self.__file_name), 'r') as file:
            return file.read()


def calculate(expression):
    operand_stack = []
    operator = {'add': '+', 'sub': '-', 'mul': '*', 'div': '/', '+': '+', '-': '-', '*': '*', '/': '/'}

    log = Logging('./log.txt')
    log.info(f'Expression: {expression}')

    for item in expression.split()[::-1]:
        if item in '0123456789':
            operand_stack.append(item)
        elif item in operator and len(operand_stack) > 1:
            operand_stack.append(
                eval(f'{operand_stack.pop()}{operator.get(item)}{operand_stack.pop()}')
            )
        else:
            log.error(f'Invalid expression')
            break
    else:
        if len(operand_stack) > 1:
            log.error(f'Invalid expression')
            print(log)
            return
        log.info(f'Result: {operand_stack[0]}')

    print(log)


calculate("* 6 + 4 5")  # 54
calculate("* add 4 5 6")  # 54
calculate("+ 2 3")  # 5
calculate("2 3")  # Error
calculate("2")  # 2
calculate("a b")  # Error
calculate("+ - * 2 3 3 / / 8 4 + 1 1")  # 2×3−3+8/4/(1+1) = 4
