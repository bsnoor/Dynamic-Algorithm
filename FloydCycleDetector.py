from random import *

# A Linked List Node
class Node:
    # Constructor
    def __init__(self, data = None, next=None):
        self.__data = data
        self.__next = next

    # Methods:
    def __str__(self):
        return "" + self.__data

    def setData(self, value):
        self.__data = value

    def getData(self):
        return self.__data

    def setNext(self, next):
        self.__next = next

    def getNext(self):
        return self.__next

# Definition for singly-linked list.
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def getHead(self):
        return self.__head

    def getSize(self):
        return self.__size

    # Insert element at the end of this list
    def insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            current = self.__head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(new_node)
        self.__size += 1

    def printLL(self):
        current = self.__head
        while current:
            print(current.getData())
            current = current.getNext()

    def __str__(self):
        s = "["
        if self.__head is not None:
            temp = self.__head
            while temp is not None:
                s += temp.getData()
                temp = temp.getNext()
                if temp is not None:
                    s +=  ", "
        return s + "]"

class FloydCycleDetector:
    # Create a LinkedList
    def __init__(self, sizeMax=13):
        # Initialize an empty LinkedList
        self._list = LinkedList()
        # Enter a loop that continues for the given sizeMax
        for i in range(sizeMax):
            # Generate a random capital letter in the ASCII range 65-90
            l = chr(randint(65, 90))
            # Insert the letter into the LinkedList
            self._list.insert(l)
        # Print the LinkedList
        print(self._list)

    def createLoop(self):
        # Set rand to the head of the LinkedList
        rand = self._list.getHead()
        # Set last to the head of the LinkedList
        last = self._list.getHead()
        # Enter a loop that continues as long as last has a next node
        while last.getNext() is not None:
            # Update last to the next node in the list
            last = last.getNext()
        # Generate a random index in the range 0 to the size of the list
        rand_index = randint(0, self._list.getSize())
        # Set i to 0
        i = 0
        # Enter a loop that continues as long as i is less than rand_index and rand has a next node
        while i < rand_index and rand.getNext() is not None:
            # Update rand to the next node in the list
            rand = rand.getNext()
            # Increment i by 1
            i += 1
        # Set the next pointer of last to point to rand, creating a loop in the LinkedList
        last.setNext(rand)

    def hasLoop(self):
        '''
        Check if the LinkedList has a loop.
        Complexity: O(n)
        :return: true if the list has a loop, otherwise false
        '''
        # Set head to the head of the LinkedList
        head = self._list.getHead()
        # Check if the list is empty or has only one node
        if head is None or head.getNext() is None:
            # Return false if the list is empty or has only one node
            return False
        # Set slow and fast to the head of the LinkedList
        slow = head
        fast = head
        # Enter a loop that continues as long as slow and fast have nodes and fast has a next node
        while slow is not None and fast is not None and fast.getNext() is not None:
            # Update slow to the next node in the list
            slow = slow.getNext()
            # Update fast to the next next node in the list
            fast = fast.getNext().getNext()
            # Check if slow and fast are pointing to the same node
            if slow == fast:
                # Return true if slow and fast are pointing to the same node
                return True
        # Return false if the loop completed without finding a loop
        return False

    def findNodeMeeting(self):
        '''
        Find the node where the two pointers (slow and fast) meet.
        :return: the node where the two pointers meet
        '''
        # Set head to the head of the LinkedList
        head = self._list.getHead()
        # Check if the list is empty or has only one node
        if head is None or head.getNext() is None:
            # Return head if the list is empty or has only one node
            return head
        # Set slow and fast to the head of the LinkedList
        slow = head
        fast = head
        # Enter a loop that continues as long as slow and fast have nodes and fast has a next node
        while slow is not None and fast is not None and fast.getNext() is not None:
            # Update slow to the next node in the list
            slow = slow.getNext()
            # Update fast to the next next node in the list
            fast = fast.getNext().getNext()
            # Check if slow and fast are pointing to the same node
            if slow == fast:
                # Break out of the loop if slow and fast are pointing to the same node
                break
        # Return fast
        return fast

    def findNodeStartLoop(self, meetingNode):
        '''
        Find the start node of the loop in the LinkedList.
        :param meetingNode: the node where the two pointers (slow and fast) meet
        :return: the start node of the loop
        '''
        # Set head to the head of the LinkedList
        head = self._list.getHead()
        # Check if the list is empty or has only one node
        if head is None or head.getNext() is None:
            # Return head if the list is empty or has only one node
            return head
        # Set slow to the head of the LinkedList
        slow = head
        # Set fast to the meeting node
        fast = meetingNode
        # Enter a loop that continues as long as slow and fast are not equal
        while slow is not fast:
            # Update fast to the next node in the list
            fast = fast.getNext()
            # Update slow to the next node in the list
            slow = slow.getNext()
            # Check if slow and fast are pointing to the same node
            if slow == fast:
                # Break out of the loop if slow and fast are pointing to the same node
                break
        # Return slow
        return slow

    def lengthLoop(self, startLoopNode):
        '''
        Find the length of the loop in the LinkedList.
        :param startLoopNode: the start node of the loop
        :return: the length of the loop
        '''
        # Initialize a variable lenLoop to 0
        lenLoop = 0
        # Set slow to the start node of the loop
        slow = startLoopNode
        # Set fast to the start node of the loop
        fast = startLoopNode
        # Update fast to the next node in the list
        fast = fast.getNext()
        # Increment lenLoop by 1
        lenLoop += 1
        # Enter a loop that continues as long as slow and fast are not equal
        while slow is not fast:
            # Update fast to the next node in the list
            fast = fast.getNext()
            # Increment lenLoop by 1
            lenLoop += 1
        # Return lenLoop
        return lenLoop

    
if __name__ == '__main__':
    # Create an instance of FloydCycleDetector
    detect = FloydCycleDetector()
    # Print whether the LinkedList has a cycle
    print("Has the list a cycle?", detect.hasLoop())
    # Create another instance of FloydCycleDetector
    detect_ = FloydCycleDetector()
    # Create a loop in the LinkedList
    detect_.createLoop()
    # Print whether the LinkedList has a cycle
    print("Has the list a cycle?", detect_.hasLoop())
    # Find the node where the two pointers meet
    meetingNode = detect_.findNodeMeeting()
    # Print the node where the two pointers meet
    print("Meeting node is", meetingNode)
    # Find the start node of the loop
    startLoopNode = detect_.findNodeStartLoop(meetingNode)
    # Print the start node of the loop
    print("Start loop node is", startLoopNode)
    # Find the length of the loop
    lengthLoop = detect_.lengthLoop(startLoopNode)
    # Print the length of the loop
    print("A length of the cycle is", lengthLoop)
