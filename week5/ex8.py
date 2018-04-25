def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        nums = [int(x) for x in input().split()]
        size = len(nums)
        biggest = 1
 
        for i in range(size):
            for j in range(i+1, size):
                candidate = gcd(nums[i], nums[j])
                if candidate > biggest:
                    biggest = candidate
        print(biggest)

if __name__ == "__main__":
    main()
