# BST using Linked List

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insertion
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

    # Inorder Traversal (Left, Root, Right)
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    # Level Order Traversal
    def level_order(self, rt):
        if rt is None:
            print("BST is empty")
            return

        arr = []
        cnt = 0
        level = 0

        arr.append(rt)

        while cnt < len(arr):
            node_count = len(arr) - cnt  # Level wise node count

            print("Level", level, ":", end=" ")

            for i in range(node_count):
                temp = arr[cnt]
                cnt += 1       # no. of nodes visited

                print(temp.data, end=" ")

                if temp.left:
                    arr.append(temp.left)

                if temp.right:
                    arr.append(temp.right)

            print()
            level += 1

    # Preorder Traversal (Root, Left, Right)
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    # Postorder Traversal (Left, Right, Root)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    # Find Minimum and Maximum
    def findminmax(self):
        if self.root is None:
            print("BST is empty")
            return

        temp = self.root

        while temp.left:
            temp = temp.left

        print("\nMin: ", temp.data)

        temp = self.root

        while temp.right:
            temp = temp.right

        print("Max: ", temp.data)

    # Count Total Number of Nodes
    def cnt(self, rt):
        if rt is None:
            return 0
        else:
            return 1 + self.cnt(rt.left) + self.cnt(rt.right)

    # Count Leaf Nodes
    def leaf(self, rt):
        if rt is None:
            return 0
        elif rt.left is None and rt.right is None:
            return 1
        else:
            return self.leaf(rt.left) + self.leaf(rt.right)


# Main Program
b1 = BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(40))

print("\nInorder:")
b1.inorder(b1.root)

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

print("\nLevel Order:")
b1.level_order(b1.root)

print("\nTotal No. of Nodes:", b1.cnt(b1.root))

print("Total Leaf Nodes:", b1.leaf(b1.root))

b1.findminmax()
