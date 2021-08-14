"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    slow = fast = head
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_len = calculate_cycle_len(slow)
            return find_start(head, cycle_len)


def calculate_cycle_len(start):
    current = start.next
    length = 1
    while current != start:
        length += 1
        current = current.next

    return length


def find_start(head, cycle_len):
    pointer1 = pointer2 = head
    while cycle_len != 0:
        cycle_len -= 1
        pointer2 = pointer2.next

    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
