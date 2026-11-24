
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Delete last node
temp = head

while temp.next.next:
    temp = temp.next

temp.next = None

while head:
    print(head.data)
    head = head.next
