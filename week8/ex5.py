import math
from collections import defaultdict

visited = []
cost = []

def visit(graph, current, dest):
    if current == dest:
        return
    global visited
    global cost
    visited[current] = True
    for neighbour, price in graph[current]:
        if not visited[neighbour] and cost[current] + price < cost[neighbour]:
            cost[neighbour] = cost[current] + price
            visit(graph, neighbour, dest)


def main():
    num_test_cases = int(input())
    for test_case in range(num_test_cases):
        servers, connections, start, dest = map(int, input().split())
        graph = defaultdict(list)
        for __ in range(connections):
            node1, node2, price = map(int, input().split())
            graph[node1].append((node2, price))
            graph[node2].append((node1, price))

        global visited
        global cost
        visited = [False]*servers
        visited[start] = True
        cost = [math.inf]*servers
        cost[start] = 0

        visit(graph, start, dest)
        if cost[dest] != math.inf:
            print("Case #%d: %d" % (test_case + 1, cost[dest]))
        else:
            print("Case #%d: unreachable" % (test_case + 1))


if __name__ == "__main__":
    main()
