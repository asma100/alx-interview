#!/usr/bin/env python3
"""tasks"""
import sys
import signal

total_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """Print the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption and print stats before exiting."""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            line = line.strip()
            if not line:
                continue
            

            parts = line.split()
            if len(parts) < 9:
                continue

            ip_address = parts[0]
            date = parts[3] + ' ' + parts[4]
            method = parts[5][1:]
            path = parts[6]
            protocol = parts[7][:-1]
            status_code = parts[8]
            file_size = parts[9]


            try:
                file_size = int(file_size)
            except ValueError:
                continue


            if method == "GET" and path == "/projects/260" and protocol == "HTTP/1.1":

                total_size += file_size


                if status_code in status_codes_count:
                    status_codes_count[status_code] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print_stats()

        except Exception as e:
            continue

except KeyboardInterrupt:
    pass
finally:
    print_stats()
