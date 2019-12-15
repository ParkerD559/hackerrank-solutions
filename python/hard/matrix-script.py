"""
To decode the script, Neo needs to read each column and select only the alphanumeric
characters and connect them. Neo reads the column from top to bottom and starts reading
from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script,
then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.
Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
"""
import re


n, m = map(int, input().rstrip().split())
matrix = [input() for _ in range(n)]
# Flatten counting col first
decoded = "".join([matrix[row][col] for col in range(m) for row in range(n)])
# Replace non-alphanumerics between alphanumerics
result = re.sub(r"(?<=\w)\W+(?=\w)", " ", decoded)
print(result)
