from typing import Any


class Node:
    key = None
    value = None
    left_node, right_node = None, None

    def __init__(self, key: int = None, value: Any = None) -> None:
        self.key = key
        self.value = value

    def __repr__(self):
        d = {
            "key": self.key,
            "value": self.value,
            "left_node": self.left_node,
            "right_node": self.right_node
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


