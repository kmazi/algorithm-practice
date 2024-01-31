"""Execute any of the algorithms for testing purpose."""

from linked_list.singly_linked_list import SinglyListNode, LinkedList
from tree.binary_tree import TreeNode
from trie.trie_structure import Trie

# if __name__ == '__main__':
#     linked_list = LinkedList(root=ListNode(3))

#     linked_list.add_node_iteration(3)
#     linked_list.add_node_iteration(1)
#     linked_list.add_node_iteration(4)
#     linked_list.add_node_iteration(2)
#     linked_list.add_node_iteration(5)

#     print('Length of linked list is', linked_list.length_iteration())
#     values = linked_list.display_all_nodes_iteration()
#     print('Here are the values in your linkedlist')
#     for v in values:
#         print(v)

#     linked_list = LinkedList()
#     linked_list.add_multiple_nodes_iteration([3,4,7,1,4])

#     print('Length of linked list is', linked_list.length_iteration())
#     values = linked_list.display_all_nodes_iteration()
#     print('Here are the values in your linkedlist')
#     for v in values:
#         print(v)

#     print('Searching for 0')
#     print(linked_list.search_nodes_recursion(0))


if __name__ == "__main__":
    words = ['late', 'win', 'always', 'allwell', 'at', 'worse']
    trie = Trie()
    for word in words:
        trie.insert(current_node=trie.root, word=word)

    while True:
        print('Enter a search word:')
        search_word = input()
        print('Do you want to search for full word?')
        prefix = True if input().lower() == 'no' else False
        if search_word == '.exit' or search_word == '':
            print('Bye..')
            break

        word_is_in_dictionary = trie.search(current_node=trie.root, word=search_word, prefix=prefix)
        response = 'Yes' if word_is_in_dictionary else 'No'
        present = '' if word_is_in_dictionary else 'not '
        print(f'{response} the search word "{search_word}" is {present}in the dictionary.')
