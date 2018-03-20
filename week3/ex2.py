from math import inf

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

def sort_list(lst):
    if not lst:
        return []
    # gets the biggest tuple in out list
    size = len(max(lst, key=lambda tup: len(tup)))
    """
    Sorts the list various time, by order of last element to first.
    Since the sorting is stable, this sorts first by the first number, then
        the second, then the third, etc.
    The reason of this roundabout way is that the tuples dont have the same
        size so we cant compare by ans[i] otherwise we get a index error.
    """
    for i in reversed(range(size)):
        lst = sorted(lst, key=lambda ans: -ans[i] if len(ans) > i else -inf) 
    return lst

def read_input():
    line = [int(x) for x in input().split()]
    if line[0] == 0:
        exit()
    return line[0], line[1], line[2:]

def main():
    while True:
        total, n, nums = read_input()
        global answers
        answers = set()
        recursive_solve(nums, [], 0, 0, total)
        answers = sort_list(list(answers))
        print("Sums of %d:" % total)
        if answers:
            for ans in answers:
                for num in ans[:-1]:
                    print(num, end="+")
                print(ans[-1])
        else:
            print("NONE")

if __name__ == "__main__":
    main()
