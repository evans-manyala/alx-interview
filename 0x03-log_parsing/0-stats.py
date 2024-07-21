#!/usr/bin/python3

import sys

line_count = 0
total_file_size = 0

status_code = {
    "200": 0, "301": 0,
    "400": 0, "401": 0,
    "403": 0, "404": 0,
    "405": 0, "500": 0
}


def print_metrics():
    """Prints the current metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code.keys()):
        if status_code[code] > 0:
            print(f"{code}: {status_code[code]}")


try:
    for line in sys.stdin:
        args = line.split()
        if len(args) >= 2:
            file_size = args[-1]
            status_line = args[-2]
            if status_line in status_code:
                status_code[status_line] += 1
            try:
                total_file_size += int(file_size)
            except ValueError:
                continue
            line_count += 1
            if line_count == 10:
                print_metrics()
                line_count = 0
except KeyboardInterrupt:
    print("\nProcess was interrupted by user")
finally:
    print_metrics()
