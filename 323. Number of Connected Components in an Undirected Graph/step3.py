class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = [[] for _ in range(n)]
        for node_a, node_b in edges:
            adjacency_list[node_a].append(node_b)
            adjacency_list[node_b].append(node_a)

        def traverse(node_id):
            visited[node_id] = True
            next_nodes = [node_id]
            while next_nodes:
                node = next_nodes.pop()
                for neighbor in adjacency_list[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        next_nodes.append(neighbor)

        visited = [False] * n
        num_connected_components = 0
        for node_id in range(n):
            if visited[node_id]:
                continue

            num_connected_components += 1
            traverse(node_id)

        return num_connected_components
