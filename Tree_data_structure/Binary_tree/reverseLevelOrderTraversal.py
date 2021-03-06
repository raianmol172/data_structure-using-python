from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def reverseLevelOrder(root):
    if root is None:
        return None
    else:
        q = deque()
        s = deque()
        q.append(root)

        while len(q):
            temp = q.popleft()
            s.append(temp)
            if temp.right:
                q.append(temp.right)
            if temp.left:
                q.append(temp.left)

        while len(s):
            temp = s.pop()
            print(temp.data, end=' ')


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
print('reverse level order traversal:')
reverseLevelOrder(tree)
