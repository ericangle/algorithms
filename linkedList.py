class Node(object):
 
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
      return str(self.data)       
    

class linked_list(object):

  def __init__(self,head=None,tail=None):
    self.head = head
    self.tail = tail

  def push_back(self,data):
    newNode = Node(data)
    
    if self.empty():
      self.head = newNode
    else:
      self.tail.nextNode = newNode

    self.tail = newNode

  def push_front(self,data):
    wasEmpty = self.empty()

    newNode = Node(data,self.head)
    self.head = newNode

    if wasEmpty:
      self.tail = newNode

  def pop_back(self):
    if self.empty():
      raise RuntimeError

    prevTail = self.tail

    if self.oneNode():
      self.makeEmpty()
    else:
      # find the node that points to the tail
      # make this node the tail, and make the new tail.nextNode = None 
      node = self.head
      while node:
        if node.nextNode == self.tail:
          self.tail = node
          self.tail.nextNode = None
          break
        node = node.nextNode

    return prevTail.data

  def pop_front(self):
    if self.empty():
      raise RuntimeError

    prevHead = self.head

    if self.oneNode():
      self.makeEmpty() 
    else: 
      self.head = prevHead.nextNode

    return prevHead.data

  def oneNode(self):
    return self.head == self.tail and self.head != None

  def makeEmpty(self):
    self.head = self.tail = None

  def empty(self):
    return self.head == None and self.tail == None

  def __len__(self):
    currentNode = self.head
    numNodes = 0
    while currentNode:
      numNodes += 1
      currentNode = currentNode.nextNode
    return numNodes

  def __str__(self):
    contents = ""
    node = self.head
    while node != None:
      contents += str(node.data) + ","
      node = node.nextNode
    contents = contents[:len(contents)-1]
    return "[" + contents + "]"

  def __iter__(self):
    self.start = self.head
    self.end = self.tail
    return self

  def next(self): # in python 3, __next__
    a = self.start
    if a == None:
      raise StopIteration
    self.start = a.nextNode
    return a
