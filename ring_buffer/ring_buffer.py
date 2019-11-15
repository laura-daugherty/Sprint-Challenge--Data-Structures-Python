class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage.append(item)
    self.current += 1
    if self.current == self.capacity:
      self.storage.pop()
      self.current -= 1

  def get(self):
    return self.current