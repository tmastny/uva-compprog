from typing import List
from collections import Counter

# edge case where you want to prioritize/start the most common
# so you aren't bottlenecked at the end waiting on one task

# This solution does not garauntee that the tasks are executed
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


class Solution:
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