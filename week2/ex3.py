import sys
from collections import deque


def recurse_solve(stack, toy, valid):
    count = 0
    while stack:
        num = stack.pop()
        if count >= -toy:
            return False
        elif num == -toy:
            return valid
        elif num < 0:
            count += -num
            valid = recurse_solve(stack, num, valid)
        # If we reach this, we hava a invalid number
        else:
            return False
    return valid


def main():
    for line in sys.stdin:
        stack = deque([int(x) for x in line.split()][::-1])
        valid = recurse_solve(stack, stack.pop(), True)
        if valid:
            print(":-) Matrioshka!")
        else:
            print(":-( Try again.")

if __name__ == "__main__":
    main()
