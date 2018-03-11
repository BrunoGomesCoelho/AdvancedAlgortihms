import sys


def main():
    lst = []

    for line in sys.stdin:
        lst.append(int(line))
    lst.sort()
    print(*lst, sep="\n")
    print()
    print(*lst[::-1], sep="\n") 


if __name__ == "__main__":
    main()



