from typing import Any


class Node:
    key = None
    value = None
    left_node, right_node = None, None
    count = 0

    def __init__(self, key: int = None, value: Any = None) -> None:
        self.key = key
        self.value = value
        if self.key is not None:
            self.count = 1

    def __repr__(self):
        d = {
            "key": self.key,
            "value": self.value,
            "left_node": self.left_node,
            "right_node": self.right_node,
            "count": self.count,
        }
        res = dict((k,v) for k,v in d.items() if v is not None)
        return str(res)


class BST:
    def __init__(self) -> None:
        self.root = None

    def put(self, key: int, value: Any):
        self.root = self.__put(self.root, key, value)

    def __put(self, node: Node, key: int, value: Any):
        if node is None:
            return Node(key, value)
        elif node.key > key:
            node.left_node = self.__put(node.left_node, key, value)
        elif node.key < key:
            node.right_node = self.__put(node.right_node, key, value)
        else:
            node.value = value
        node.count = 1 + self.__size(node.left_node) + self.__size(node.right_node)
        return node

    def get(self, key: int):
        return self.__get(self.root, key)

    def __get(self, node: Node, key: int):
        if node is None:
            return None
        elif node.key > key:
            return self.__get(node.left_node, key)
        elif node.key < key:
            return self.__get(node.right_node, key)
        else:
            return node.value

    def floor(self, key: int):
        node = self.__floor(self.root, key)
        if node is None:
            return None
        else:
            return node.key

    def __floor(self, node: Node, key: int) -> Node:
        if node is None:
            return None
        elif node.key == key:
            return node
        elif (node.key > key):
            return self.__floor(node.left_node, key)
        else:
            t = self.__floor(node.right_node, key)
            if t is None:
                return node
            else:
                return t

    def ceiling(self, key: int):
        node = self.__ceiling(self.root, key)
        if node is None:
            return None
        else:
            return node.key

    def __ceiling(self, node: Node, key: int):
        if node is None:
            return None
        elif node.key == key:
            return node
        elif node.key > key:
            t = self.__ceiling(node.left_node, key)
            if t is None:
                return node
            else:
                return t
        else:
            return self.__ceiling(node.right_node, key)

    def size(self):
        return self.__size(self.root)

    def __size(self, node: Node):
        if node is None:
            return 0
        else:
            return node.count

    def rank(self, key: int):
        return self.__rank(self.root, key)

    def __rank(self, node: Node, key:int):
        if node is None:
            return 0
        elif node.key > key:
            return self.__rank(node.left_node, key)
        elif node.key < key:
            return 1 + self.__size(node.left_node) + self.__rank(node.right_node, key)
        else:
            return self.__size(node.left_node)

    def inorder(self) -> list:
        queue = list()
        self.__inorder(self.root, queue)
        return queue

    def __inorder(self, node: Node, queue: list):
        if node is None:
            pass
        else:
            self.__inorder(node.left_node, queue)
            queue.append(node.key)
            self.__inorder(node.right_node, queue)

    def preorder(self):
        q = list()
        self.__preorder(self.root, q)
        return q

    def __preorder(self, node: Node, queue: list):
        if node is None:
            pass
        else:
            queue.append(node.key)
            self.__preorder(node.left_node, queue)
            self.__preorder(node.right_node, queue)

    def postorder(self):
        q = list()
        self.__postorder(self.root, q)
        return q

    def __postorder(self, node: Node, queue: list):
        if node is None:
            pass
        else:
            self.__preorder(node.left_node, queue)
            self.__preorder(node.right_node, queue)
            queue.append(node.key)



if __name__ == '__main__':
    bst = BST()
    bst.put(5, 'Hello')
    bst.put(4, 'My')
    bst.put(6, 'Dear')
    bst.put(3, 'Friend')

    print(bst.root)
    print(bst.root.left_node)
    print(bst.root.right_node)

    print(bst.get(3))
    print(bst.get(6))
    print(bst.get(4))
    print(bst.get(0))

    bst.put(3, 'who?')
    print(bst.root)
    print(bst.get(3))

    print(bst.floor(7))
    print(bst.floor(2))
    print(bst.floor(4))

    print("<==================>")

    print(bst.ceiling(1))
    print(bst.ceiling(2))
    print(bst.ceiling(4))
    print(bst.ceiling(7))

    print(bst.root)

    print(bst.rank(5))
    print(bst.rank(6))
    print(bst.rank(7))
    print(bst.rank(1))
    
    # DFS depth first search
    print(bst.inorder())
    print(bst.preorder())
    print(bst.postorder())
