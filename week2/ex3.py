import sys


def main():
    lst = []

    for line in sys.stdin:
        lst.append(int(line))
    lst.sort()
    print(lst)
    print(lst[::-1]) 


if __name__ == "__main__":
    main()



