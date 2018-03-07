import sys


def main():
    count = 0

    for line in sys.stdin:
        count += sum(map(int, line.split()))
    print(count)

if __name__ == "__main__":
    main()
