
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node

        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def del_node(self, rt, val):
        if rt is None:
            return rt

        if val < rt.data:
            rt.left = self.del_node(rt.left, val)

        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)

        else:
            if rt.left is None:
                return rt.right

            elif rt.right is None:
                return rt.left

            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt

    def get_successor(self, temp):
        temp = temp.right

        while temp.left is not None:
            temp = temp.left

        return temp

    def inorder(self, rt):
        if rt is None:
            return

        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def count_leaf(self, rt):
        if rt is None:
            return 0

        if rt.left is None and rt.right is None:
            return 1

        return self.count_leaf(rt.left) + self.count_leaf(rt.right)

    def preorder(self, rt):
        if rt is None:
            return

        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return

        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    def search(self, key):
        temp = self.root

        while temp:
            if temp.data == key:
                return True

            elif key < temp.data:
                temp = temp.left

            else:
                temp = temp.right

        return False

    def findminmax(self, rt):
        if rt is None:
            print("Tree is empty")
            return

        temp = rt

        while temp.left:
            temp = temp.left

        print("\nMin:", temp.data)

        temp = rt

        while temp.right:
            temp = temp.right

        print("Max:", temp.data)


b1 = BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
b1.insert(Node(50))

print("Inorder:")
b1.inorder(b1.root)

print("\nLeaf nodes:", b1.count_leaf(b1.root))

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

b1.findminmax(b1.root)

if b1.search(50):
    print("\nFound the node")
else:
    print("\nNot found")
