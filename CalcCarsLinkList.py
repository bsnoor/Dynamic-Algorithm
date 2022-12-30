import random

class Node:
    __data = ' '
    __next = None
    __prev = None

    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def __str__(self):
        return ' ' + self.__data

    def setData(self, value):
        self.__data = value

    def getData(self):
        return self.__data

    def setNext(self, next):
        self.__next = next

    def getNext(self):
        return self.__next

    def setPrev(self, prev):
        self.__prev = prev

    def getPrev(self):
        return self.__prev


class DoubleCycleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def add(self, value):
        # Create a new node with the given value
        new_node = Node(value)

        # Check if the linked list is empty
        if self.__head is None:
            # If the list is empty, the new node becomes the head and the tail
            self.__head = new_node
            self.__tail = self.__head
            # Set the new node's next and prev attributes to point back to itself
            self.__head.setNext(self.__tail)
            self.__head.setPrev(self.__tail)
        else:
            # If the list is not empty, set the new node's next attribute to point to the current head
            new_node.setNext(self.__head)
            # Set the new node's prev attribute to point to the current tail
            new_node.setPrev(self.__tail)
            # Set the current tail's next attribute to point to the new node
            self.__tail.setNext(new_node)
            # Update the __tail attribute to refer to the new node
            self.__tail = new_node
            # Set the current head's prev attribute to point to the new tail
            self.__head.setPrev(self.__tail)
        # Increment the size of the list by 1
        self.__size += 1

    def getHead(self):
        return self.__head

    def __str__(self):
        # Initialize an empty string with the opening square bracket
        s = "["
        # Check if the linked list is not empty
        if self.__head is not None:
            # Set a temporary variable to the head of the list
            temp = self.__head
            # Enter awhile loop that continues as long as temp is not None and temp is not the tail
            while temp is not None and temp is not self.__tail:
                # Add the value of the current node to the string s
                s += temp.getData() + ", "
                # Update temp to the next node in the list
                temp = temp.getNext()
        # Check if temp is None
        if temp is None:
            # If temp is None, return s followed by a closing square bracket
            return s + "]"
        # If temp is not None, return s followed by the value of the tail node
        # and a closing square bracket
        return s + self.__tail.getData() + "]"


class CalcCarsLinkList:
    def __init__(self, sizeMax=13):
        # Initialize an empty double-linked list
        self._cars = DoubleCycleLinkedList()
        # Iterate over the range from 0 to sizeMax - 1
        for i in range(sizeMax):
            # Generate a random capital letter between 'A' and 'Z'
            c = chr(random.randint(65, 90))
            # Uncomment the following lines to exclude the letters 'V' and 'W'
            # while c == "V" or c == "W":
            # c = chr(random.randint(65, 90))
            # Add the letter to the end of the linked list
            self._cars.add(c)
        # Print the linked list
        print(self._cars)

    def calcCars(self):
        '''
        Cars calculation: parking problem with double cycle linked list
        Complexity: O(n^2)
        :return: number of cars
        '''
        # Create a copy of the _cars linked list
        copyListCars = self._cars
        # Check if the linked list is empty
        if copyListCars.getHead() is None:
            # Return 0 if the list is empty
            return 0
        # Set a temporary variable to the head of the list
        temp = copyListCars.getHead()
        # Update the value of the head node to "V"
        copyListCars.getHead().setData("V")
        # Update temp to the next node in the list
        temp = temp.getNext()
        # Initialize a counter to 1
        count = 1
        # Enter an infinite loop
        while True:
            # Check if the value of temp is "V"
            if temp.getData() == "V":
                # If the value is "V", update it to "W"
                temp.setData("W")
                # Set steps equal to count
                steps = count
                # Enter a loop that continues as long as steps is greater than 0
                while steps > 0:
                    # Update temp to the previous node in the list
                    temp = temp.getPrev()
                    # Decrement steps by 1
                    steps -= 1
                # Check if the value of temp is "W"
                if temp.getData() == "W":
                    # If the value is "W", break out of the outer loop
                    break
                else:
                    # If the value is not "W", reset count to 1,
                    # set temp to the head of the list,
                    # and update temp to the next node in the list
                    count = 1
                    temp = copyListCars.getHead()
                    temp = temp.getNext()
            else:
                # If the value of temp is not "V", update temp to the next node in the list and increment count by 1
                temp = temp.getNext()
                count += 1
        # Return the value of count
        return count

    def calcCarsTwoPointers(self):
        '''
        Cars calculation: parking problem with two pointers
        Complexity: O(n)
        :return: number of cars
        '''
        # Check if the linked list is empty
        if self._cars.getHead() is None:
            # Return 0 if the list is empty
            return 0
        # Set headNode to the head of the linked list
        headNode = self._cars.getHead()
        # Set nodeForward to the next node after headNode
        nodeForward = headNode.getNext()
        # Initialize a counter to 1
        count = 1
        # Enter a loop that continues as long as nodeForward is not headNode
        while nodeForward is not headNode:
            # Update nodeForward to the next node in the list
            nodeForward = nodeForward.getNext()
            # Increment count by 1
            count += 1
        # Return the value of count
        return count

    
if __name__ == '__main__':
    '''
    Capital letters are in range of 65, 90
    small letters are in the range 97 (ascii 'a' is 97,), 97+26-1 (there are 26 letters in the alphabet)
    arr = [chr(random.randrange(65,90)) for i in range(13)]
    print("array:", arr)

    print(chr(90))
    '''

    # Create an instance of CalcCarsLinkList
    parking = CalcCarsLinkList()
    # Print the number of cars using the calcCars method
    print("number of cars by DCLL =", parking.calcCars())
    # Print the number of cars using the calcCarsTwoPointers method
    print("number of cars by two pointers =", parking.calcCarsTwoPointers())


