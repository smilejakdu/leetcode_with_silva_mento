''':arg
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

''':arg
answer1
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = {}
        while head:
            if head in nodes:
                return True
            nodes[head] = head
            head = head.next
        return False


''':arg
answer2
'''


class Solution(object):
    def hasCycle(self, head):
        nodes = set()

        current_node = head
        while current_node:
            if current_node in nodes:
                return True
            else:
                nodes.add(current_node)
            current_node = current_node.next

        return False
