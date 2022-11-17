class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """ 
        Tricky part in this question is finding common area. So, there can be three cases for common area :

        1) No overlapping -> in this case our area can go negative so that's why we calculate max(res,0)

            ax1 ------------------- ax2
                                        bx1 -------------- bx2

        2) Partial Overlapping -> in this case both is partially overlapping with each other.

            ax1 ------------------- ax2
                        bx1 -------------- bx2

        3) Complete Overlapping -> in this case one of the rectilinear is completely engulfed.

            ax1 ------------------------- ax2
                  bx1-------------- bx2
        """
        area1 = (ax2-ax1)*(ay2-ay1)
        area2 = (bx2-bx1)*(by2-by1)
        common = max(min(ax2,bx2) - max(ax1,bx1),0) * max(min(ay2,by2) - max(ay1,by1),0)

        return area1+area2-common