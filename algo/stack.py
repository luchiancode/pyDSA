
class Node:
    value = None
    next = None

    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        

class Stack:
    def __init__(self):
        self.length = 0
        self.head = None

    def peek(self):
        return self.head.value
    
    def pop(self):
        if(not self.head): return None

        curr = self.head

        while(True):
            if(curr.next.next == None):
                curr.next = None
                break
            else:
                curr = curr.next


        return True
    
    def push(self, value):
        node = Node(value)
        if(self.length == 0):
            self.head = node
        else:
            curr = self.head
            while(True):
                if(curr.next == None):
                    curr.next = node
                    break
                else:
                    curr = curr.next
         
        self.length+=1


    def print_stack(self):

        curr = self.head

        while(curr):
            print(curr.value)
            curr = curr.next


stack = Stack()
stack.push(1)
stack.push(7)
stack.push(30)
stack.push(11)
stack.push(17)
stack.push(310)
stack.pop()
stack.push(130)


stack.print_stack()



    

    



