"""
Consider an algorithm that takes as input a positive integer n.
If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one.
 The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:

        3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

Input
The only input line contains an integer n.

Output
Print a line that contains all values of n during the algorithm.
"""

path = []

def weird_algorithm(n: int) -> None:
    path.append(n)
    if n == 0:
        return
    if n == 1:
        return
    if n%2 == 0:
        return weird_algorithm(n // 2)

    weird_algorithm((n*3) + 1)

n = int(input())
weird_algorithm(n)

print(*path)