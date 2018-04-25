def main():
    test_cases = int(input())
    for _ in range(test_cases):
        line = input()
        while not line:
            line = input()
        friends, boxes = map(int, line.split())
        cat = 0
        for box in range(boxes):
            add = 1
            all_chocolates = [int(x) for x in input().split()]
            for choc in all_chocolates[1:]:
                add *= choc
                add %= friends
            cat += add
            cat %= friends
        print(cat)

if __name__ == "__main__":
    main()
