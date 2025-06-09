#!/usr/bin/env python3

"""Simple command-line calculator"""

import operator


def main():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    print("Simple Calculator")
    print("Type 'quit' to exit")
    while True:
        try:
            expr = input('Enter expression (e.g., 2 + 3): ')
        except EOFError:
            print()
            break
        if expr.lower() in ('quit', 'exit'):
            break
        try:
            left, op, right = expr.split()
            left = float(left)
            right = float(right)
            if op not in operations:
                print('Unsupported operator:', op)
                continue
            result = operations[op](left, right)
            print('Result:', result)
        except ValueError:
            print('Invalid expression. Use format: <number> <operator> <number>')
        except ZeroDivisionError:
            print('Error: Division by zero')
    print('Goodbye!')


if __name__ == '__main__':
    main()
