#!/usr/bin/python3
"""Log parsing"""


def parseLogs():
    """
    Reads stdin line by line and computes metrics
    """
    stdin = __import__('sys').stdin
    lineNumber = 0
    size = 0
    statusCodes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            lineNumber += 1
            line = line.split()
            try:
                size += int(line[-1])
                if line[-2] in codes:
                    try:
                        statusCodes[line[-2]] += 1
                    except KeyError:
                        statusCodes[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if lineNumber == 10:
                report(size, statusCodes)
                lineNumber = 0
        report(size, statusCodes)
    except KeyboardInterrupt as e:
        report(size, statusCodes)
        raise


def report(size, statusCodes):
    """
    Prints the log size and status codes
    """
    print("File size: {}".format(size))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    parseLogs()
