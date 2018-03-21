SIZE = 8

def valid_diagonal(cols, x, y):
    for y0, x0 in enumerate(cols):
        if y0 != y and x0 != -1 and abs(x-x0) == abs(y-y0):
            return False
    return True

def pick_col(cols, x, y):
    if x in cols or not valid_diagonal(cols, x, y):
        return cols, False
    return [row if col != y else x for col, row in enumerate(cols)], True


def solver(all_ans, cols, y):

    if all(x != -1 for x in cols):
        all_ans.append(cols)
        return
    if cols[y%SIZE] != -1:
        return
    for x in range(SIZE):
        new_cols, valid = pick_col(cols, x=x, y=y)
        if valid:
            solver(all_ans, new_cols, y=(y+1)%SIZE)

def main():
    test_cases = int(input())
    input()
    for i in range(test_cases):
        all_ans = []
        x, y = [int(num)-1 for num in input().split()]
        cols = [-1]*8
        cols[y] = x
        solver(all_ans, cols, (y+1)%SIZE)
        # Printing answer
        print("SOLN    COLUMN")
        print(" #\t\t1 2 3 4 5 6 7 8")
        print()
        all_ans.sort()
        for idx, ans in enumerate(all_ans):
            if idx + 1 < 10:
                print(" ", end="")
            print(idx+1,"      ", sep="", end="")
            print(" ".join(str(x+1) for x in ans))
        if i != test_cases-1:
            print()
if __name__ == "__main__":
    main()
