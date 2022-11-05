import pdb
from random import randint


class RandomizedSetSetUpAPI:

    s = set()

    def __init__(self):
        self.s = set

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False

        self.s.add(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False

        self.s.remove(val)
        return True

    def getRandom(self) -> int:
        rand_element = self.s.pop()
        self.s.add(rand_element)

        return rand_element


class RandomizedSetClose:
    def __init__(self):
        self.val_idx = {}
        self.a = []
        self.n = 0

    def _swap(self, i, j):
        temp = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = temp

    def insert(self, val: int) -> bool:
        if val in self.val_idx:
            return False

        # increase number of elements to keep and set
        # index of val to the end of the range
        self.n += 1
        self.val_idx[val] = self.n - 1

        if len(self.a) < self.n:
            self.a.append(val)
        else:
            self.a[self.n - 1] = val

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_idx:
            return False

        # set the index of the last element in keep range
        # to the index of "val"
        self.val_idx[self.a[self.n - 1]] = self.val_idx[val]

        # swap val with the last element within "keep" range
        self._swap(self.val_idx[val], self.n - 1)

        # decrease size of keep range
        self.n -= 1

        del self.val_idx[val]

        return True

    def getRandom(self) -> int:
        return self.a[randint(0, self.n - 1)]


class RandomizedSet:
    def __init__(self):
        self.val_idx = {}
        self.a = []

    def insert(self, val: int) -> bool:
        if val in self.val_idx:
            return False

        self.a.append(val)
        self.val_idx[val] = len(self.a) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_idx:
            return False

        idx_to_remove = self.val_idx[val]

        self.a[idx_to_remove], self.a[-1] = self.a[-1], self.a[idx_to_remove]

        self.val_idx[self.a[idx_to_remove]] = idx_to_remove

        self.a.pop()
        del self.val_idx[val]

        return True

    def getRandom(self) -> int:
        return self.a[randint(0, len(self.a) - 1)]


cases = [
    (
        [
            "RandomizedSet",
            "insert",
            "remove",
            "insert",
            "getRandom",
            "remove",
            "insert",
            "getRandom",
        ],
        [[], [1], [2], [2], [], [1], [2], []],
        [None, True, False, True, 2, True, False, 2],
    ),
    (
        [
            "RandomizedSet",
            "insert",
            "remove",
            "insert",
            "getRandom",
            "remove",
            "insert",
            "getRandom",
        ],
        [[], [-1], [-2], [-2], [], [-1], [-2], []],
        [None, True, False, True, -2, True, False, -2],
    ),
    (
        [
            "RandomizedSet",
            "insert",
            "insert",
            "remove",
            "insert",
            "remove",
            "getRandom",
        ],
        [[], [0], [1], [0], [2], [1], []],
        [None, True, True, True, True, True, 2],
    ),
]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
if __name__ == "__main__":

    for case in cases:
        rs = RandomizedSet()

        for cmd, input, ans in zip(case[0], case[1], case[2]):
            if cmd == "RandomizedSet":
                continue

            operation = getattr(rs, cmd)
            if cmd == "getRandom":
                output = operation()
            else:
                output = operation(input[0])

            if output != ans:
                print(f"cmd={cmd}, input={input}, output={output}, ans={ans}")
