from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


def level(root):
    if not root:
        return []

    queue = deque([root])
    levels = []

    while queue:
        size = len(queue)
        current_level = []

        for i in range(size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        levels.append(current_level)

    return levels