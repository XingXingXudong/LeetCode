# coding: utf-8
from collections import deque


# Defintion for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __str__(self):
        neighbor_labels = [str(x.label) for x in self.neighbors]
        return "<label: {}, neighbos=[{}]>".format(str(self.label), ", ".join(neighbor_labels))

    __repr__ = __str__

def print_graph(node):
    """BFS print the graph"""
    node_set = set()
    queue = deque([(node, 0)])
    while queue:
        n, i = queue.popleft()
        print("--" * i, n)
        for new_node in n.neighbors:
            if new_node in node_set:
                continue
            queue.append((new_node, i+1))
            node_set.add(new_node)


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node):
        if not node:
            return
        copy_node = UndirectedGraphNode(node.label)
        dic = {node: copy_node}
        self.dfs(node, dic)
        return copy_node

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                copy_neighbor = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = copy_neighbor
                dic[node].neighbors.append(copy_neighbor)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])

    def bfs_clone_graph(self, node):
        """Clone graph use BFS"""
        cg = UndirectedGraphNode(node.label)
        copy_map = {node: cg}
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for nb in cur.neighbors:
                if nb not in copy_map:
                    queue.append(nb)
                    copy_nb = UndirectedGraphNode(nb.label)
                    copy_map[nb] = copy_nb
                    copy_map[cur].neighbors.append(copy_nb)
                else:
                    copy_map[cur].neighbors.append(copy_map[nb])
        return cg

    def recursive_clone_graph(self, node):
        """Clone graph use Recursive"""
        if not node:
            return 
        copy_node = None
        curr = node

        copy_node = UndirectedGraphNode(curr.label)

        self.visited[copy_node.label] = copy_node

        for neighbor in curr.neighbors:
            if neighbor.label not in self.visited:
                copy_node.neighbors.append(self.recursive_clone_graph(neighbor))
            else:
                copy_node.neighbors.append(self.visited[neighbor.label])
        return copy_node


    def dfs_clone_graph(self, node):
        """Clone graph use DFS"""

        if not node:
            return 

        stack = []
        node_set = {}

        copy_node = UndirectedGraphNode(node.label)
        node_set[node] = copy_node
        stack.append(node)

        while stack:
            cur_node = stack.pop()
            for n in cur_node.neighbors:
                if n not in node_set:
                    n_copy = UndirectedGraphNode(n.label)
                    node_set[n] = n_copy
                    node_set[cur_node].neighbors.append(n_copy)
                    stack.append(n)
                else:
                    node_set[cur_node].neighbors.append(node_set[n])

        return copy_node


if __name__ == '__main__':
    node_7 = UndirectedGraphNode(7)
    node_6 = UndirectedGraphNode(6)
    node_6.neighbors.append(node_7)
    node_3 = UndirectedGraphNode(3)
    node_3.neighbors.append(node_6)
    node_4 = UndirectedGraphNode(4)
    node_4.neighbors.append(node_6)
    node_5 = UndirectedGraphNode(5)
    node_5.neighbors.append(node_5)
    node_1 = UndirectedGraphNode(1)
    node_2 = UndirectedGraphNode(2)
    node_2.neighbors.append(node_3)
    node_2.neighbors.append(node_4)
    node_2.neighbors.append(node_5)
    node_0 = UndirectedGraphNode(0)
    node_0.neighbors.append(node_1)
    node_0.neighbors.append(node_2)

    print_graph(node_0)

    copy_graph = Solution()

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print_graph(copy_graph.cloneGraph(node_0))

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print_graph(copy_graph.bfs_clone_graph(node_0))

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print_graph(copy_graph.recursive_clone_graph(node_0))

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print_graph(copy_graph.dfs_clone_graph(node_0))



