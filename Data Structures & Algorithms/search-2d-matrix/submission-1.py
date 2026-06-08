class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_list = []
        for x in matrix:
            new_list.extend(x)

        l = 0
        r = len(new_list) - 1
        while l<=r:
            m = (l+r)//2
            if target == new_list[m]:
                return True
            elif target > new_list[m]:
                l = m+1
            else:
                r = m-1
        return False
                
        

        