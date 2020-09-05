import sys

input=sys.stdin.readline

class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value=value
        self.pointer=pointer

class LinkedQueue(object):
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def isEmpty(self):
        return not bool(self.head)

    def dequeue(self):
        if not self.head:
            return -1
            # Queue empty
        elif self.head:
            value=self.head.value
            self.head=self.head.pointer
            self.count -= 1
            return value

    def enqueue(self,value):
        node = Node(value)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            if self.tail:
                self.tail.pointer=node
            self.tail=node
        self.count += 1

    def size(self):
        return self.count

    def peek(self):
        return self.head.value

    def back(self):
        return self.tail.value

    def print(self):
        node=self.head
        while node:
            print(node.value, end=" ")
            node=node.pointer
        print()

if __name__=="__main__":
    queue=LinkedQueue()
    num=int(input())
    for i in range(num):
        order=input().split()

        if order[0]=='push':
            queue.enqueue(int(order[1]))
        elif order[0]=='front':
            print(queue.peek())
        elif order[0]=='back':
            print(queue.back())
        elif order[0]=='size':
            print(queue.size())
        elif order[0]=='empty':
            if not queue.isEmpty():
                print(0)
            else:
                print(1)
        elif order[0]=='pop':
            print(queue.dequeue())