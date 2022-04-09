from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self:
            return "{}".format(self.val)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        if not nums:
            return None

        # 가운데를 루트로 만들고
        # 왼쪽 부분 트리 범위 나누기
        # 왼쪽 자식 노드로 떨구기
        # 오른쪽 부분 트리 범위 나누기
        # 왼쪽 자식 노드로 떨구기
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


if __name__ == "__main__":
    print(Solution().sortedArrayToBST([1, 3]))
