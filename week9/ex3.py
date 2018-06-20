import sys

MEMO = [0]*(7489+1)
MEMO[0] = 1
COINS = [1, 5, 10, 25, 50]

def main():
    line = sys.stdin.readline()
    while line:
        # Intialize the variables
        MEMO = [0]*(7489+1)
        MEMO[0] = 1

        change = int(line)
        for coin in COINS:
            for number in range(coin, change+1):
                MEMO[number] += MEMO[number - coin]

        print(MEMO[change])
        line = sys.stdin.readline()

if __name__ == "__main__":
    main()
