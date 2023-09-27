import heapq

from math import log2
from dataclasses import dataclass, field

@dataclass(order=True, init=False)
class Node:
    freq: float
    name: str = field(compare=False)

    def __init__(self, name, freq, l=None, r=None):
        self.p = None

        if l != None:
            l.p = self
        self.l = l

        if l != None:
            r.p = self
        self.r = r

        self.name = name
        self.freq = freq
    

class HuffmanEncoding:
    def __init__(self, freqs: dict) -> None:
        self.freqs = freqs

        queue = [Node(char, f) for char, f in freqs.items()]
        heapq.heapify(queue)

        while len(queue) > 1:
            node_i = heapq.heappop(queue)
            node_j = heapq.heappop(queue)

            sum = node_i.freq + node_j.freq
            tree = Node(None, sum, l=node_i, r=node_j)

            heapq.heappush(queue, tree)

        self.tree = tree

    def decode(self, bits):
        text = ""

        i = 0
        while i < len(bits):
            node = self.tree
            
            while node.name is None:
                if bits[i] == '1':
                    node = node.r
                elif bits[i] == '0':
                    node = node.l
                else:
                    raise Exception("Invalid code")

                i += 1
            
            text += node.name
        
        return text

    def encode(self, text: str):
        text = text.lower()
        code = self.encoding()

        bits = ""
        for letter in text:
            if letter in code:
                bits += code[letter]
        
        return bits

    def encoding(self):
        code = {}
        stack = [(self.tree, "")]

        while stack:
            node, bits = stack.pop()
            if node.l is None:
                code[node.name] = bits
            else:
                stack.append((node.l, bits + "0"))
                stack.append((node.r, bits + "1"))

        return code

    def cost(self):
        cost = 0
        stack = [self.tree]

        while stack:
            node = stack.pop()
            cost += node.freq
            if node.l != None:
                stack.append(node.l)
                stack.append(node.r)
        
        cost -= self.tree.freq
        return cost, cost / self.total()

    def total(self):
        frequencies = [freq for _, freq in self.freqs.items()]
        total = 0
        for freq in frequencies:
            total += freq
        
        return total

    def entropy(self):
        frequencies = [freq for _, freq in self.freqs.items()]

        total = self.total()
        if total > 1.001:
            frequencies = [freq / total for freq in frequencies]

        entropy = 0
        for freq in frequencies:
            entropy -= freq * log2(freq)
        
        return entropy


data = [
    {
        " ": 0.183,
        "e": 0.102,
        "t": 0.077,
        "a": 0.068,
        "o": 0.059,
        "i": 0.058,
        "n": 0.055,
        "s": 0.051,
        "h": 0.049,
        "r": 0.048,
        "d": 0.035,
        "l": 0.034,
        "c": 0.026,
        "u": 0.024,
        "m": 0.021,
        "w": 0.019,
        "f": 0.018,
        "g": 0.017,
        "y": 0.016,
        "p": 0.016,
        "b": 0.013,
        "v": 0.009,
        "k": 0.006,
        "j": 0.002,
        "x": 0.002,
        "q": 0.001,
        "z": 0.001,
    },
    {
        " ": 7,
        "a": 4,
        "e": 4,
        "f": 3,
        "h": 2,
        "i": 2,
        "m": 2,
        "n": 2,
        "s": 2,
        "t": 2,
        "l": 1,
        "o": 1,
        "p": 1,
        "r": 1,
        "u": 1,
        "x": 1,
    },
    {"A": 31, "C": 20, "G": 9, "T": 40},
    {"a": 0.5, "b": 0.25, "c": 0.125, "d": 0.0625, "e": 0.0625},
    {"A": 70, "B": 3, "C": 20, "D": 37},
    {"1": 100, "2": 100, "3": 300, "4": 210, "5": 150},
    {"a": .25, "b": .25, "c": .25, "d": .125, "e": .125},
    {"a": 0.5, "b": 0.25, "c": 0.125, "d": 0.0625},
]

for freqs in data:
    huffman = HuffmanEncoding(freqs)
    code = huffman.encoding()
    cost, weighted = huffman.cost()
    entropy = huffman.entropy()
    print(f"cost: {cost:<10}, weighted: {weighted:<.3f}, entropy: {entropy:<.3f}, code: {code}")

    if len(freqs) > 15:
        message = "Hello world! Welcome to my killer planet Xander."
        print(f"message: {message}")

        bits = huffman.encode(message)
        print(f"encoded message: len: {len(bits)}, {bits}")
        
        decoded = huffman.decode(bits)
        print(f"decoded message: {decoded}")