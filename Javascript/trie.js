class TrieNode {
    constructor() {
        this.children = new Map();
        this.word = false;
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
        const nextNode = currentNode.children.get(character);
        if (nextNode === undefined) {
            nextNode = currentNode.children.set(character, 
                new TrieNode()).get(character);
        }
        nextNode.count += 1;
        index += 1;

        if (index < len(word)) {
            this.insertWord(nextNode, word=word, index=index);
        } else {
            nextNode.word = true;
        }

    }

    deleteWord(currentNode, word, index=0) {
        // Get the charater
        const character = word[index];
        // Get node in the trie for that character
        const nextNode = currentNode.children.get(character);
        if (nextNode === undefined) {
            // character not in the trie so word doesn't exit.
            return false;
        } else {
            // Increase the index to move to next character
            index += 1;
            // If recursion hasnt got to end of word, continue
            // if at end of word which is a prefix of another word, then
            // mark it as no longer a word.
            if (index < word.length) {
                this.deleteWord(nextNode, word, index=index);
            } else if (index === word.length && nextNode.word) {
                nextNode.word = false;
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
        currentNode = currentNode.children.get(word[index]);
        if (currentNode === undefined) return false;
        index += 1;

        if (index < word.length) {
            return this.search(currentNode, word, index, prefix);
        } else return prefix || currentNode.word;
    }
}
