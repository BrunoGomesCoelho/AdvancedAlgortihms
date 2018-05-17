import sys
from collections import defaultdict


def visit(graph, visited, current):
    visited[current] = True
    for neighbour in graph[current]:
        if not visited[neighbour]:
            visit(graph, visited, neighbour)

def to_num(letter):
    return ord(letter)-ord("A")

def to_nums(string):
    return to_num(string[0]), to_num(string[1])

def main():
    test_case = int(sys.stdin.readline())
    for _ in range(test_case):
        sys.stdin.readline()    # reads blank line
        size = ord(sys.stdin.readline()[0]) - ord("A") + 1
        line = sys.stdin.readline()

        graph = defaultdict(list)
        visited = [False]*size

        while line:
            a, b = to_nums(line)
            graph[a].append(b)
            graph[b].append(a)
            line = sys.stdin.readline()

        count = 0
        for node in range(size):
            if not visited[node]:
                count += 1
                visit(graph, visited, node)
        print(count)

if __name__ == "__main__":
    main()
