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



def fn(root):
    if not root:
        return []

    order = list()
    stack = list()

    stack.append(root)

    while stack:
        root = stack[-1]
        stack.pop()

        order.append(root.value)

        if root.right != None:
            stack.append(root.right)
        if root.left != None:
            stack.append(root.left)

    return order