import sys
from collections import defaultdict
from math import inf


def get_drink(order, count, in_graph):
    candidates = [x for x in in_graph if count[x] == 0]

    smallest = None
    pos = inf
    for candidate in candidates:
        candidate_pos = order.index(candidate)
        if candidate_pos < pos:
            smallest = candidate
            pos = candidate_pos

    return smallest

def main():
    line = sys.stdin.readline()
    test_case = 1
    while line:
        if len(line) == 1:
            line = sys.stdin.readline()
        # Creates structures
        graph = defaultdict(list)
        count = defaultdict(int)
        input_order = []
        in_graph = []
        answer = []

        # Reads drinks
        num_drinks = int(line)
        for _ in range(num_drinks):
            drink = sys.stdin.readline().rstrip()
            input_order.append(drink)
            in_graph.append(drink)

        # reads edges
        num_edges = int(sys.stdin.readline().rstrip())
        for _ in range(num_edges):
            a, b = sys.stdin.readline().rstrip().split(" ")
            count[b] += 1
            graph[a].append(b)

        # process
        while in_graph:
            drink = get_drink(input_order, count, in_graph)
            answer.append(drink)
            for neighbour in graph[drink]:
                count[neighbour] -= 1
            in_graph.remove(drink)

        print("Case #%d: Dilbert should drink beverages in this order: "
              % test_case, end="")
        test_case += 1

        for drink in answer[:-1]:
            print(drink, end=" ")
        print(answer[-1], ".\n", sep="")

        line = sys.stdin.readline()

if __name__ == "__main__":
    main()
