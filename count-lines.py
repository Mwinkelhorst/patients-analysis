"""
This module counts the number of lines in standard input
input: a string
output: total number of lines
"""

import sys

count = 0
for line in sys.stdin:
	count+=1

print(count, "lines in standard input")

