from doubly_linked_list import ListNode, DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
      if self.storage.length == 0:
        self.current = item


      if self.storage.length == self.capacity:

        print("at capacity, need to swap out oldest")
        print("current is:", self.current)

        dll = DoublyLinkedList()
        
        boole = False
        while self.storage.head is not None:
          node = self.storage.remove_from_head()

          if boole:
            boole = False
            self.current = node
            print("  last loop we replaced, new current is:", self.current)
            dll.add_to_tail(node)
          elif node == self.current:
            print("replacing oldest with item:", self.current, item)
            boole = True
            dll.add_to_tail(item)
          else:
            dll.add_to_tail(node)
        if boole is True:
          print("something broke")
          node = dll.remove_from_head()
          print("node", node)

          self.current = node
          dll.add_to_head(node)
        self.storage = dll
        print("all done, new current is:", self.current)

        
      else:
        self.storage.add_to_tail(item)



      #if self.capacity == capactiy:
        #remove from tail
        #add item to head
      #else:
        #add item to head

    def get(self):
      #While items:
        #if item is not None:
          # remove from head
          # add to list_buffer_contents
          # remove from size
          # move_to_front(next)
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        while self.storage.length != 0:
          if self.current is not None:
            oldhead = self.storage.remove_from_head()
            print("old head", oldhead)
            if oldhead is not None:
              list_buffer_contents.append(oldhead)
        for item in list_buffer_contents:
          self.storage.add_to_tail(item)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass