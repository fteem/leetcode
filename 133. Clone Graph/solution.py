class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


def clone_graph_bfs(self, node):
    if not node:
        return

    root = UndirectedGraphNode(node.label)
    stack = [node]
    visited = {node.label: root}

    while stack:
        n = stack.pop()
        for neighbor in n.neighbors:
            if neighbor.label not in visited:
                stack.append(neighbor)
                visited[neighbor.label] = UndirectedGraphNode(neighbor.label)
            visited[n.label].neighbors.append(visited[neighbor.label])

    return root


def clone_graph_dfs(self, node):
    if not node:
        return

    visited = {}

    def clone_node(node):
        if not node:
            return
        if node.label in visited:
            return visited[node.label]
        clone = UndirectedGraphNode(node.label)
        visited[node.label] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(visited.get(neighbor.label, clone_node(neighbor)))
        return clone
    return clone_node(node)



if __name__ == '__main__':
    node0 = UndirectedGraphNode(0)
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node0.neighbors = [node1, node2]
    node1.neighbors = [node0, node2]
    node2.neighbors = [node2]

    clone_graph_bfs(node0)
    clone_graph_dfs(node0)