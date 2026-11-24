
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(20)
head.next = Node(30)

# Insert new node at beginning
new_node = Node(10)
new_node.next = head
head = new_node

temp = head
while temp:
    print(temp.data)
    temp = temp.next
