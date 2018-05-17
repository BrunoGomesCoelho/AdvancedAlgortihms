from collections import defaultdict

def recursive(graph, colours, past, current, current_colour):
    # color also represents visited since None means not visited
    colours[current] = current_colour
    for neighbour in graph[current]:
        if current != 0 and neighbour != past and colours[neighbour] == current_colour:
            return False
        elif colours[neighbour] is None:
            colours[neighbour] = current_colour
            return recursive(graph, colours, current, neighbour, not current_colour)
    return True

def main():
    nodes = int(input())
    while nodes != 0:
        graph = defaultdict(list)
        edges = int(input())
        colours = [None]*nodes

        for _ in range(edges):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        solved = recursive(graph, colours, 0, 0, True)

        if solved:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")

        nodes = int(input())

if __name__ == "__main__":
    main()
