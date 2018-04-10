PRIMES = []
bound = 1

def sieve(upperbound):
    bs = [False]*upperbound
    bs[0] = bs[1] = True
    for i in range(bound, n+1):



def prime_factors(n, primes)::w
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

def main():
    # Reads all inputs
    line = input()
    while line:
        n, m = map(int, line.split())
        inputs.append((n, m))
        line = input()

    # Generates primes up to max(n)
    sieve(max(inputs, key=lambda x: x[0]), primes)
    for n, m in inputs():


if __name__ == "__main__":
    main()
