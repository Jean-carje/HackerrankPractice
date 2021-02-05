# Problem
# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/
# Score: 5.00 points

# ---------------------------------------------------------
# Solution:

# class SinglyLinkedListNode:
    # def __init__(self, node_data):
        # self.data = node_data
        # self.next = None

# class SinglyLinkedList:
    # def __init__(self):
        # self.head = None

# def print_singly_linked_list(node, sep, fptr):
    # while node:
        # fptr.write(str(node.data))

        # node = node.next

        # if node:
            # fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if head == None:
        head = node
        return head
    last = head
    while last.next:
        last = last.next
    last.next = node
    return head

# ---------------------------------------------------------


