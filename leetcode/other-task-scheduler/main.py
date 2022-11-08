from typing import List
from collections import Counter, deque
import heapq

# edge case where you want to prioritize/start the most common
# so you aren't bottlenecked at the end waiting on one task

# This solution does not guaranteed that the tasks are executed
# in the *least* amount of time. It only finds a solution that
# respects all the task delays.
class SolutionFinishTasks:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        delay = n + 1

        # orders task from most to least common
        num_tasks = Counter(tasks)
        tasks = {task: {"num": num, "delay": 0} for task, num in num_tasks.items()}

        time = 0
        while tasks:
            # finds a task with no delay to execute
            for task, stats in tasks.items():
                if stats["delay"] == 0:
                    stats["delay"] = delay

                    tasks[task]["num"] -= 1
                    if tasks[task]["num"] == 0:
                        del tasks[task]
                    break

            time += 1
            for task, stats in tasks.items():
                if stats["delay"] > 0:
                    tasks[task]["delay"] -= 1

        return time


# Greedy approach: the next task should always be one with no delay,
# but the largest number of remaining executions
class SolutionTooSlow:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        delay = n + 1

        num_tasks = Counter(tasks)
        tasks = {task: {"num": num, "delay": 0} for task, num in num_tasks.items()}

        time = 0
        while tasks:

            available = [task for task, stats in tasks.items() if stats["delay"] == 0]
            if available:
                # task with most remaining num
                next = max(available, key=lambda t: tasks[t]["num"])
                tasks[next]["delay"] = delay

                tasks[next]["num"] -= 1
                if tasks[next]["num"] == 0:
                    del tasks[next]

            time += 1
            for task, stats in tasks.items():
                if stats["delay"] > 0:
                    tasks[task]["delay"] -= 1

        return time


# Same idea as before, but with fewer copies and passes.
# Turns out to still be too slow, but slightly faster. Passes
# additional test cases.
class SolutionStillTooSlow:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        delay = n + 1

        num_tasks = Counter(tasks)
        tasks = {task: {"num": num, "delay": 0} for task, num in num_tasks.items()}

        time = 0
        while tasks:

            next = None
            max = 0
            for task, stats in tasks.items():
                if stats["delay"] == 0 and stats["num"] > max:
                    next, max = task, stats["num"]

            if next:
                tasks[next]["delay"] = delay

                tasks[next]["num"] -= 1
                if tasks[next]["num"] == 0:
                    del tasks[next]

            time += 1
            for task, stats in tasks.items():
                if stats["delay"] > 0:
                    tasks[task]["delay"] -= 1

        return time


class MaxHeap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)

    def push(self, item):
        heapq.heappush(self.data, -item)

    def pop(self):
        return -heapq.heappop(self.data)

    def __bool__(self):
        return bool(self.data)

    def __repr__(self) -> str:
        return repr(self.data)


# runtime: 0%!. Also provees that the greedy solution works.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        delay = n
        available = MaxHeap(list(Counter(tasks).values()))
        waiting = deque()

        time = 0
        while available or waiting:
            time += 1

            if waiting and time > waiting[-1][1] + delay:
                available.push(waiting.pop()[0])

            if available:
                remaining = available.pop() - 1
                if remaining:
                    waiting.appendleft((remaining, time))

        return time


cases = [
    (["A", "A", "A", "B", "B", "B"], 2, 8),
    (["A", "A", "A", "B", "B", "B"], 0, 6),
    (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
    (["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2, 12),
]

if __name__ == "__main__":
    for tasks, n, ans in cases:
        s = Solution()
        output = s.leastInterval(tasks, n)

        if output != ans:
            print(f"{tasks}, {n}, {output}: {ans}")
