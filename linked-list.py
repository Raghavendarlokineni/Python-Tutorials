import debugpy
class Element():
    """
    element class for creating an element/object

    Attributes:
        value - any data type
        next - int 
    """
    def __init__(self, value):
        """
        intializer method for element class
        """
        self.value = value
        self.next = None

class LinkedList():
    """
    linkedList class for creating a linked list

    Attributes:
        head 
    """
    def __init__(self, head=None):
        """
        intializer method for LinkedList class
        """
        self.head = head

    def append(self, new_element):
        """
        method to append new element to the linked list
        
        Args:
            new_element 
        Returns:
            None
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element

    def get_position(self, position):
        """
        Method to find out the element in the given position
        
        Args: 
            position - int
        Returns:
            Element at the position required
        """
        current = self.head
        counter = 1
        #debugpy.breakpoint()
        if self.head:
            while current:
                print("value is", current.value)
                if position == counter:
                    return current
                counter += 1
                current = current.next 
        return None
    def insert(self, new_element, position):
        """
        Method to insert the element at position required

        Args:
            new_element - Element object
            position - int to insert
        Returns:
            None
        """
        current = self.head
        
        if self.head:
            #debugpy.breakpoint()
            while position-1:
                if position-1 == 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                position -= 1
            print(current.value)
            
        else:
            self.head = new_element
        return None
    def delete(self, value):
        """
        Method to delete for a given value

        Args:
            value - int
        Returns:
            None
        """
        current = self.head
        #debugpy.breakpoint()
        next_element = current
        if current.value == value:
                self.head = current.next
                current = None
                return None
        else:
            while current:
                if current.value == value:
                    next_element.next = current.next
                    current = None
                    return None
                next_element = current
                current = current.next
        return None
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print("test - 1 = 3",ll.head.next.next.value)
# Should also print 3
print ("test - 2 = 3",ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ("test - 34 = 3",ll.get_position(4).value)
print ("test - 33 = 4",ll.get_position(3).value)
print ("test - 32 = 2",ll.get_position(2).value)
print ("test - 31 = 1",ll.get_position(1).value)

# Test delete
ll.delete(0)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
