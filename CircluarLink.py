#  File: CircularLink.py
#  Description: HW 13
#  Student Name: Alice Liang
#  Student UT EID: axl84
#  Course Name: CS 313E
#  Unique Number: 84825
#  Date Created: 07/26/20
#  Date Last Modified: 07/28/20

class Link(object):

    def __init__(self):
        self.data = None
        self.next = None


class CircularList(object):

    # Constructor
    def __init__(self):
        self.first = Link()
        self.last = Link()
        # self.first.next = self.last
        # self.last.next = self.first

    # Insert an element (value) in the list
    def insert(self, data):

        new_link = Link()
        new_link.data = data

        if self.first.data == None:
            self.first = new_link
            self.last = new_link
            new_link.next = self.first
        # else:
        self.last.next = new_link
        self.last = new_link
        self.last.next = self.first

    # Find the link with the given data (value)
    def find(self, data):

        current = self.first

        if current == None:
            return None

        while current.data != data:
            current = current.next

        return current

    # Delete a link with a given data (value)
    def delete(self, data):

        previous = None
        current = self.first

        if current == None:
            return None

        while current.data != data:
            previous = current
            current = current.next

            if current == self.first:
                return None

        if previous != None:
            previous.next = current.next

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after(self, start, n):

        previous = None
        current = start

        if current == None:
            return None

        for i in range(n-1):
            previous = current
            current = current.next

        if previous != None:
            previous.next = current.next

        return previous.next

    def deleted_number(self, start, n):

        if start == None:
            return -1

        current = start
        for i in range(n-1):
            current = current.next

        if current != None:
            return current.data

        return -1

    # Return a string representation of a Circular List
    def __str__(self):

        current = self.first
        s = ''
        while current != None:
            if len(s) > 0:
                s += '  '
            s += str(current.data)
            current = current.next

        return s

    def display(self):
        current = self.first
        if self.first is None:
            print("List is empty")
            return
        else:
            print("Nodes of the circular linked list: ")
            # Prints each node by incrementing pointer.
            print(current.data),
            while(current.next != self.first):
                current = current.next
                print(current.data),


def main():

    # Case 0
    num_soldiers = 190
    starting_soldier = 30
    elim_num = 48

    # return a list with the order in which the soldiers were removed in
    cLink = CircularList()

    for i in range(num_soldiers):
        cLink.insert(i+1)

    start = cLink.find(starting_soldier)
    deleteSoldiers = []
    while num_soldiers > len(deleteSoldiers) + 1:
        deletedSoldier = cLink.deleted_number(start, elim_num)
        deleteSoldiers.append(deletedSoldier)
        start = cLink.delete_after(start, elim_num)

    return deleteSoldiers


main()
