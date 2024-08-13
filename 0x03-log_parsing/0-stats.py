#!/usr/bin/python3
"""
read from st.in line by line till 10 lines
"""

import sys

codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
              '404': 0, '405': 0, '500': 0}

file_size = 0
counter = 0

try:
    for line in sys.stdin:
        lines = line.split(" ")

        if (len(lines) > 4):
            code = lines[-2]
            size = int(lines[-1])

            if code in codes_dict.keys():
                codes_dict[code] += 1

            file_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(file_size))
            for key, value in sorted(codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(file_size))
    for key, value in sorted(codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
