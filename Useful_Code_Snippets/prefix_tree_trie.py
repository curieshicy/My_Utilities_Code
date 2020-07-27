class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True
                
    def check_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word
        
    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
            
    def words_with_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
            
        return self.dfs(prefix, node, [])
        
    def dfs(self, prefix_word, tree_node, res):
        if tree_node.is_word:
            res.append(prefix_word)
            
        for ch in tree_node.children:
            self.dfs(prefix_word + ch, tree_node.children[ch], res)
            
        return res
            
            
use = Trie()
words = ['abc', 'abd', 'abe', 'amf']
for word in words:
    use.insert_word(word)

print (use.check_word('abcd'))
print (use.starts_with('am'))
print (use.words_with_prefix('a'))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
