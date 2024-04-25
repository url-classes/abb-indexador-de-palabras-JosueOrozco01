from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.left: Node[T] | None = None
        self.right: Node[T] | None = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree(Generic[T]):

    def __init__(self):
        self.__root: Node | None = None

    def __insert(self, data: T, subtree: Node[T] | None) -> Node[T]:
        if subtree is None:
            return Node(data)
        else:
            if data < subtree.data:
                subtree.left = self.__insert(data, subtree.left)
                print(f"Insertar '{data}' a la izquierda de '{subtree.data}'")
            elif data > subtree.data:
                subtree.right = self.__insert(data, subtree.right)
                print(f"Insertar '{data}' a la derecha de '{subtree.data}'")
        return subtree

    def insert(self, data: T):
        words = sorted(data.split())
        for i, word in enumerate(words):
            if i == 0:
                self.__root = self.__insert(word, self.__root)
                print(f"Raíz: {word}")
            elif word < self.__root.data:
                self.__insert(word, self.__root)
            else:
                self.__insert(word, self.__root)

    def __inorder_traversal(self, subtree: Node | None) -> list[T]:
        if subtree is None:
            return []
        else:
            return self.__inorder_traversal(subtree.left) + [subtree.data] + self.__inorder_traversal(subtree.right)

    def inorder_traversal(self) -> list[T]:
        return self.__inorder_traversal(self.__root)


# Ejemplo de uso
sentence = "El arbol esta bonito"
bst = BinarySearchTree()
bst.insert(sentence)
sorted_sentence = bst.inorder_traversal()
print(sorted_sentence)
