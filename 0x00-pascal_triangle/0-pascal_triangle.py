#!/usr/bin/python3
"""model"""


def pascal_triangle(n):
  """
  This function generates Pascal's Triangle up to the nth row.
  """
  if n <= 0:
    return []
  triangle = []
  triangle.append([1])
  for i in range(1, n):
    previous_row = triangle[i-1]
    current_row = []
    current_row.append(1)
    for j in range(1, i):
      current_row.append(previous_row[j-1] + previous_row[j])
    current_row.append(1)
    triangle.append(current_row)
  return triangle
