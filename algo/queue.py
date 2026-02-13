
class Node:
    value = None
    next = None

    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def peek(self):
        return self.head.value
    
    def dequeue(self):
        if(not self.head): return None

        head = self.head
        self.head = head.next
        self.length -= 1

        #free memory
        head.next = None


        return head.value
    
    def enqueue(self, value):
        node = Node(value)
        if(self.length == 0):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length+=1


    def print_queue(self):

        curr = self.head

        while(curr):
            print(curr.value)
            curr = curr.next


queue =  Queue()
queue.enqueue(1)
queue.enqueue(7)
queue.enqueue(30)
queue.enqueue(11)
queue.enqueue(17)
queue.enqueue(310)

queue.dequeue()

queue.print_queue()



    

    



