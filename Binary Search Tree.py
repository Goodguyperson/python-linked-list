import random

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__ (self):
        self.root = None

    # Finds whether an element is within the tree
    def search (self, root, key):
        if root is None:
            return False

        if root.value == key:
            return True

        if root.value <= key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)


    # Insert an element into bst recursively
    def insert (self, root, value):
        if root is None:
           root = TreeNode(value)
        else:
            if root.value <= value:
                root.right = self.insert(root.right, value)
            else:
                root.left = self.insert(root.left, value)
        return root


    # Deletes an element within bst
    def delete (self, root, val):
        if root is None:
            return root

        if root.value < val:
            root.right = self.delete(root.right, val)
        elif root.value > val:
            root.left = self. delete(root.left, val)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            else:
                temp = root.right
                while temp.left is not None:
                    temp = temp.left

                root.value = temp.value
                root.right = self.delete(root.right, temp.value)

    # Print bst in order
    def inorderPrint (self, root):
        if root is not None:
            self.inorderPrint(root.left)
            print(root.value)
            self.inorderPrint(root.right)

if __name__ == '__main__':
    tree = BinarySearchTree()
    root = None

    root = tree.insert(root, 10)
    root = tree.insert(root, 20)
    root = tree.insert(root, 5)
    root = tree.insert(root, 11)


    tree.inorderPrint(root)
    tree.delete(root, root.value)
    tree.inorderPrint(root)


