# first notice that z = A - x - y
from math import sqrt

def get_z(a, x, y):
    return a - x -y

def is_answer(a, b, c, x, y):
    z = get_z(a, x, y)
    if z < 1:
        return False
    return x**2 + y**2 + z**2 == c and x*y*z == b and x+y+z == a


def solve(a, b, c):
    smallest = min(b, int(sqrt(c)))
    solved = False

    # i = x
    for i in range(1, smallest):
        if solved:
            break
        # j = y
        for j in range(1, smallest):
            if is_answer(a, b, c, i, j):
                x = i
                y = j
                solved = True
                break
    if solved:
        print(x, y, get_z(a, x, y))
    else:
        print("No solution.")


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        a, b, c = map(int, input().split())
        solve(a, b, c)


if __name__ == "__main__":
    main()



