class Solution:
    # Example room structure:
    # [[1],[2],[3],[]]
    # Meaning:
    # Room 0 → key to room 1
    # Room 1 → key to room 2
    # Room 2 → key to room 3
    # Room 3 → no keys

    visited = [0, 3, 1]  # Example initialization
    stack = []

    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        stack = [0]  # start from room 0
        while stack:
            room = stack.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        return len(visited) == len(rooms)