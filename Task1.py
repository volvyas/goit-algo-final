
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __le__(self, other):
        return self.data <= other.data

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size +=1

    def insert_at_end(self, data):
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        self.size += 1
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            self.size -= 1
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None
        self.size -= 1

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        string = "["
        while current:
            string += str(current.data) + ', '
            current = current.next
        if self.size > 0:
            string = string[:-2]
        string += "]"
        print(string)

    def reverse_list(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_left_half(self, linked_list, mid: int):
        left_half = LinkedList()
        current = linked_list.head
        for _ in range(mid):
            left_half.insert_at_end(current.data)
            current = current.next
        return left_half

    def get_right_half(self, linked_list, mid: int):
        right_half = LinkedList()
        current = linked_list.head
        for _ in range(mid):
            current = current.next
        while current:
            right_half.insert_at_end(current.data)
            current = current.next
        return right_half

    def merge_sort(self, linked_list):
        if linked_list.size <= 1:
            return linked_list

        mid = linked_list.size // 2
        left_half = linked_list.get_left_half(linked_list, mid)
        #print("Left:")
        left_half.print_list()
        right_half = linked_list.get_right_half(linked_list, mid)
        #print("Right:")
        right_half.print_list()

        return self.merge(self.merge_sort(left_half), self.merge_sort(right_half))

    def merge(self, left, right):
        merged = LinkedList()
        left_index = 0
        right_index = 0
        left_elem = left.head
        right_elem = right.head

        while left_index < left.size and right_index < right.size:
            if left_elem <= right_elem:
                merged.insert_at_end(left_elem.data)
                left_elem = left_elem.next
                left_index += 1
            else:
                merged.insert_at_end(right_elem.data)
                right_elem = right_elem.next
                right_index += 1

        while left_index < left.size:
            merged.insert_at_end(left_elem.data)
            left_elem = left_elem.next
            left_index += 1

        while right_index < right.size:
            merged.insert_at_end(right_elem.data)
            right_elem = right_elem.next
            right_index += 1

        return merged


llist = LinkedList()

llist.insert_at_beginning(1)
llist.insert_at_beginning(3)
llist.insert_at_beginning(2)
llist.insert_at_beginning(7)
llist.insert_at_beginning(5)
llist.insert_at_beginning(6)
llist.insert_at_beginning(4)

print("Before rev:")
llist.print_list()

#llist.reverse_list()

#print("After rev:")
#llist.print_list()


list1 = llist.merge_sort(llist)
list1.print_list()