from collections.abc import MutableMapping

#? Is MutableMapping Needed? Not sure if it has any use in this case.
class Distances(MutableMapping):
    def __init__(self, root):
        self.root = root
        self.store = dict()
        self.store[root] = 0

    def __getitem__(self, key):
        return self.store[self._keytransform(key)]

    def __setitem__(self, key, value):
        self.store[self._keytransform(key)] = value

    def __delitem__(self, key):
        del self.store[self._keytransform(key)]

    def __iter__(self):
        return iter(self.store)
    
    def __len__(self):
        return len(self.store)

    def _keytransform(self, key):
        return key

    def get_cells(self):
        return list(self.cells.keys())
    
    def path_to(self, goal):
        current = goal

        breadcrumbs = Distances(self.root)
        breadcrumbs[current] = self.store[current]
        while current != self.root:
            for neighbor in current.get_links():
                if self.store[neighbor] < self.store[current]:
                    breadcrumbs[neighbor] = self.store[neighbor]
                    current = neighbor
                    break
        return breadcrumbs
    
    def max(self):
        max_distance = 0
        max_cell = self.root
        
        for cell, distance in self.store.items():
            if distance > max_distance:
                max_distance = distance
                max_cell = cell
        return (max_cell, max_distance)
    
