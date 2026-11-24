
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Linking nodes
n1.next = n2
n2.next = n3

# Display linked list
temp = n1

while temp:
    print(temp.data)
    temp = temp.next
