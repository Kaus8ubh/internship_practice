
class Custom_Dict:
  def __init__(self):
      self.keys = []  
      self.values = [] 

  def add(self, key):
      if key in self.keys:
          index = self.keys.index(key)
          self.values[index] += 1  
      else:
          self.keys.append(key)
          self.values.append(1) 

  def count_frequency(self, words):
      for word in words:
          self.add(word)

  def display(self):
      for key, value in zip(self.keys, self.values):
          print(f"{key}: {value}")

#usage
words = ["mobile", "bag", "car", "house", "mobile", "bag"]
word_counter = Custom_Dict()
word_counter.count_frequency(words)
word_counter.display()  
