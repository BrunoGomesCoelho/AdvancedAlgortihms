import sys
from math import sin, cos, tan, exp

def solve(p, q, r, s, t, u):
    f = lambda x: p*exp(-x) + q*sin(x) + r*cos(x) + s*tan(x) + t*x**2 + u
    start, end = 0, 1
    error = 0.0000001

    if f(0) * f(1) > 0: # if True, there is no answer
        print("No solution")
        return

    while end - start > error:
        x = (end + start) / 2
        # If x increases, the function decreases between 0 and 1
        # Therefore if positive, we need to increase x and vice-versa
        if f(x) > 0:
            start = x
        else:
            end = x
    print("%.4lf" % x)

def main():
    line = sys.stdin.readline()
    while line:
        p, q, r, s, t, u = map(int, line.split())
        solve(p, q, r, s, t, u)
        line = sys.stdin.readline()

if __name__ == "__main__":
    main()
