from copy import deepcopy
from queue import PriorityQueue

MATRIX_SIZE = 4


def read_matrix():
    matrix = []

    for _ in range(MATRIX_SIZE):
        matrix.append([int(x) for x in input().split()])

    return matrix

def read_test_cases():
    n = int(input())
    test_cases = []

    for _ in range(n):
        test_cases.append(read_matrix())

    return test_cases

def calculate_permutations(matrix):
    options = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]
    permutations = []
    row = col = -1
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            if matrix[i][j] == 0:
                row = i
                col = j

    for i, j, letter in options:
        if 0 <= row + i < MATRIX_SIZE and 0 <= col + j < MATRIX_SIZE:
            temp = deepcopy(matrix)  # creates a copy of the matrix so we dont change it in place
            temp[row][col], temp[row+i][col+j] = temp[row+i][col+j], temp[row][col]
            permutations.append((temp, letter))

    return permutations

def check_answer(matrix):
    answer = True
    for i in range(MATRIX_SIZE):
        for j in range(1, MATRIX_SIZE + 1):
            if matrix[i][j-1] != i*MATRIX_SIZE + j and (i != MATRIX_SIZE - 1 or j != MATRIX_SIZE):
                answer = False
    return answer


def count_inversions(array):
    """Function for counting the amount of inversions in """
    count = 0
    size = MATRIX_SIZE*MATRIX_SIZE

    for i in range(size-1):
        for j in range(i+1, size):
            if array[i] != 0 and array[j] != 0 and array[i] > array[j]:
                count += 1

    return count


def has_answer(matrix):
    """For checking if the puzzle is solvable, we used the following side as a guide:
        http://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
    Resuming, the puzzle instance is solvable if
        the blank is on an even and number of inversions is odd.
        the blank is on an odd row and number of inversions is even.
    """
    zero_pos = -1
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            if matrix[i][j] == 0:
                zero_pos = i

    inversions = count_inversions([num for row in matrix for num in row])

    return (zero_pos % 2 == 0 and inversions % 2 == 1) or (
            zero_pos % 2 == 1 and inversions % 2 == 0)


def tuplize(matrix):
    """Returns a linear version of a matrix"""
    return tuple([num for row in matrix for num in row])



def calculate_heuristic(matrix):
    """We use the Manhattan Distance between the given piece and where it should be on the bord
    It is a admissible heuristic.
    """
    cost = 0
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            num = matrix[i][j]
            if num != i*MATRIX_SIZE + (j+1) and num != 0:
                correct_row = (num - 1) // MATRIX_SIZE
                correct_col = (num - 1) % MATRIX_SIZE
                cost += abs(i - correct_row) + abs(j - correct_col)
    return cost


def main():

    test_cases = read_test_cases()

    for test_case in test_cases:
        answer = "This puzzle is not solvable."
        queue = PriorityQueue()
        visited = set()

        if not has_answer(test_case):
            print(answer)
            continue

        """
        The queue follows the order
            total cost, level, matrix, answer
        for all elements """
        queue.put((0, 0, test_case, ""))

        while not queue.empty():
            _, level, matrix, current_answer = queue.get()

            if level > 50:
                break

            if check_answer(matrix):
                answer = current_answer
                break

            permutations = calculate_permutations(matrix)

            for permutation, letter in permutations:
                # A tuple is necessary for storing in a set since it is immutable
                permutation_tuple = tuplize(permutation)
                if permutation_tuple not in visited:
                    heuristic_cost = calculate_heuristic(permutation)
                    visited.add(permutation_tuple)
                    queue.put((heuristic_cost+level+1,
                               level+1,
                               permutation,
                               current_answer + letter
                              ))

        print(answer)

if __name__ == "__main__":
    main()
