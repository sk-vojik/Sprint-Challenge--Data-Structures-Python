class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    #check to see if current amount is within capacity. if it is, append, and up current amount
    if self.current < self.capacity - 1:
      self.current += 1
    #if we're at capacity, reset current to 0, and next appended value will override oldest item
    else:
      self.current = 0

  def get(self):
    return [item for item in self.storage if item != None]
 