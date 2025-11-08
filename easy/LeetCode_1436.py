#TODO You are given the array paths, where paths[i] = [cityAi, cityBi]
# means there exists a direct path going from cityAi to cityBi.
# Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop,
# therefore, there will be exactly one destination city.
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = {a for a, b in paths }
        for a, b in paths:
            if b not in start:
                return b
        return None


s = Solution()

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

result = s.destCity(paths)

print(result)