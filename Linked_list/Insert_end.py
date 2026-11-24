
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)

# Insert node at end
new_node = Node(30)

temp = head
while temp.next:
    temp = temp.next

temp.next = new_node

temp = head
while temp:
    print(temp.data)
    temp = temp.next
