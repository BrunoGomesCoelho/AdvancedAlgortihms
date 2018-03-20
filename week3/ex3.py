SIZE = 8




def solver(matrix, row, ans):
    if row == SIZE:
        answer.append()

    
    for i in range(SIZE):
        new_matrix, problem = pick_col(matrix, row, i)
        if not problem:
            new_ans = ans + str(row)
            solver(new_matrix, row+1)


def main():
    ans = []
    


if __name__ == "__main__":
    main()



