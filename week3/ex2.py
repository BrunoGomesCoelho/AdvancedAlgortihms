def recursive_solve(nums, current, pos, count, total):
    if count == total:
        global answers
        answers.add(tuple(current))
        return
    if count > total:
        return
    size = len(nums)
    i = pos
    while i < size:
        recursive_solve(nums, current + [nums[i]], i+1, count+nums[i], total)
        j = i + 1
        while j < size:
            if nums[j] != nums[pos]:
                break
            j += 1
        i = j


def read_input():
    line = [int(x) for x in input().split()]
    return line[0], line[1], line[2:]

def main():
    total, n, nums = read_input()
    global answers
    answers = set()
    if n == 0:
        exit()
    recursive_solve(nums, [], 0, 0, total)
    print("anserws: ", answers)


if __name__ == "__main__":
    main()
