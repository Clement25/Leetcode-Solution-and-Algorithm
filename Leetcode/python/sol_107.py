# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        treeArray = []
        if not root:
            return None
        
        treeArray.append([root])
        i = 0
        
        while treeArray[i]:
            res = []
            for r in treeArray[i]:
                if r.left:
                    res.append(r.left)
                if r.right:
                    res.append(r.right)
            treeArray[i] = [n.val for n in treeArray[i]]
            treeArray.append(res)
            i += 1
        
        treeArray.reverse()
        return treeArray[1:]
            