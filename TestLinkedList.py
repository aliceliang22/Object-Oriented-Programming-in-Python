#  File: TestLinkedList.py
#  Description: HW 12
#  Student Name: Alice Liang
#  Student UT EID: axl84
#  Course Name: CS 313E
#  Unique Number: 84825
#  Date Created: 07/22/20
#  Date Last Modified: 07/23/20

import sys
class Link (object):

    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):

    # initialize the linked list
    def __init__ (self):
        self.first = None
        self.last = None

    # get number of links 
    def get_num_links (self):

        num = 0
        current = self.first
        while current != None:
            num += 1
            current = current.next

        return num
    
    # add an item at the beginning of the list
    def insert_first (self, data): 

        new_link = Link(data)

        new_link.next = self.first
        self.first = new_link

        if self.last == None:
            self.last = new_link

    # add an item at the end of a list
    def insert_last (self, data): 

        new_link = Link(data)

        if self.first == None:
            self.first = new_link
            self.last = new_link
            return

        self.last.next = new_link
        self.last = new_link

    # add an item in an ordered list in ascending order
    def insert_in_order (self, data): 

        new_link = Link(data)

        current = self.first
        previous = None

        while current != None:
            if data <= current.data:
                if previous != None:
                    tmpLink = previous.next
                    previous.next = new_link
                    new_link.next = tmpLink
                else:
                    self.insert_first(data)
                return

            else:
                previous = current
                current = current.next

        if current == None:
            self.insert_last(data)
            return

    # search in an unordered list, return None if not found
    def find_unordered (self, data): 

        current = self.first

        if current == None:
            return None

        while current.data != data:
            if current.next == None:
                return None
            else:
                current = current.next
    
        return current.data

    # Search in an ordered list, return None if not found
    def find_ordered (self, data): 

        current = self.first

        if current == None:
            return None

        while current.data != data:
            if current.next == None or data < current.data:
                return None
            else:
                current = current.next
    
        return current.data

    # Delete and return Link from an unordered list or None if not found
    def delete_link (self, data):

        previous = self.first
        current = self.first

        if current == None:
            return None

        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next

        if current != None:
            previous.next = current.next

        return current.data

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):

        current = self.first
        s = ''
        while current != None:
            if len(s) > 0:
                s += '  '
            s += str(current.data)
            current = current.next
            
        return s 

    # Copy the contents of a list and return new list
    def copy_list (self):

        current = self.first
        new_LinkedList = LinkedList()
        while current != None:
            new_LinkedList.insert_last(current.data)
            current = current.next
            
        return new_LinkedList

    # Reverse the contents of a list and return new list
    def reverse_list (self): 

        previous = None
        current = self.first
        self.last = self.first

        new_LinkedList = LinkedList()

        while current != None:
            new_LinkedList.insert_first(current.data)
            new = current.next
            current.next = previous
            previous = current
            current = new
        self.first = previous

        return new_LinkedList

    # Sort the contents of a list in ascending order and return new list
    def sort_list (self): 

        if self.first == None:
            return None

        current = self.first
        new_LinkedList = LinkedList()

        while current != None:
            new_LinkedList.insert_in_order(current.data)
            current = current.next

        return new_LinkedList

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):

        data = -sys.maxsize
        current = self.first

        while current != None:
            if data > current.data:
                return False
            else:
                data = current.data
                current = current.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty (self): 

        current = self.first

        if current == None:
            return True

        return False

    # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other): 

        current = other.first
        new_LinkedList = self.copy_list()

        while current != None:
            new_LinkedList.insert_in_order(current.data)
            current = current.next
        
        return new_LinkedList

    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):

        current1 = self.first
        current2 = other.first

        while current1 != None and current2 != None:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next    

        if current1 == None and current2 == None:
            return True

        if current1 == None or current2 == None:
            return False

        return True

    # Return a new list, keeping only the first occurence of an element and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):

        if self.first == None:
            return None
            
        current = self.first

        new_LinkedList = LinkedList()

        while current != None:
            if new_LinkedList.find_unordered(current.data) == None:
                new_LinkedList.insert_last(current.data)
            current = current.next
        
        return new_LinkedList

def main():

    nums = [7, 5, 8, 3, 2, 4, 5, 8, 7, 9, 11]
    nums2 = [-1, 22, 13, 10, 1, 4, 8, 17, 16]

    n = len(nums)

    # Test methods insert_first() and __str__() by adding more than 10 items to a list and printing it.
    list1 = LinkedList()
    for i in range(n):
        list1.insert_first(nums[i])
    # assert str(list1) == "11  9  7  8  5  4  2  3  8  5  7"
    print(list1)


    # Test method insert_last()
    list2 = LinkedList()
    for i in range(n):
        list2.insert_last(nums[i])
    # assert str(list2) == "7  5  8  3  2  4  5  8  7  9  11"
    print(list2)


    # Test method insert_in_order()
    list3 = LinkedList()
    for i in range(n):
        list3.insert_in_order(nums[i])
    # assert str(list3) == "2  3  4  5  5  7  7  8  8  9  11"
    print(list3)


    # Test method get_num_links()
    list4 = list2.get_num_links()
    # assert str(list4) == "11"
    print(list4)


    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there 
    list5 = list2.find_unordered(5)
    list55 = list2.find_unordered(1)
    # assert str(list5) == "5"
    # assert str(list55) == "None"
    print(list5)
    print(list55)


    # Test method find_ordered() 
    # Consider two cases - data is there, data is not there 
    list6 = list3.find_ordered(5)
    list66 = list3.find_ordered(1)
    # assert str(list6) == "5"
    # assert str(list66) == "None"
    print(list6)
    print(list66)


    # Test method delete_link()
    # Consider two cases - data is there, data is not there 
    list7 = list2.delete_link(7)
    list77 = list2.delete_link(1)
    # assert str(list7) == "7"
    # assert str(list77) == "None"
    print(list7) 
    print(list77) 


    # Test method copy_list()
    list8 = list2.copy_list()
    # assert str(list8) == "7  5  8  3  2  4  5  8  7  9  11"
    print(list8)


    # Test method reverse_list()
    list9 = list2.reverse_list()
    # assert str(list9) == "11  9  7  8  5  4  2  3  8  5  7"
    print(list9)


    # Test method sort_list()
    list10 = list2.sort_list()
    # assert str(list10) == "2  3  4  5  5  7  7  8  8  9  11"
    print(list10)


    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    isSorted1 = list2.is_sorted()
    isSorted2 = list3.is_sorted()
    # assert isSorted1 == False
    # assert isSorted2 == True
    print(isSorted1)
    print(isSorted2)


    # Test method is_empty()
    isEmpty1 = list2.is_empty()
    empty = LinkedList()
    isEmpty2 = empty.is_empty()
    # assert isEmpty1 == False
    # assert isEmpty2 == True
    print(isEmpty1)
    print(isEmpty2)


    # Test method merge_list()
    mergelst = LinkedList()
    for i in range(len(nums2)):
        mergelst.insert_in_order(nums2[i])
    list13 = list3.merge_list(mergelst)
    # assert str(list13) == "-1  1  2  3  4  4  5  5  7  7  8  8  8  9  10  11  13  16  17  22"
    print(list13)


    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    list14 = list2.copy_list()
    isEqual1 = list2.is_equal(list14)
    isEqual2 = mergelst.is_equal(list14)
    # assert isEqual1 == True
    # assert isEqual2 == False
    print(isEqual1)
    print(isEqual2)

    
    # Test remove_duplicates()
    remove = list2.remove_duplicates()
    # assert str(remove) == "11  9  7  8  5  4  2  3"
    print(remove)

if __name__ == "__main__":
  main()