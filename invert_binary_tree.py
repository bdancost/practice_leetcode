from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case: If the node is null (empty tree or leaf reached), return None
        if not root:
            return None

        # Step 1: Swap the left and right children of the current node
        root.left, root.right = root.right, root.left

        # Step 2: Recursively call the function to invert both subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root of the newly inverted tree
        return root


# --- TEST CODE ---
# Building the original tree:
#      4
#     / \
#    2   7
root_node = TreeNode(4)
root_node.left = TreeNode(2)
root_node.right = TreeNode(7)

validator = Solution()
inverted_root = validator.invertTree(root_node)

# Verifying the swap: root.left should now be 7 and root.right should be 2
print(f"Root: {inverted_root.val}")
print(f"Left child after inversion: {inverted_root.left.val}")  # Should output: 7
print(f"Right child after inversion: {inverted_root.right.val}")  # Should output: 2