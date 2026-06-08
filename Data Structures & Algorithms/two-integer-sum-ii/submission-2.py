class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers 
        i = 0
        j = len(n) - 1

        while i < j:
            print(f"{n=} {target=} {i=} {j=}")
            c = n[i] + n[j]

            if c == target:
                return [i + 1, j + 1]

            if c < target:
                i += 1
            else:
                j -= 1


        