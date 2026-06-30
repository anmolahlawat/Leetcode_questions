class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = {}

        for row in wall:
            position = 0

            # Ignore the last brick (right boundary)
            for i in range(len(row) - 1):
                position += row[i]
                edge_count[position] = edge_count.get(position, 0) + 1

        max_edges = 0
        for count in edge_count.values():
            max_edges = max(max_edges, count)

        return len(wall) - max_edges