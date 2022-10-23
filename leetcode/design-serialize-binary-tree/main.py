# Problem: https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/812/

from collections import deque
import pdb

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    
    def _list_to_string(self, lst):
        lst2 = []
        for value in lst:
            lst2.append('null' if value is None else str(value))
            
        return '[' + ','.join(lst2) + ']'
            
    
    def _dfs(self, node, nodes):
        
        queue = deque()
        queue.append(node)
        while queue:
            node = queue.pop()
            
            if node is None:
                nodes.append(None)
                continue
                
            nodes.append(node.val)
                            
            queue.appendleft(node.left)
            queue.appendleft(node.right)
    
        return nodes
        
    
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'
        
        nodes = []
        self._dfs(root, nodes)
        
        i = len(nodes) - 1
        while nodes[i] is None:
            i -= 1
            
        nodes = [nodes[j] for j in range(0, i + 1)]
        return self._list_to_string(nodes)
        
    def _string_to_list(self, s):
        
        s = s.lstrip('[').rstrip(']')
        nodes = []
        for value in s.split(','):
            nodes.append(None if value == 'null' else int(value))
            
        return nodes
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None

        data = self._string_to_list(data)
        
        nodes = [TreeNode(x) if x is not None else None for x in data]

        root = nodes[0]
                
        nodes = deque(nodes)
        queue = deque([nodes.popleft()])
        while nodes:            
            to_enqueue = len(queue) * 2
            
            index = 0
            while queue:
                node = queue.popleft()
                if node is None:
                    continue
                
                if index < len(nodes):
                    node.left = nodes[index]
                
                if index + 1 < len(nodes):
                    node.right = nodes[index + 1]
                
                index += 2
                
            while to_enqueue and nodes:
                if nodes[0] is None:
                    nodes.popleft()
                else:
                    queue.append(nodes.popleft())
                
                to_enqueue -= 1
                

        return root

root = TreeNode(1)
root.left = TreeNode(2)

rootr = TreeNode(3)
root.right = rootr
rootr.left = TreeNode(4)
rootr.right = TreeNode(5)

trees = [
    root
]

cases = [
    '[1,2,3,null,null,4,5]',
    '[]',
    '[1,2,3]',
    '[1,null,2,3]',
    '[5,4,7,3,null,2,null,-1,null,9]',
    '[1,2,3,null,null,4,5,6,7]',
    "[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]"
]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# ----> ans is a TreeNode
if __name__ == '__main__':
    print('str->Tree->str')
    for case in cases:
        ser = Codec()
        deser = Codec()    
        
        # print(deser._list_to_string(ser._string_to_list(case)))
        print(case)
        print(ser.serialize(deser.deserialize(case)))
        print()
        
    # print('\nTree->str')
    # for tree in trees:
    #     ser = Codec()
    #     deser = Codec()  
        
    #     print(ser.serialize(tree))