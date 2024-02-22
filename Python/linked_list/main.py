"""Execute any of the algorithms for testing purpose."""

from tkinter.tix import ListNoteBook
from linked_list.singly_linked_list import LinkedList
from Python.tree.trie import Trie

if __name__ == '__main__':
    # Linkedlist test
    linked_list = LinkedList(root=ListNoteBook(3))

    linked_list.add_node_iteration(3)
    linked_list.add_node_iteration(1)
    linked_list.add_node_iteration(4)
    linked_list.add_node_iteration(2)
    linked_list.add_node_iteration(5)

    print('Length of linked list is', linked_list.length_iteration())
    values = linked_list.display_all_nodes_iteration()
    print('Here are the values in your linkedlist')
    for v in values:
        print(v)

    linked_list = LinkedList()
    linked_list.add_multiple_nodes_iteration([3,4,7,1,4])

    print('Length of linked list is', linked_list.length_iteration())
    values = linked_list.display_all_nodes_iteration()
    print('Here are the values in your linkedlist')
    for v in values:
        print(v)

    print('Searching for 0')
    print(linked_list.search_nodes_recursion(0))
