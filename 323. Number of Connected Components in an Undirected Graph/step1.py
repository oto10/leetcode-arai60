class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for node_a, node_b in edges:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        num_connected_components = 0
        visited = [False] * n
        for node_id in range(n):
            if visited[node_id]:
                continue

            num_connected_components += 1
            next_nodes = [node_id]
            visited[node_id] = True

            while next_nodes:
                node = next_nodes.pop()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        next_nodes.append(neighbor)

        return num_connected_components
