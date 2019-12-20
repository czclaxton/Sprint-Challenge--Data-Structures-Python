from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()
        self.overwritten = 0

    def append(self, item):
        current_node = self.storage.head

        if self.current < self.capacity:
            self.storage.add_to_tail(item)
            self.current += 1
        else:
            if self.overwritten == 0:
                self.storage.delete(current_node)
                self.storage.add_to_head(item)
                self.overwritten += 1
            else:
                for i in range(self.overwritten):
                    if current_node.next:
                        current_node = current_node.next
                
                print("current val: ",current_node.value)
                current_node.insert_before(item)
                current_node.delete()
                self.overwritten +=1
                print(self.overwritten)
                if self.overwritten == self.capacity:
                    self.overwritten = 0
            


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next
           
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
