#!/usr/bin/python3
"""Log parsing"""


def parseLogs():
    """
    Reads stdin line by line and computes metrics
    """
    stdin = __import__('sys').stdin
    size = 0
    line_Number = 0
    status_Codes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            line_Number += 1
            line = line.split()
            try:
                size += int(line[-1])
                if line[-2] in codes:
                    try:
                        status_Codes[line[-2]] += 1
                    except KeyError:
                        status_Codes[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if line_Number == 10:
                report(size, status_Codes)
                line_Number = 0
        report(size, status_Codes)
    except KeyboardInterrupt as e:
        report(size, status_Codes)
        raise


def report(size, status_Codes):
    """
    Prints the log size and status codes
    """
    print("File size: {}".format(size))
    for key, value in sorted(status_Codes.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    parseLogs()
