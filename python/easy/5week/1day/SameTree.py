''':arg
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

'''

''':arg
answer1 
아래와 같은 답은 사실 정확한 답은 아니라고 생각이든다.
단순하게 left , right 만 생각할것이 아니라 , 
left 와 right 도 같았을때는 어떻게 해야할까?? 라는 고민도 해야할것 같다.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p or not q:
        if p == q:
            return True
        else:
            return False

    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    return False


''':arg
다른 answer 2
'''


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        if p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
