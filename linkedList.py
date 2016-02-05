class Node(object):
 
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

class linked_list(object):

  def __init__(self,head=None,tail=None):
    self.head = head
    self.tail = tail

  def push_back(self,data):
    newNode = Node(data)
    
    # If the list is empty, make newNode the head
    if self.head == None:
      self.head = newNode

    # If there is a tail, make it point to newNode,
    # and make newNode the new tail
    if self.tail != None:
      self.tail.nextNode = newNode
    self.tail = newNode

  def push_front(self,data):
    newNode = Node(data,self.head)
    self.head = newNode

    # If the list is empty, make newNode the tail
    if self.tail == None:
      self.tail = newNode

  def pop_back(self):
    if self.empty():
      raise RuntimeError
    # find the node that points to the tail
    # make this node the tail, and make the new tail.nextNode = None 
    node = self.head
    while node != None:
      if node == self.tail:
        returnData = node.data
        self.head = None
        self.tail = None
        return returnData
      if node.nextNode == self.tail:
        returnData = self.tail.data
        self.tail = node
        self.tail.nextNode = None
        return returnData
      node = node.nextNode

  def pop_front(self):
    if self.empty():
      raise RuntimeError
    prevHead = self.head
    self.head = prevHead.nextNode
    return prevHead.data

  def empty(self):
    return self.size() == 0

  def size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.nextNode
    return count

  def PrintList( self ):
    node = self.head
    while node != None:
      print node.data
      node = node.nextNode  
