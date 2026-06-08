class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = nums
        n.sort()

        ans = {}

        print(f"{n=}")

        for x in range(0, len(n)):
            i = x + 1
            j = len(n) - 1

            while i < j:
                curr = [n[x], n[i], n[j]]
                curr.sort()
                print(curr)

                if sum(curr) == 0:
                    string_list = list(map(str, curr))
                    k = "".join(string_list)    
                    ans[k] = curr

                if sum(curr) > 0:
                    j -= 1
                else:
                    i += 1
        print(ans)
        return [v for k, v in ans.items()]
