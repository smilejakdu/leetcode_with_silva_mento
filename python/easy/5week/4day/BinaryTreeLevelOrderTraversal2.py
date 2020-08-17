''':arg

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution(object):
    def levelOrderBottom(self, root):

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans

        queue = deque([root])
        while queue:
            r = []
            for i in range(len(queue)):
                node = queue.popleft()
                r.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(r)

        return ans[::-1]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root):
        ans = []
        if root is None:
            return ans

        q = []
        q.append(root)

        while q:
            nodeCount = len(q)
            row = []

            while nodeCount:
                currNode = q.pop(0)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)

                row.append(currNode.val)
                nodeCount -= 1

            ans.insert(0, row)
        return ans
