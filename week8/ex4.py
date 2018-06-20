import math


def calculate_cost(dist_x, dist_y, src, dest):
    return math.sqrt((dist_x[src] - dist_x[dest])**2 +(dist_y[src] - dist_y[dest])**2)


def floyd_warshall(towns, dist_x, dist_y):
    # Creates the distance vector, of size towns*towns*towns
    dist = []
    for __ in range(towns):
        dist.append([[None]*towns for _ in range(towns)])

    # Calculates with 0 steps
    for i in range(towns):
        for j in range(towns):
            cost = calculate_cost(dist_x, dist_y, i, j)
            if cost <= 10:
                dist[0][i][j] = cost
            else:
                dist[0][i][j] = math.inf

    ans = -1

    # Calculates minimum over all steps
    for k in range(1, towns):
        for i in range(towns):
            for j in range(towns):
                dist[k][i][j] = min(dist[k-1][i][j], dist[k-1][i][k] + dist[k-1][k][j])
                if dist[k][i][j] > ans and dist[k][i][j] != math.inf:
                    ans = dist[k][i][j]
    return ans

def main():
    num_test_cases = int(input())
    for test_case in range(num_test_cases):
        towns = int(input())
        dist_x = []
        dist_y = []
        for _ in range(towns):
            x, y = map(int, input().split())
            dist_x.append(x)
            dist_y.append(y)

        ans = floyd_warshall(towns, dist_x, dist_y)

        print("Case #%d:" % (test_case+1))
        if ans != -1 and ans != 0:
            print("%.4lf" % ans)
        else:
            print("Send Kurdy")

        if test_case != num_test_cases - 1:
            print()

if __name__ == "__main__":
    main()
