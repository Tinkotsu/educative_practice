"""

Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second
half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the
LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    slow = fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    reverted_half_head = revert(slow)

    while reverted_half_head != slow:
        temp = head.next
        head.next = reverted_half_head
        head = temp

        temp = reverted_half_head.next
        reverted_half_head.next = head
        reverted_half_head = temp


def revert(head):
    prev = None
    while head is not None:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()

"""
Time Complexity
The above algorithm will have a time complexity of O(N)O(N) where ‘N’ is the number of nodes in the LinkedList.

Space Complexity
The algorithm runs in constant space O(1)O(1).
"""
