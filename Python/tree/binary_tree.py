from collections import deque
from typing import List


class Node:
    def __init__(self, val: int) -> None:
        self.info = val
        self.left = None
        self.right = None
        self.level = None


class BinaryTree:
    def __init__(self, root_val: Node | None=None):
        self.root = root_val

    def set_val(self, node: Node, val: int) -> None:
        if val >= node.info:
            if node.right is None:
                node.right = Node(val)
            else:
                self.set_val(node.right, val)
        else:
            if node.left is None:
                node.left = Node(val)
            else:
                self.set_val(node.left, val)

    def add_node(self, val: int) -> None:
        if self.root is None:
            self.root = Node(val=val)
        else:
            self.set_val(self.root, val)

    def get_preorder(self) -> str:
        pass

    def get_postorder(self) -> str:
        pass

    def levelOrder(self):
        # Write your code here
        vals = ''
        nodes = deque([self.root])
        
        while True:
            try:
                node = nodes.popleft()
            except IndexError:
                break
            
            vals = node.info if not vals else f'{vals} {node.info}'
                
            if node.left:
                nodes.append(node.left)
                
            if node.right:
                nodes.append(node.right)
                
        print(vals)

    def _get_max_height(self, node, prev, max_height):
        try:
            height = node.height
        except AttributeError:
            node.height = prev + 1
            max_height = max(node.height, max_height)
        else:
            max_height = max(height, max_height)
            
        if node.left is None and node.right is None:
            return max_height
        if node.left:
            max_height = self.get_max_height(node.left, node.height, max_height)
        if node.right:
            max_height = self.get_max_height(node.right, node.height, max_height)

        return max_height
    
    def height(self):
        self.root.height = 0
        max_height = self.root.height
        max_height = self._get_max_height(self.root, self.root.height, self.root.height)
        return max_height

class TreeNode:
    """Define tree operations."""
    
    def __init__(self, val: int) -> None:
        """Initialize a tree."""
        self.val = val
        self.left: self.__class__ = None
        self.right: self.__class__ = None
        
    def add_nodes(self, vals: List[int]) -> None:
        """Add nodes whoes values are what is in array."""
        queues = [self]
        root = None
        
        for node_vals in vals:
            first = node_vals[0]
            second = node_vals[1]
            if first != -1 or second != -1:
                root = queues.pop(0)
            if first == -1 and second == -1:
                queues.pop(0)
                continue
                
            if first != -1:
                root.left = self.__class__(val=first)
                queues.append(root.left)
            if second != -1:
                root.right = self.__class__(val=second)
                queues.append(root.right)
                
    def inorder_traversal(self) -> List[int]:
        """Traverse tree from left to right."""
        vals = []
        
        def traverse(node, vals) -> None:
            if node.left:
                traverse(node=node.left, vals=vals)
            vals.append(node.val)
            if node.right:
                traverse(node=node.right, vals=vals)
                
        traverse(self, vals=vals)
        return vals