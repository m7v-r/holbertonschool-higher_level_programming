#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""
import sys


def print_stats(size, status_codes):
    """Prints the accumulated statistics."""
    print("File size: {}".format(size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def run_parsing():
    """Reads stdin and processes log lines."""
    total_size = 0
    status_counts = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 2:
                total_size += int(parts[-1])
                code = parts[-2]
                if code in status_counts:
                    status_counts[code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
    print_stats(total_size, status_counts)


if __name__ == "__main__":
    run_parsing()
