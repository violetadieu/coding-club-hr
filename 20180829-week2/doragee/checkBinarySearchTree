class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      
  def getData(self):
    return self.data

  def getLeft(self):
    return self.left
    
  def setLeft(self, node):
    self.left = node
    
  def getRight(self):
    return self.right
    
  def setRight(self, node):
    self.right = node
    
root = node(3)

node1 = node(5)
node2 = node(2)
root.setLeft(node1)
root.setRight(node2)

node3 = node(1)
node4 = node(4)
node1.setLeft(node3)
node1.setRight(node4)

node5 = node(6)
node2.setLeft(node5)

if __name__ == '__main__':
  
  print(root.getLeft().getData())
