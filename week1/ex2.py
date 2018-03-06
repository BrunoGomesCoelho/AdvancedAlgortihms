def main():

    lines = int(input())
    count = 0

    for _ in range(lines):
        count += sum(map(int, input().split()))

    print(count)

if __name__ == "__main__":
    main()
