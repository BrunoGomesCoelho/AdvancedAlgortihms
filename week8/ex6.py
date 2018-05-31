import heapq
from sys import stdin   # easy way of dealing with EOF


def neibours(edges, node):
    ans = []
    for cost, node2, node1 in edges:
        if node1 == node:
            ans.append((cost, node2))
    return ans


def msf(num_junctions, edges):
    visited = [False]*num_junctions
    visited[0] = True
    new_edges = []
    heap = []

    for edge in neibours(edges, 0):
        heapq.heappush(heap, edge)

    while heap:
        cost, dest = heapq.heappop(heap)
        if not visited[dest]:
            visited[dest] = True
            new_edges.append((cost, dest))
        for price, node2  in neibours(edges, dest):
            if not visited[node2]:
                heapq.heappush(heap, (price, node2))

    return new_edges


def main():
    num_junctions, num_roads = map(int, stdin.readline().split())

    while num_junctions + num_roads != 0:
        total = 0
        edges = []
        # All edges follow the order (cost, src, dest) for faster ordering
        for _ in range(num_roads):
            node1, node2, cost = map(int, input().split())
            total += cost
            edges.append((cost, node1, node2))
            edges.append((cost, node2, node1))

        minimum_spanning_tree = msf(num_junctions, edges)
        current_cost = 0
        for cost, _ in minimum_spanning_tree:
            total -= cost
        print(total)

        num_junctions, num_roads = map(int, stdin.readline().split())

if __name__ == "__main__":
    main()
