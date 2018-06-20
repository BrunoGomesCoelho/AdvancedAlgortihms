from collections import defaultdict

total = 0

def visit(graph, count, path, visited, end, current):
    if current == end:
        global total
        total += 1
        for x in path:
            count[x] += 1
        return
    path.append(current)
    visited[current] = True

    for index, neighbour in enumerate(graph[current]):
        if neighbour != 0 and not visited[index]:
            visit(graph, count, path.copy(), visited.copy(), end, index)

def main():
    test_case = int(input())
    for i in range(test_case):
        nodes = int(input())
        matrix = []

        for _ in range(nodes):
            matrix.append([int(x) for x in input().split()])

        answer = [["N"]*nodes for _ in range(nodes)]
        answer[0] = ["Y"]*nodes
        
        # For every node, try a bfs on 0->node
        for end in range(1, nodes):
            visited = [False]*nodes
            count = defaultdict(int)
            global total
            total = 0
            visit(matrix, count, [], visited.copy(), end, 0)

            for node in range(1, nodes):
                if count[node] == total:
                    answer[node][end] = "Y"
            answer[end][end] = "Y"
        
        print("Case %d:" % (i+1))
        print("+", "-"*(2*nodes - 1), "+", sep="")
        for line in answer:
            print("|", "|".join(map(str, line)), "|", sep="")
            print("+", "-"*(2*nodes - 1), "+", sep="")

if __name__ == "__main__":
    main()
