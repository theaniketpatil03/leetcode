'''
Question - 

You are given two 'non-empty' linked lists representing two 'non-negative' integers.
The digits are stored in 'reverse order' and each their nodes contain a single digit.
Add the two numbers and return it as a linked list

Example - 

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

class node:

    def __init__(self, data=None) -> None:
        self.head = data
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = node()


