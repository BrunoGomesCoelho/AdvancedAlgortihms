def operator():
    line = input().split()
    letter = line[0]
    nums = line[1:]

    if letter == "S":
        print("T", sum(map(int, nums)))
    elif letter == "R":
        print("T", int(nums[0]) - sum(map(int, nums[1:])))
    else:
        print("E")


def main():
    lines = int(input())

    for _ in range(lines):
        operator()


if __name__ == "__main__":
    main()
