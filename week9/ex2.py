def main():
    num_cases = int(input())

    for _ in range(num_cases):
        num_objects = int(input())
        objects = []
        for __ in range(num_objects):
            objects.append([int(x) for x in input().split()])

        memo = [0]*31
        for item_price, item_weight in objects:
            for weight in range(30, item_weight-1, -1):
                memo[weight] = max(memo[weight], memo[weight-item_weight]+item_price)

        ans = 0
        family_size = int(input())
        for __ in range(family_size):
            max_weight = int(input())
            ans += memo[max_weight]
        print(ans)

if __name__ == "__main__":
    main()
