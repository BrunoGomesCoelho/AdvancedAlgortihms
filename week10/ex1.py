def main():
    amount_routes = int(input())
    for route in range(amount_routes):
        num_stops = int(input())
        stops = [int(input()) for x in range(num_stops-1)]

        start = end = 0
        max_niceness = 0

        for idx, stop in enumerate(stops):
            possible = max_niceness + stop
            if possible > max_niceness:
                end = idx
                max_niceness = possible
            elif possible <= 0:
                start = idx

        if max_niceness != 0:
            print("The nicest part of route {} is between stops {} and {}"\
                  .format(route+1, start+2, end+2))
        else:
            print("Route {} has no nice parts".format(route+1))


if __name__ == "__main__":
    main()
