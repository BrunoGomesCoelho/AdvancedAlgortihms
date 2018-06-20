import math
import copy

from sys import stdin # Easy way of dealing with EOF

def find_minimum_element(heap, distances):
    element, minimum = 0, math.inf
    for node in heap:
        if distances[node] < minimum:
            element = node
            minimum = distances[node]
    return element


def dijkstra(graph, num_intersections, stations, start):
    # Creates data stuctures
    distances = [math.inf]*num_intersections
    distances[start] = 0
    waiting = [x for x in range(num_intersections)]

    # Create dummy nodes connecting all sources, with cost 0 and updating distances
    for station in stations:
        distances[station] = 0
        graph[start][station] = 0
        graph[station][start] = 0

    while waiting:
        current = find_minimum_element(waiting, distances)
        waiting.remove(current)
        neighbours = [x for x in range(num_intersections)
                      if graph[current][x] != math.inf and current != x]

        for neighbour in neighbours:
            alt = distances[current] + graph[current][neighbour]
            if alt < distances[neighbour]:
                distances[neighbour] = alt

    return max(distances)


def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        input() # read blank line
        num_stations, num_intersections = map(int, input().split())
        graph = [[math.inf]*num_intersections for __ in range(num_intersections)]
        stations = []

        for __ in range(num_stations):
            stations.append(int(input())-1)

        line = stdin.readline()
        while line:
            node1, node2, cost = map(int, line.split())
            graph[node1-1][node2-1] = cost
            graph[node2-1][node1-1] = cost
            line = stdin.readline()

        ans = 1
        max_dist = -1

        for intersection in range(num_intersections-1, -1, -1):
            if intersection not in stations:
                temp = dijkstra(copy.deepcopy(graph), num_intersections, stations, intersection)
                if temp > max_dist:
                    max_dist = temp
                    ans = intersection
        print(ans)


if __name__ == "__main__":
    main()
