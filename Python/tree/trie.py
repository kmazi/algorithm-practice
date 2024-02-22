"""Define trie datastructure functionalities."""
from __future__ import annotations
from typing import Dict, List


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


class LongestPrefixTrie(Trie):
    def __init__(self):
        """Set root node to be TrieNode instance."""
        self.root = TrieNode()

    def insert(self, current_node: TrieNode, words: List[str], index=0, 
               cha_index=0, common_prefix='') -> str:
        """Insert words into trie node.

        Arguments:
        ---
            current_node -- Current node to insert character. 

            words -- A list of words to insert.

            index -- Index of word currently being inserted.

            cha_index -- Index of character in word being inserted.

            common_prefix -- Common prefix in all words.
        """
        if index < len(words):
            word = words[index]
            character = word[cha_index]
            # Get node representing character if exist or create new node
            # for it and return the created node
            current_node = current_node.children.setdefault(character, 
                                                            TrieNode())
            # Increase cha_index for adding the next character to the trie
            # increase word count on node after adding character.
            cha_index += 1
            current_node.count += 1
            # Add character to common prefix if words formed with it is 
            # equal to the number of words so far. I.e all words seen
            # uses that character as prefix
            if current_node.count == index+1:
                common_prefix += character

            if cha_index < len(word):
                common_prefix = self.insert(current_node, words, index, 
                                            cha_index, common_prefix)
            else:
                index += 1
                current_node.word = True
                # Return common prefix after adding all words or when
                # there's no common prefix. Continue adding words otherwise
                if index == len(words) or len(common_prefix) == 0:
                    return common_prefix

                common_prefix = self.insert(self.root, words, index)
        return common_prefix


class SuffixTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, current_node: TrieNode, word: str, suff_index: int=0, 
               cha_index: int=0, count=0) -> int:
        """Insert characters of word into suffix trie.
        Arguments:
        ---
            current_node -- The node to insert character node.

            word -- word from which characters are inserted.

            suffix_index -- The start index of a suffix for insertion.

            cha_index -- Character position in suffix to insert in a node

            count -- Number of distinct node seen so far.

        Returns:
            int -- Total number of distinct substrings of word.
        """
        position = suff_index + cha_index
        length = len(word)
        # index start from the begining of word to the end. after exploring
        # suffix starting at index, the value moves by 1 until it gets to
        # end of string.
        if suff_index == length:
            return count
        if position < length:
            # Position is the index of character to be added to a node.
            # its the character index + the suffix index
            character = word[position]
            current_node = current_node.children.setdefault(character, 
                                                            TrieNode())
            current_node.count += 1
            cha_index += 1
            # if word count on a node is 1 then count it. The total number
            # nodes in the trie represents the number of distinct substring
            # in the word.
            if current_node.count == 1:
                count += 1
            # Continue adding characters of current suffix
            count = self.insert(current_node, word, suff_index, cha_index, 
                                count)
        else:
            current_node.word = True
            # Start adding another suffix
            count = self.insert(self.root, word, suff_index+1, 0, count)

        return count
    
    def print_all_substrings(self, current_node: TrieNode, word: str='', 
                             substrings: List[str]=[]):
        """Print all substrings in suffix trie.
        
        Arguments:
        ---
            currentNode -- The node being explored.

            word -- word built from characters representing nodes
            
            substrings -- List of substrings from word
            
        Returns:
        ---
            List: Array of substrings.
        """
        for character, node in current_node.children.items():
            # Append every character represented in every previous nodes
            # to  the character of current node. Append word formed to 
            # substring array.
            substrings.append(word+character)
            self.print_all_substrings(node, word+character, substrings)
        return substrings;


if __name__ == '__main__':
    # SuffixTrie Test
    word = 'traction'
    suffix_trie = SuffixTrie()
    no_of_distrinct_substring = suffix_trie.insert(suffix_trie.root, 
                                                   word=word)
    print(f'Number of distinct substring in word "{word} is {no_of_distrinct_substring}"', 
          end='\n\n')
    print('Here are all the substrings:', 
          suffix_trie.print_all_substrings(suffix_trie.root))

    # Trie test
    print('Trie Test', end='\n\n')
    words = ['late', 'win', 'always', 'allwell', 'at', 'worse']
    print('Words in Trie dictionary are:', words)
    trie = Trie()
    for word in words:
        trie.insert(current_node=trie.root, word=word)

    words_to_search = ['lat', 'always', 'win', 'att']
    for word in words_to_search:
        result = trie.search(trie.root, word, prefix=False)
        response = 'Yes' if result else 'No'
        present = '' if result else 'not '
        print(f'{response} the search word "{word}" is {present}in the dictionary.')

    # Prefix trie test
    print('PrefixTrie tests', end='\n\n')
    words = ['salvation', 'salvory', 'salvage']
    print('All words in the dictionary:')

    longest_common_prefix = LongestPrefixTrie()
    print('Longest common prefix is:', longest_common_prefix.insert(
        longest_common_prefix.root, words))
    longest_common_prefix.print_words(longest_common_prefix.root)
    
    # prints out: 'salv'
