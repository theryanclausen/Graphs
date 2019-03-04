"""
Simple graph implementation
"""
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError('That vertex does not exist')
    def bft(self, starting_vertex_id):
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex_id)
        while q.size() > 0:
            current = q.dequeue()
            if current not in visited:
                print('bft',current)
                visited.add(current)
                for neighbor in self.vertices[current]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex_id):
        s = Stack()
        visited = set()
        s.push(starting_vertex_id)
        while s.size() > 0:
            current = s.pop()
            if current not in visited:
                print('dft', current)
                visited.add(current)
                for neighbor in self.vertices[current]:
                    s.push(neighbor)
    
    def rdft(self, starting_vertex_id, visited=set()):
        if starting_vertex_id in visited:
            return
        visited.add(starting_vertex_id)
        for neighbor in self.vertices[starting_vertex_id]:
            self.rdft(neighbor, visited)

    def bfs(self, starting_vertex_id, target):
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex_id)
        while q.size() > 0:
            current = q.dequeue()
            if current == target:
                return True
            if current not in visited:
                visited.add(current)
                for neighbor in self.vertices[current]:
                    q.enqueue(neighbor)
        return False

    def dfs(self, starting_vertex_id, target):
        s = Stack()
        visited = set()
        s.push(starting_vertex_id)
        while s.size() > 0:
            current = s.pop()
            if current == target:
                return True
            if current not in visited:
                visited.add(current)
                for neighbor in self.vertices[current]:
                    s.push(neighbor)
        return False

graph = Graph()  # Instantiate your graph
graph.add_vertex('2')
graph.add_vertex('1')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_edge('5', '3')
graph.add_edge('6', '3')
graph.add_edge('7', '1')
graph.add_edge('4', '7')
graph.add_edge('1', '2')
graph.add_edge('7', '6')
graph.add_edge('2', '4')
graph.add_edge('3', '5')
graph.add_edge('2', '3')
graph.add_edge('4', '6')

# graph.rdft('1')
# print(graph.dfs('1','79'))