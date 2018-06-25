# Solves the Longest Decreasing Sequence problem.
def solve(array):
    # Initially the highest sequence up to element i is the element itself
    #   of lenght 1
    lds = [1]*len(array)

    # Bases on the fact that:
    # lds[i] = 1 + max(lds[j] if j < i and arr[j] > arr[i])
    #   if no j satisfies, lds[i] = 1

    for i, _ in enumerate(array):
        new_value = 0
        for j in range(i):
            # Here automatically we have j < i
            if array[j] > array[i]:
                new_value = max(1, lds[j])
        lds[i] = 1 + new_value

    return max(lds)


def main():
    test_case = 1
    num = int(input())
    first = True

    # For each test case
    while num != -1:

        # Read numbers
        numbers = []
        while num != -1:
            numbers.append(num)
            num = int(input())
        ans = solve(numbers)

        # Deals with a newline after test cases
        if not first: print()
        else: first = False

        print("Test #{}:\nmaximum possible interceptions: {}"\
                .format(test_case, ans))

        test_case += 1
        num = int(input())

if __name__ == "__main__":
    main()
