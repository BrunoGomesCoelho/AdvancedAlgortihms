import sys

PRIME = 131071

def main():
    char = sys.stdin.read(1)
    x = 0
    while char:
        if char == "\n":
            char = sys.stdin.read(1)
        elif char == "#":
            if x == 0:
                print("YES")
            else:
                print("NO")
            x = 0
            char = sys.stdin.read(1)
        else:
            x  = (2*x + int(char)) % PRIME
            char = sys.stdin.read(1)

if __name__ == "__main__":
    main()
