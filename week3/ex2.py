

def recursive_solve(answers, nums, current, pos, count, total):
    if count == total:
        answers.append(current)
        return
    if count > total:
        return
    
    size = len(nums)
    i = pos
    while i < size:
        recursive_solve(answers, nums, current + [nums[i]], pos+1, count+nums[i], total)
        for j in range(pos+1, size):
            if nums[j] != nums[pos]:
                break
        i = j



def read_input():
    line = [int(x) for x in input().split()]
    return line[0], line[1], line[2:]

def main():
    t, n , nums = read_input()
    answers = []
    if n == 0:
        exit()
   
    recursive_solve(answers, nums, [], 0, 0, t)
    print(answers)


if __name__ == "__main__":
    main()



