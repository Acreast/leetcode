// Last updated: 4/23/2026, 1:24:17 AM
1class Solution {
2    
3    // ---------- TrieNode: one node of the prefix tree ----------
4    class TrieNode {
5        TrieNode[] children; // 26 slots for 'a' to 'z'
6        boolean isEnd; // true if this node marks the end of a dictionary word
7        
8        TrieNode() {
9            children = new TrieNode[26];
10            isEnd = false;
11        }
12    }
13    
14    // ---------- Trie: builds the dictionary as a tree ----------
15    class Trie {
16        private TrieNode root;
17        
18        // Constructor: insert all dictionary words
19        public Trie(String[] words) {
20            root = new TrieNode();
21            for (String word : words) {
22                insert(word);
23            }
24        }
25        
26        // Insert a single word into the trie
27        public void insert(String word) {
28            TrieNode node = root;
29            for (char c : word.toCharArray()) {
30                int index = c - 'a'; // 0 for 'a', 1 for 'b', ...
31                if (node.children[index] == null) {
32                    node.children[index] = new TrieNode();
33                }
34                node = node.children[index];
35            }
36            node.isEnd = true; // mark the end of the word
37        }
38        
39        // Return the root node so we can start traversal from outside
40        public TrieNode getRoot() {
41            return root;
42        }
43    }
44    
45    // ---------- Main method: find all queries that match within 2 edits ----------
46    public List<String> twoEditWords(String[] queries, String[] dictionary) {
47        List<String> res = new ArrayList<>();
48        
49        // Build a trie from the dictionary
50        Trie trie = new Trie(dictionary);
51        TrieNode root = trie.getRoot();
52        
53        // Check each query word individually
54        for (String query : queries) {
55            if (dfs(root, query, 0, 0)) { // start at root, position 0, 0 edits used
56                res.add(query);
57            }
58        }
59        
60        return res;
61    }
62    
63    // ---------- DFS that allows at most 2 edits ----------
64    // node: current trie node
65    // query: the word we are trying to match
66    // pos: current character index in query (0..len-1)
67    // editsUsed: how many replacements have been made so far
68    private boolean dfs(TrieNode node, String query, int pos, int editsUsed) {
69        // If we already exceeded the allowed number of edits, stop this path
70        if (editsUsed > 2) {
71            return false;
72        }
73        
74        // If we have processed all characters of the query,
75        // then we succeed only if the current trie node represents a complete dictionary word.
76        if (pos == query.length()) {
77            return node.isEnd;
78        }
79        
80        char currChar = query.charAt(pos);
81        int index = currChar - 'a';
82        
83        // ---------- Option 1: exact match (no extra edit) ----------
84        // Move to the child that corresponds to the same letter.
85        if (node.children[index] != null) {
86            if (dfs(node.children[index], query, pos + 1, editsUsed)) {
87                return true; // found a matching path
88            }
89        }
90        
91        // ---------- Option 2: replace current letter with any other letter (1 edit) ----------
92        // Try every possible letter that is different from the original.
93        for (int i = 0; i < 26; i++) {
94            if (i != index && node.children[i] != null) {
95                // We use one more edit (editsUsed + 1) and move to that child
96                if (dfs(node.children[i], query, pos + 1, editsUsed + 1)) {
97                    return true;
98                }
99            }
100        }
101        
102        // No path succeeded → this query cannot match any dictionary word within 2 edits
103        return false;
104    }
105}