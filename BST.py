
class Tree:
  def __init__(self, val=None):
    self.value = val
    if self.value:
      self.left=Tree()
      self.right=Tree()
    else:
      self.left = None
      self.right = None

  def is_empty(self):
    return self.value == None

  def insert(self, data):
    if self.is_empty():
      self.value = data
      self.left=Tree()
      self.right=Tree()
      return

    elif data > self.value:
      self.right.insert(data)

    elif data < self.value:
      self.left.insert(data)

    elif data == self.value:
      return

  def find(self, val):
    if self.is_empty():
      print("not found")

    elif val == self.value:
      print("found")

    elif val > self.value:
      return self.right.find(val)

    elif val < self.value:
      return self.left.find(val)

  def in_order(self):
    if self.is_empty():
      return []
    else:
      return self.left.in_order() + [self.value] + self.right.in_order()

t=Tree(10)
t.insert(5)
t.insert(15)  
t.insert(3)
t.insert(7)
t.insert(12)
t.insert(18)
t.insert(4)

t.find(18)
print(t.in_order())