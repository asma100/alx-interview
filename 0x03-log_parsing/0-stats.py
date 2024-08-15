#!/usr/bin/env python3
"""tasks"""
import sys
import signal

from collections import Counter

total_size = 0
line_count = 0
status_codes = Counter()

try:
  for line in sys.stdin:
    line = line.rstrip()  # Remove trailing newline
    if not line:
      continue

    # Extract data from the line
    try:
      ip, _, _, _, status_code, file_size_str = line.split()
      file_size = int(file_size_str)
    except (ValueError, IndexError):
      continue  # Skip invalid lines

    total_size += file_size
    status_codes[int(status_code)] += 1
    line_count += 1

    # Print statistics every 10 lines or on keyboard interrupt
    if line_count % 10 == 0 or line_count == 1:
      print(f"Total file size: {total_size}")

  # Print final statistics after loop (if not interrupted)
  if line_count > 0:
    print(f"Total file size: {total_size}")

    # Sort status codes and print counts
    for code, count in sorted(status_codes.items()):
      print(f"{code}: {count}")

except KeyboardInterrupt:
  # Print statistics on keyboard interrupt
  print(f"Total file size: {total_size}")

  # Sort status codes and print counts (if any)
  if status_codes:
    for code, count in sorted(status_codes.items()):
      print(f"{code}: {count}")
