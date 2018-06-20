from math import inf


def bfs(graph, num_nodes, source, sink):
    parents = [None]*num_nodes
    visited = [False]*num_nodes
    visited[source] = True
    queue = []
    queue.append(source)

    while queue:
        vert = queue.pop()
        # For each neighbour, if not visited, visit
        for neighbour, cost in enumerate(graph[vert]):
            if not visited[neighbour] and cost > 0:
                queue.append(neighbour)
                parents[neighbour] = vert
                visited[neighbour] = True
    return parents[sink], parents


def ford_fulkerson(graph, num_nodes, source, sink):
    max_flow = 0
    valid_path, parents = bfs(graph, num_nodes, source, sink)

    # While there is a extending path
    while valid_path is not None:
        path_flow = inf
        current = sink
        # Go backwards finding the augment path value
        while current != source:
            previous = parents[current]
            path_flow = min(path_flow, graph[previous][current])
            current = previous

        max_flow += path_flow

        # Go forwards again updating all "residual" edges
        # In our case just update the other edge since it is bidirectional
        current = sink
        while current != source:
            previous = parents[current]
            # Substract the min path_flow from the "forwards" edge
            graph[previous][current] -= path_flow

            # Add the residual edge backwards
            graph[current][previous] += path_flow
            current = previous


        # Recalculate if there is a path
        valid_path, parents = bfs(graph, num_nodes, source, sink)

    return max_flow


def main():
    num_nodes = int(input())
    test_case = 1
    while num_nodes:
        source, sink, num_connections = map(int, input().split())
        source, sink = source - 1, sink - 1
        graph = [[0]*num_nodes for _ in range(num_nodes)]

        for _ in range(num_connections):
            node1, node2, cost = map(int, input().split())
            graph[node1-1][node2-1] = cost
            graph[node2-1][node1-1] = cost
        max_flow = ford_fulkerson(graph, num_nodes, source, sink)
        print("Network %d" % test_case)
        print("The bandwith is %d." % max_flow)

        num_nodes = int(input())
        test_case += 1


if __name__ == "__main__":
    main()
