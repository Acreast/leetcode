# Last updated: 7/12/2025, 11:52:05 PM
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: Build the graph using adjacency list representation
        graph = defaultdict(list)
        for from_node, to_node in edges:
            graph[to_node].append(from_node)  # Reverse the edge direction
        
        # Step 2: Function to perform DFS and collect ancestors
        def dfs(node):
            if node in ancestors:
                return ancestors[node]
            
            ancestors[node] = set()
            for parent in graph[node]:
                ancestors[node].add(parent)
                ancestors[node].update(dfs(parent))
            
            return ancestors[node]
        
        # Step 3: Collect ancestors for each node using DFS
        ancestors = {}
        for i in range(n):
            dfs(i)
        
        # Step 4: Sort and format the output as required
        answer = [[] for _ in range(n)]
        for node, anc_set in ancestors.items():
            answer[node] = sorted(list(anc_set))
        
        return answer
            
        