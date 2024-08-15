#!/usr/bin/python3
"""
Log parsing script
"""

import sys
import re

def print_statistics(stats: dict) -> None:
    """
    Helper function to display statistics
    """
    print("File size: {}".format(stats["total_size"]))
    for status_code in sorted(stats["status_counts"]):
        if stats["status_counts"][status_code]:
            print("{}: {}".format(status_code, stats["status_counts"][status_code]))

if __name__ == "__main__":
    # Regular expression to match the log line format
    log_pattern = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )

    # Initialize counters and storage
    line_counter = 0
    stats = {}
    stats["total_size"] = 0
    stats["status_counts"] = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for log_line in sys.stdin:
            log_line = log_line.strip()
            match = log_pattern.fullmatch(log_line)
            if match:
                line_counter += 1
                status_code = match.group(1)
                size = int(match.group(2))

                # Update total file size
                stats["total_size"] += size

                # Update status code count
                if status_code.isdecimal():
                    stats["status_counts"][status_code] += 1

                # Print statistics every 10 lines
                if line_counter % 10 == 0:
                    print_statistics(stats)

    finally:
        print_statistics(stats)
