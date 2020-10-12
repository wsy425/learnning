class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


diff , per = 999, 999
def getMinimumDifference(self, root: TreeNode) -> int:
    def Search(root):
        if root == None:
            return
        Search(root.left)
        self.diff = min(self.diff , abs(self.per - root.val))
        self.per = root.val
        Search(root.right)
    Search(root)
    return self.diff

getMinimumDifference([1,1,3,2])