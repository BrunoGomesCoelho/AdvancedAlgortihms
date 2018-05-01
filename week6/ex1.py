import sys

def can_solve(distances, nights, campsites, target):
    slept = 0
    count = target
    for i in range(0, len(distances)-1):
        difference = distances[i+1] - distances[i]
        if count >= difference:
            count -= difference
        else:
            slept += 1
            count = target - difference
        if slept > nights or count < 0:
            return False
    return True


def main():
    line = sys.stdin.readline()
    while line and not line.isspace():
        campsites, nights = map(int, line.split())
        distances = [0]
        for i in range(campsites + 1):
            distances.append(int(input()) + distances[i])

        start, end = 0, distances[-1]
        ans = 10000000

        while end - start >= 0:
            middle = (start+end) // 2
            #print(start, middle, end)
            #print(middle)
            if can_solve(distances, nights, campsites, target=middle):
                end = middle - 1
                ans = min(ans, middle)
            else:
                start = middle + 1
        print(ans)
        line = sys.stdin.readline()


if __name__ == "__main__":
    main()
