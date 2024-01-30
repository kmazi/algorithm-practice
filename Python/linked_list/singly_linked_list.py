"""Solve problems involving singly linked list."""
from __future__ import annotations
from typing import List, Optional


class SinglyLinkedList:
    """Define a singly linked list."""
    def __init__(self):
        """Set linkedlist root node."""
        self.head: Optional[SinglyListNode] = None
        
        
class SinglyListNode:
    def __init__(self, val: int) -> None:
        """Initialize linkedlist node."""
        self.data = val
        self.next: Optional['SinglyListNode'] = None
        
    def print_list(self, node, result):
        result.append(node.data)
        if node.next:
            self.print_list(node.next, result)
        
def insert_node(node: Optional[SinglyListNode], 
                data: int) -> None:
    """Insert node recursively."""
    if node.next is not None:
        insert_node(node.next, data)
    else:
        node.next = SinglyListNode(val=data)


def insertNodeAtTail(head: Optional[SinglyListNode], 
                     data: int) -> SinglyListNode:
    """Insert a node at the end of a singly linkedlist."""
    if head is None:
        head = SinglyLinkedList().head = SinglyListNode(val=data)
    else:
        insert_node(head, data)
    return head


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


class SinglyListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        """Print the value of objects root node."""
        return str(f'Node value is: {self.val}')


class LinkedList:
    """Define functionalities to manipulate a linked(singly) list."""

    def __init__(self, root: Optional[SinglyListNode] = None) -> None:
        """Set linked list root value."""
        self.root = root

    def __str__(self):
        """Print the value of objects root node."""
        return str(f'Node root is: {self.root.val}')

    def add_node_iteration(self, node_val: int) -> None:
        """Add a node to the end of the linked list."""
        new_node = SinglyListNode(val=node_val)
        if not self.root:
            self.root = new_node
        else:
            last_node = self.root
            # Iterate to the last node in the list
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def add_multiple_nodes_iteration(self, vals: List[int]):
        """Add multiple nodes."""
        for val in vals:
            if not self.root:
                self.root = SinglyListNode(val=val)
            else:
                last_node = self.root
                while last_node.next:
                    last_node: SinglyListNode = last_node.next
                last_node.next = SinglyListNode(val=val)

    def search_nodes_iteration(self, val: int) -> Optional[SinglyListNode]:
        """Search through nodes for a value."""
        node = self.root
        while node:
            if node.val == val:
                return node
            node = node.next
        return None

    def search_nodes_recursion(self, val: int) -> Optional[SinglyListNode]:
        """Search through nodes for a value recursively."""
        node = self.root

        def search(start_node):
            """Search through nodes for a value recursively."""
            result = None
            if start_node and start_node.val == val:
                result = start_node
            else:
                if start_node and start_node.next:
                    result = search(start_node=start_node.next)
            return result
        return search(node)

    def display_all_nodes_iteration(self) -> List[int]:
        """Display values of linkedlist as array."""
        vals = []
        node = self.root
        while node:
            vals.append(node.val)
            node = node.next

        return vals

    def length_iteration(self) -> int:
        """Compute length of nodes in linkedlist."""
        length = 0
        node = self.root
        while node:
            length += 1
            node = node.next
        return length


class Solution:
    def add_two_numbers(self, l1: Optional[SinglyListNode],
                        l2: Optional[SinglyListNode]) -> Optional[SinglyListNode]:
        list_sum, prev_node, remainder = None, None, 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + remainder
            val = total % 10
            remainder = total // 10

            if list_sum is None:
                prev_node = list_sum = SinglyListNode(val)
            else:
                prev_node.next = prev_node = SinglyListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if remainder:
            prev_node.next = SinglyListNode(remainder)

        return list_sum

    def add_two_numbers_recursively(
            self, l1: Optional[SinglyListNode],
            l2: Optional[SinglyListNode]) -> Optional[SinglyListNode]:
        list_node = SinglyListNode(None)
        remainder = 0

        def add_up(linked_list: SinglyListNode, n1: SinglyListNode,
                   n2: SinglyListNode, remainder: int) -> None:
            total = getattr(n1, 'val', 0) + getattr(n2, 'val', 0) + remainder
            val = total % 10
            remainder = total // 10
            linked_list.val = val

            n1 = getattr(n1, 'next', None)
            n2 = getattr(n2, 'next', None)
            if n1 or n2:
                linked_list.next = SinglyListNode()
                add_up(linked_list=linked_list.next, n1=n1, n2=n2,
                       remainder=remainder)
            else:
                if remainder:
                    linked_list.next = SinglyListNode(remainder)

        add_up(linked_list=list_node, n1=l1, n2=l2, remainder=remainder)
        return list_node
