import math
import heapq

def calculate_cost(dist_x, dist_y, src, dest):
    return math.sqrt((dist_x[src] - dist_x[dest])**2 +(dist_y[src] - dist_y[dest])**2)

def neibours(edges, node):
    ans = []
    for edge in edges:
        if edge[1] == node:
            ans.append(edge)
    return ans

def msf(outposts, edges):
    visited = [False]*outposts
    visited[0] = True
    new_edges = []
    heap = []

    for edge in neibours(edges, 0):
        heapq.heappush(heap, edge)

    while heap:
        cost, src, dest = heapq.heappop(heap)
        if not visited[dest]:
            new_edges.append((cost, src, dest))
            visited[dest] = True
        for edge in neibours(edges, dest):
            heapq.heappush(heap, edge)

    return new_edges


def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        satelites, outposts = map(int, input().split())
        dist_x = []
        dist_y = []

        for _ in range(outposts):
            x, y = map(int, input().split())
            dist_x.append(x)
            dist_y.append(y)

        # All edges follow the order (cost, src, dest) for faster ordering
        edges = []
        for i in range(outposts):
            for j in range(i+1, outposts):
                cost = calculate_cost(dist_x, dist_y, i, j)
                edges.append((cost, i, j))

        minimum_edges = sorted(msf(outposts, edges))
        print("%.2f" % minimum_edges[-satelites][0])

if __name__ == "__main__":
    main()
