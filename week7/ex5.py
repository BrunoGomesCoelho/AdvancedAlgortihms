from collections import defaultdict


def get_next_task(count, in_graph, graph):
    candidates = [x for x in in_graph if count[x] == 0]

    other = None
    # special case to preserve output order
    for candidate in candidates:
        if candidate not in graph:
            return candidate
        if count[candidate] == 0:
            other = candidate
    return other

def main():
    tasks, orders = map(int, input().split())
    while not (tasks == orders == 0):

        # Creates structures
        graph = defaultdict(list)
        count = defaultdict(int)
        answer = []
        in_graph = [x for x in range(1, tasks+1)]

        for _ in range(orders):
            a, b = map(int, input().split())
            count[b] += 1
            graph[a].append(b)

        # process
        while in_graph:
            task = get_next_task(count, in_graph, graph)
            answer.append(task)
            for neighbour in graph[task]:
                count[neighbour] -= 1
            in_graph.remove(task)

        print(*answer, sep=" ")
        tasks, orders = map(int, input().split())

if __name__ == "__main__":
    main()
