# done without binary search since it uncessary and takes much longer

def solve_input(liters_100km):
    leaks = last_pos = ans = running = 0
    while True:
        line = input()
        words = line.split()
        current_pos = int(words[0])
        running += leaks * (current_pos-last_pos)
        running += liters_100km * (current_pos-last_pos) / 100

        ans = max(running, ans)
        if "Fuel" in line:
            liters_100km = int(words[3])
        elif "Leak" in line:
            leaks += 1
        elif "Mechanic" in line:
            leaks = 0
        elif "Gas" in line:
            running = 0
        elif "Goal" in line:
            break
        last_pos = current_pos
    return ans

def main():
    line = input()
    while line != "0 Fuel consumption 0":
        print("%.3lf" % solve_input(int(line.split()[3])))
        line = input()

if __name__ == "__main__":
    main()
