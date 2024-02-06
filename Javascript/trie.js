class TrieNode {
    constructor() {
        this.children = new Map();
        this.wordEnd = false;
        this.count = 0;
    }
}


class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insertWord(currentNode, word, index=0) {
        // Get node represented by character if it exists or create
        // a new node for it.
        const character = word[index];
        let nextNode = currentNode.children.get(character);
        if (nextNode === undefined) {
            nextNode = currentNode.children.set(character, 
                new TrieNode()).get(character);
        }
        // increase word count and character index by 1
        nextNode.count += 1;
        index += 1;

        if (index < word.length) {
            // Go over same process for the rest of the characters in
            // the word.
            this.insertWord(nextNode, word=word, index=index);
        } else {
            //At the last character of the word. set that word attribute
            // to true to indicate a word ends there.
            nextNode.wordEnd = true;
        }

    }

    deleteWord(currentNode, word, index=0) {
        // Get the charater and Increase the index to move to next character
        const character = word[index++];
        // Get node in the trie for that character
        const nextNode = currentNode.children.get(character);
        if (nextNode === undefined) {
            // character not in the trie so word doesn't exit.
            return false;
        } else {
            // If recursion hasnt got to end of word, continue
            // if at end of word which is a prefix of another word, then
            // mark it as no longer a word.
            if (index < word.length) {
                this.deleteWord(nextNode, word, index=index);
            } else if (index === word.length && nextNode.wordEnd) {
                nextNode.wordEnd = false;
            } else throw RangeError('No such word exist in dictionary.');
            // node count is greater than 1 when more than one word use 
            // a character represented at a node.
            // Delete node if no other word depend on it
            if (nextNode.count > 1) {
                // deduct word count
                nextNode.count -= 1;
            } else {
                currentNode.children.delete(character);
            }
            return true;
        }
    }

    search(currentNode, word, index=0, prefix=true) {
        // Get node at current character position.
        // word doesn't exist if no node is present at character position.
        currentNode = currentNode.children.get(word[index++]);
        if (currentNode === undefined) return false;

        // Go over process again with the next node until that last
        // character of word is reached.
        // If the last character of search string is a word or prefix of word
        // print true or false otherwise.
        if (index < word.length) {
            return this.search(currentNode, word, index, prefix);
        } else return prefix || currentNode.wordEnd;
    }

    word_break_search(currentNode, word, index=0) {
        // Get node for character indicated by index. Increase index by 1
        // afterwards.
        currentNode = currentNode.children.get(word[index++]);
        // Return false if node doesn't exist
        if (currentNode === undefined) return false;
        let result = false;
        // If node exists and word ends at that character, then either continue
        // search for word end from next character or start searching for a new
        // word starting from next character.
        if (currentNode.wordEnd) {
            if (index < word.length) {
                // Search word from root node after a word is found.
                let pathA = this.word_break_search(this.root, word, index);
                if (pathA) {
                    result = pathA;
                } else {
                    // continue search of longer word from current word found.
                    result = this.word_break_search(currentNode, word, index);
                }
            } else {
                result = true;
            }
        } else {
            // Return false if we get to the end of the word and it's not in our 
            // dictionary.
            if (index < word.length) {
                result = this.word_break_search(currentNode, word, index);
            } else {
                result = false;
            }
        }
        return result;
    }

    printWords(currentNode, word='') {
        // Go through each every node from root node downward
        currentNode.children.forEach((node, character) => {
            if (node.wordEnd) {
                // print word when end of character node is met
                console.log(word+character);
                // continue search if end of character node is a prefix
                // of another word.
                if (node.count > 1) {
                    this.printWords(node, word+character);
                }
            } else {// continue search until end of node is reached.
                this.printWords(node, word+character);
            }
        });
    }
}


const trie = new Trie();
const words = ['the', 'alaba', 'alabasta', 'albeit', 'alpine', 'a', 'ab', 'worse', 'always', 'allwell', 'alive', 'w'];
words.forEach((word) => {
    trie.insertWord(trie.root, word);
});

trie.printWords(trie.root);
console.log('Searching for alarm:', trie.search(trie.root, 'alarm'));
console.log('Searching for alaba:', trie.search(trie.root, 'alaba'));
console.log('Searching for alab:', trie.search(trie.root, 'alab'));
console.log('Deleting w:', trie.deleteWord(trie.root, 'w'));
console.log('Searching for deleted w:', trie.search(trie.root, 'w', prefix=false));

console.log(trie.word_break_search(trie.root, 'thealabaworse'));
console.log(trie.word_break_search(trie.root, 'alabpine'));
