#!/usr/bin/python3
"""
Computes metrics from standard input.
"""


def print_status(size, status_codes):
    """
    Accumulated metrics print on Console.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


def process_line(line, size, status_codes):
    """
    Update metrics after process a single line of input and.
    """
    line_parts = line.split()

    try:
        size += int(line_parts[-1])
    except (IndexError, ValueError):
        pass

    try:
        status_code = int(line_parts[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1
    except (IndexError, ValueError):
        pass

    return size, status_codes


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }
    count = 0

    try:
        for line in sys.stdin:
            size, status_codes = process_line(line, size, status_codes)
            count += 1

            if count == 10:
                print_status(size, status_codes)
                count = 0

        print_status(size, status_codes)

    except KeyboardInterrupt:
        print_status(size, status_codes)
        raise
