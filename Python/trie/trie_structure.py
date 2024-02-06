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
        # Create a new node for character if it doesn't already exist
        # else return the node at that charater position.
        current_node = current_node.children.setdefault(
            word[index], TrieNode())
        # increase word count and character index by 1
        current_node.count += 1
        index += 1

        if index < len(word):
            # Go over same process for the rest of the characters in
            # the word.
            self.insert(current_node=current_node, word=word, index=index)
        else:
            # At the last character of the word. set that word attribute
            # to true to indicate a word ends there.
            current_node.word = True

    def delete(self, current_node: TrieNode, word: str, index: int = 0):
        """Delete word in trie."""
        character = word[index]
        next_node = current_node.children.get(character)
        # Next node will start from first character in word to the end.
        # When the character is not found, word doesn't exist in storage.
        if next_node is None:
            return False
        # Increase index count to next character in word
        index += 1
        if index < len(word):
            # call funx again to search more character if end of word
            # isn't reached.
            self.delete(current_node=next_node, word=word, index=index)
        elif index == len(word) and next_node.word:
            # If end of word to delete is reached and it exists in storage
            # set it to false such that no word ends there anymore
            next_node.word = False
        else:
            # if both conditions are not satisfied, then the word you're
            # trying to delete is a prefix and such cannot be deleted.
            raise RecursionError('Not a word.')
        # This is were deleting actually occurs.
        # Reduce the count of word in character if it's used in other
        # words. Delete character node otherwise.
        if next_node.count > 1:
            next_node.count -= 1
        else:
            del current_node.children[character]

        return True

    def search(self, current_node: TrieNode, word: str, index: int = 0,
               prefix=True) -> bool:
        """Search trie storage for word."""
        # Get node holding each character in word.
        current_node = current_node.children.get(word[index])
        index += 1
        if not current_node:
            # This happens when no node is present for character
            return False
        # Continue search if not end of word
        if index < len(word):
            return self.search(current_node=current_node, word=word,
                               index=index, prefix=prefix)
        else:
            # return true if end of word is reached or word is a
            # prefix else false
            return prefix or current_node.word
        
    def word_break_search(self, current_node: TrieNode, word: str, 
                          index: int=0) -> bool:
        """Search dictionary for words built from input string."""
        current_node = current_node.children.get(word[index])
        # Return false when not doesn't exist in dictionary.
        if current_node is None:
            return False
        
        search_result = False
        index += 1 # Increase index after fetching node value
        # If word is reached, start searching for next character from root 
        # node or continue searching for longer word.
        if current_node.word:
            if index < len(word):
                path_a = self.word_break_search(current_node=self.root, 
                                                word=word, index=index)
                if path_a:
                    search_result = path_a
                else:
                    path_b = self.word_break_search(
                        current_node=current_node, word=word, index=index)
                    search_result = path_b
            else:
                search_result = True
        else:
            # if node exist but word doesn't end there, continue searching 
            # through the characters of the word till the end. If char end is
            # reached and word doesn't end there then return False.

            if index < len(word):
                search_result = self.word_break_search(
                    current_node=current_node, word=word, index=index)
            else:
                search_result = False

        return search_result
                

    def print_words(self, current_node: TrieNode, word: str = ''):
        """Print all words in storage."""
        for character, node in current_node.children.items():
            # Loop through every characters registered in node and print
            # if a word ends there.
            if node.word:
                print(word+character)
                # Continue to search down if word end is a prefix of
                # another word.
                if node.count > 1:
                    self.print_words(node, word+character)
            else:
                # Call function again with next node if end of word is
                # not reached yet.
                self.print_words(node, word+character)
