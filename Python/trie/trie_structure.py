"""Define trie datastructure functionalities."""
from __future__ import annotations
from typing import Dict


class TrieNode:
    """Define a node in trie datastructure."""

    def __init__(self):
        """Initialize node children."""
        self.children: Dict[str, 'TrieNode'] = {}
        self.word = False
        self.count = 0


class Trie:
    """Define insert, search and delete ops for trie."""

    def __init__(self):
        """Set root val for trie."""
        self.root = TrieNode()

    def insert(self, current_node: TrieNode, word: str, 
               index: int = 0) -> None:
        """Add word to trie structure."""

        current_node = current_node.children.setdefault(
            word[index], TrieNode())
        # increase word count by 1
        current_node.count += 1

        index += 1

        if index < len(word):
            self.insert(current_node=current_node, word=word, index=index)
        else:
            current_node.word = True

    def delete(self, current_node: TrieNode, word: str, index: int=0):
        character = word[index]
        next_node = current_node.children.get(character)
        if next_node is None:
            return False
        
        index += 1
        if index < len(word):
            self.delete(current_node=next_node, word=word, index=index)
        elif index == len(word) and next_node.word:
            next_node.word = False
        else:
            raise RecursionError('Not a word.')

        if next_node.count > 1:
            next_node.count -= 1
        else:
            del current_node.children[character]

        return True

    def search(self, current_node: TrieNode, word: str, index: int=0, 
               prefix=True) -> bool:
        """Search trie storage for word."""
        current_node = current_node.children.get(word[index])
        index += 1
        if not current_node:
            return False
        
        if index < len(word):
            return self.search(current_node=current_node, word=word, 
                                index=index, prefix=prefix)
        else:
            return prefix or current_node.word
