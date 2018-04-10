from collections import defaultdict

PRIMES_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def prime_factors(n, primes):
    idx_prime = 0
    prime = PRIMES_100[idx_prime]
    while n != 1 and prime**2 <= n:
        while n % prime == 0:
            n //= prime
            primes[prime] += 1
        idx_prime += 1
        prime = PRIMES_100[idx_prime]
    if n != 1:
        primes[n] += 1

def factorial_primes(n, primes):
    for num in range(1, n+1):
        prime_factors(num, primes)

def main():
    n = int(input())
    while n != 0:
        primes = defaultdict(int)
        factorial_primes(n, primes)

        # printing
        print("{0:3d}! =".format(n), end="")
        end = PRIMES_100.index(max(primes)) + 1
        for num in range(0, end):
            if num != 0 and num % 15 == 0:
                print("\n" + " "*6, end="")
            if PRIMES_100[num] in primes:
                temp = primes[PRIMES_100[num]]
                print("{0:3d}".format(temp), end="")

        print()
        n = int(input())

if __name__ == "__main__":
    main()
