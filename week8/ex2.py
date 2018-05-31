from sys import stdin # Easy way of dealing with EOF
from collections import defaultdict

def dijkstra(graph, stations, start):
    pass


def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        input() # read blank line
        num_stations, num_intersections = map(int, input().split())
        graph = defaultdict(list)
        stations = []

        for __ in range(num_stations):
            stations.append(int(input()))

        line = stdin.readline()
        while  line:
            node1, node2, cost = map(int, line.split())
            graph[node1].append((node2, cost))
            graph[node2].append((node1, cost))
            line = stdin.readline()

        ans = 1
        max_dist = -1
        
        for intersection in range(num_stations+1, 0, -1):
            if intersection not in stations:
                temp = dijkstra(graph, stations, intersection)
                if temp > max_dist:
                    max_dist = temp
                    ans = intersection

        print(ans)


if __name__ == "__main__":
    main()
