import sys
def main():
    line = [int(x) for x in sys.stdin.readline().split()[:-1]]
    while line:
        num_biggest = max(line)
        mod_biggest = 1
        for i in range(2, num_biggest):
            if all(num % i == line[0] % i for num in line):
                mod_biggest = i
        print(mod_biggest)
        
        line = [int(x) for x in sys.stdin.readline().split()[:-1]]

if __name__ == "__main__":
    main()
