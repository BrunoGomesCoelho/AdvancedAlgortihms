from collections import defaultdict


def visit(graph, visited, current):
    visited[current] = True
    for neighbour in graph[current]:
        if not visited[neighbour]:
            visit(graph, visited, neighbour)

def main():
    test_case = int(input())
    for _ in range(test_case):
        nodes = int(input())
        matrix = []

        for _ in range(nodes):
            matrix.append([int(x) for x in input().split()])

        answer = [ [None]*nodes for _ in range(nodes)]


        
        
if __name__ == "__main__":
    main()
