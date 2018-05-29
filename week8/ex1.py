import math

def main():
    test_cases = int(input())

    for _ in range(test_cases):
        # Read the input
        num_vert, num_edges = map(int, input().split())
        edges = []
        for __ in range(num_edges):
            edges.append([int(x) for x in input().split()])

        distances = [math.inf if x != 0 else 0 for x in range(num_vert)]

        # Relax all edges V-1 times
        for __ in range(num_vert):
            for src, dest, cost in edges:
                if distances[dest] > distances[src] + cost:
                    distances[dest] = distances[src] + cost

        # Check for negative cycles
        for src, dest, cost in edges:
            if distances[dest] > distances[src] + cost:
                print("possible")
                break
        else:
            print("not possible")


if __name__ == "__main__":
    main()
