# Implementation of Stack using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push element into stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    # Pop element from stack
    def pop(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            removed = self.top.data
            self.top = self.top.next
            print("Removed:", removed)

    # Peek top element
    def peek(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print("Top Element:", self.top.data)

    # Display stack elements
    def display(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            temp = self.top

            while temp:
                print(temp.data)
                temp = temp.next


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.peek()

s.pop()

s.display()