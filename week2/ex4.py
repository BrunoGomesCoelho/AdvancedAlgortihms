import sys
from collections import deque
from heapq import heappush, heappop


def print_answer(count, stack_valid, queue_valid, priority_queue_valid):
    if count == 1:
        if stack_valid:
            print("stack")
        elif queue_valid:
            print("queue")
        elif priority_queue_valid:
            print("priority queue")
    elif count > 1:
        print("not sure")
    else:
        print("impossible")


def check_data_stucture(cmds, stack, queue, priority_queue):
    stack_valid = queue_valid = priority_queue_valid = True

    for _ in range(cmds):
        cmd, num = map(int, input().split())
        # insertion
        if cmd == 1:
            stack.append(num)
            queue.append(num)
            heappush(priority_queue, -num)
        # deletion
        elif cmd == 2:
            if num != stack.pop():
                stack_valid = False
            if num != queue.popleft():
                queue_valid = False
            if num != -heappop(priority_queue):
                priority_queue_valid = False
        else:
            print("ERROR - INVALID INPUT")
            exit(1)

    count = [stack_valid, queue_valid, priority_queue_valid].count(True)
    print_answer(count, stack_valid, queue_valid, priority_queue_valid)

def main():
    while True:
        try:
            cmds = int(input())
            check_data_stucture(cmds, deque(), deque(), [])
        except:
            break


if __name__ == "__main__":
    main()
