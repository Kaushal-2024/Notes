class Node:
    def __init__(self, value):
        self.next = None
        self.data = value

class SingalLinkList:
    def __init__(self):
        self.head = None
        self.end = self.head

    def insert(self, value):
        new_node = Node(value)
        if self.head:
            self.end.next = new_node
            self.end = new_node
        else:
            self.head = new_node
            self.end = new_node
        print("after insert :",value)
        self.print_SL()
    
    def print_SL(self):
        print_head = self.head
        while print_head:
            print(print_head.data,end="-> ")
            print_head = print_head.next
        print()
        print("head = ",self.head.data)
        print("end = ",self.end.data)

def main():
    num_sl = SingalLinkList()
    num_sl.insert(1)
    num_sl.insert(2)
    num_sl.insert(3)
    num_sl.insert(4)
    num_sl.insert(5)

    num_sl.print_SL()



if __name__ == "__main__":
    main()
