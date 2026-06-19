class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[0])):
                arr.append(matrix[r][c])
        print(arr)
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            print(f"{l=} {m=} {arr[m]=} {r=}")
            if arr[m] == target:
                return True
            elif arr[m] < target: # eliminate right side
                print(f"set r {arr[m]=}")
                l = m + 1
            else:
                print(f"set l {arr[m]=}")
                r = m - 1
        return False