
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

search = 20
temp = head
found = False

while temp:
    if temp.data == search:
        found = True
        break
    temp = temp.next

if found:
    print("Element found")
else:
    print("Element not found")
