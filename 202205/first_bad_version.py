def isBadVersion(version: int, bad_version) -> bool:
    if version < bad_version:
        return False
    else:
        return True

class Solution:
    def firstBadVersion(self, n: int, bad_version) -> int:
        """
        Time Limit Exceeded

        for i in range(0,n):
            if isBadVersion(i, bad_version):
                return i
        
        return n
        """
        left_: int = 1
        right_: int = n
        while left_ < right_:
            mid: int = left_ + (right_ - left_) // 2
            if isBadVersion(mid, bad_version):
                right_ = mid
            else:
                left_ = mid + 1
        
        return left_
