INVALID = -1
total_money = 0
amount_garments = 0

def solve(memo, garments, current_money, current_item_index):
    # If we dont have any money
    if current_money < 0:
        return INVALID

    # If we have brought all items
    elif current_item_index == amount_garments:
        return total_money - current_money

    # If we have memorized
    if memo[current_money][current_item_index] is not None:
        return memo[current_money][current_item_index]

    # Try to buy every item
    ans = INVALID
    for price in garments[current_item_index]:
        ans = max(ans, solve(memo, garments,
                             current_money - price, current_item_index+1))
    memo[current_money][current_item_index] = ans
    return ans

def main():
    num_cases = int(input())

    for _ in range(num_cases):
        global total_money, amount_garments
        total_money, amount_garments = map(int, input().split())
        memo = [[None]*amount_garments for x in range(total_money+1)]
        garments = []
        for __ in range(amount_garments):
            garments.append([int(x) for x in input().split()[1:]])

        ans = solve(memo, garments, total_money, 0)
        print(ans if ans != INVALID else "no solution")

if __name__ == "__main__":
    main()
