class Node:
    def __init__(self, value= None):
        self.value = value
        self.next = None
        return
    
    def isEmpty(self):
        if self.value==None:
            return True
        else:
            return False
    
    def append(self, v):
        if self.isEmpty():
            self.value = v
        elif self.next == None:
            self.next = Node(v)
        else:
            self.next.append(v)
        return
    
    def appendi(self,v):
        if self.isEmpty():
            self.value = v
        
        temp = self
        while temp.next != None:
            temp = temp.next

        temp.next = Node(v)
        return
    
    def insert(self, v):
        if self.isEmpty():
            self.value = v
            return 
        
        newNode = Node(v)

        (self.value, newNode.value) = (newNode.value, self.value)

        (self.next, newNode.next) = (newNode, self.next)
        return
    
    def delete(self,v):
        if self.isEmpty():
            return 
        
        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next

        else:
            if self.next!=None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None