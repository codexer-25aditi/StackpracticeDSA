#Stack manipulation using Linked List
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def __str__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next

class Stacks:
    def __init__(self):
        self.LinkedList=LinkedList()  # here stack is being created using LL

    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False
    def push(self,value):
        node=Node(value)
        node.next=self.LinkedList.head
        self.LinkedList.head=node
        return "The value had been inserted"
    def pop(self):
        if self.isEmpty():
            return "The list is empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
    def peek(self):
        if self.isEmpty():
            return "The List is empty"
        else:
            nodeValue=self.LinkedList.head.value
            return nodeValue
    def deletes(self):
        self.LinkedList.head.value=None
        return "The list is successfully deleted"







customStack=Stacks()
print(customStack.isEmpty())
print(customStack.push(11))
customStack.push(12)
customStack.push(13)
customStack.push(14)
customStack.push(15)
print(customStack)
print("---------------------")
print(customStack.pop())
print("---------------")
print(customStack.deletes())
print(customStack.peek())
print("-------------------")

