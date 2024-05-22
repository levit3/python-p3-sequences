#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    while len(fib_list) !=length :
        if len(fib_list) == 0 :
            fib_list.append(0)
        elif len(fib_list) == 1:
            fib_list.append(1)
        else:
            new_val=fib_list[-1] + fib_list[-2]
            fib_list.append(new_val)
    print(fib_list)