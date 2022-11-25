class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        count = 1

        while itr:
            print(f"\t{count}) {itr.data}")
            itr = itr.next
            count += 1

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        count = 1

        while itr:
            print(f"\t{count}) {itr.data}")
            itr = itr.prev
            count += 1

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


dl = DoublyLinkedList()
dl.insert_values([25, 50, 40, 83])

while True:
    print("\n\nSelect your option:\n1) View transactions in newest order\n2) View transactions in oldest order\n3) Add transaction\n4) Remove transaction\n5) Exit")
    choice = int(input("\nChoice: "))

    if choice == 1:
        print("\nTransactions in newest order:")
        dl.print_forward()

    elif choice == 2:
        print("\nTransactions in oldest order:")
        dl.print_backward()

    elif choice == 3:
        amt = int(input("Enter amount spent: "))
        idx = int(input("Enter index to add at: "))
        dl.insert_at(idx, amt)

        print(f"\nAdded {amt} at index {idx}")

    elif choice == 4:
        idx = int(input("Enter index to remove transaction: "))
        dl.remove_at(idx)

        print(f"\nRemoved transaction at index {idx}")

    elif choice == 5:
        print("\nExiting")
        break

    else:
        print("\nInvalid choice")
        continue
