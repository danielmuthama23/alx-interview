#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys

codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
file_size = 0
count = 0


def print_info():
    """print stdin input computed statistics
    <Helper function>
    """
    print("File size: {}".format(file_size))
    for key, val in sorted(codes.items()):
        if val > 0:
            print("{}: {}".format(key, val))


try:
    while sys.stdin:
        input_line = sys.stdin.readline()
        section = input_line.split()

        status_code = section[-2]
        size = section[-1]
        count += 1

        if status_code:
            if status_code in codes.keys():
                codes[status_code] += 1
            file_size += int(size)

        if count % 10 == 0:
            print_info()
except KeyboardInterrupt:
    print_info()
    raise
print_info()
