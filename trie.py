"""
自动补全，输入是个前缀字符串，另一个输入是个一堆单词。

所以思路就非常简单，用个trie就行。用前缀找到子树，然后DFS一遍把所有的单词输出即可。
"""
class TrieNode:
    # we will build a prefix tree and use * to track the word
    def __init__(self):
        self.root = {"*": "*"}

    def insert(self, word):
        # insert the word
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            # point to the next node
            cur = cur[letter]
        # we need to keep track of the end of the word
        cur["*"] = "*"

    def find_start(self, pre):
        # output should be a dic for the starting points of dfs
        cur = self.root
        for letter in pre:
            if letter not in cur:
                return None
            cur = cur[letter]
        return cur
if __name__ == "__main__":
    input = ["ab", "a", "de", "abde"]
    pre = "ab"
    trie = TrieNode()
    for i in input:
        trie.insert(i)
    start = trie.find_start(pre)
    # res => to store the result
    res = []
    # dfs
    def dfs(node, s):
        # we reach the leaves
        if not node:
            return
        for key, val in node.items():
            # we found a word
            if key == "*":
                res.append(pre + s)
                continue
            dfs(val, s + key)
        return
    dfs(start, "")
    print(res)


