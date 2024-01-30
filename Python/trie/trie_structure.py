"""Define trie datastructure functionalities."""
from __future__ import annotations
from typing import Dict


class TrieNode:
    """Define a node in trie datastructure."""

    def __init__(self):
        """Initialize node children."""
        self.children: Dict[str, 'TrieNode'] = {}
        self.word = False


class Trie:
    """Define insert, search and delete ops for trie."""

    def __init__(self):
        """Set root val for trie."""
        self.root = TrieNode()

    def insert(self, word: str, index: int = 0) -> None:
        """Add word to trie structure."""
        if index == 0:
            self.current_node = self.root

        self.current_node = self.current_node.children.setdefault(
            word[index], TrieNode())

        index += 1

        if index < len(word):
            self.insert(word=word, index=index)
        else:
            self.current_node.word = True

    def search(self, word: str, index: int=0, prefix=True) -> bool:
        """Search trie storage for word."""
        if index == 0:
            self.current_node = self.root

        self.current_node = self.current_node.children.get(word[index])
        index += 1
        if self.current_node:
            if index >= len(word):
                if prefix or self.current_node.word:
                    return True
                else:
                    return False
                
            else:
                return self.search(word=word, index=index, prefix=prefix)
        else:
            return False
