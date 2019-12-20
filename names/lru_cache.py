from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]

        else:
            return None


        # if key not in self.dict:
        #     return None
        # else:
        #     node = self.dict[key]
        #     print('__________________', node)
        #     self.dll.move_to_end(node)
        #     print("node.value", node.value[1])
        #     return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        # check to see if key in the cache
        # if it is in the cache:
            #move to front
            #update value

        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return
            
        # check the length
        # if at limit
            #delete last
        if self.current == self.limit:
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()
            self.current -= 1

        #if not in the cache:
            # add to front of cache
        #defining tail as most recent and head as oldest
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.current += 1






    # Laura's solution

    # def set(self, key, value):
    #     if self.current == self.limit:
    #         my_pair = (key, value)
    #         my_node = ListNode(my_pair)
    #         #remove oldest entry
    #         print("if value", my_pair)
    #         del self.dict[self.dll.head]
    #         self.dll.remove_from_head()
    #         #add entry to newest spot
    #         self.dll.add_to_tail(my_node)
    #     if key in self.dict:
    #         my_pair = (key, value)
    #         my_node = ListNode(my_pair)            
    #         print("2 if value", my_pair)
    #         self.dll.move_to_end(my_node)
    #         self.dict.update(my_node)
    #     else:
    #         my_pair = (key, value)
    #         my_node = ListNode(my_pair)            
    #         print("else value", my_pair)
    #         self.dict[key] = my_node
    #         self.current += 1
    #         self.dll.add_to_tail(my_node)


