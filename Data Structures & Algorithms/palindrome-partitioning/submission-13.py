class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = set()

        def is_valid(path: List[str]) -> bool:
            t = True
            l = "".join(path)
            # print(f"{l=}")
            for x in path:
                a = x == x[::-1]
                if not a:
                    t = False
            return t and len(l) == len(s)

        def bt(i, j, path):
            if j >= len(s) + 1:
                if is_valid(path):
                    # print(f"FOUND: {path=}")
                    ans.add(tuple(path))
                return
            
            # take as is
            path.append(s[i:j])
            bt(j, j+1, path) # new i
            path.pop()

            # keep expanding
            bt(i, j+1, path)
            return
        bt(0, 1, [])
        print(f"{ans=}")
        ans = [list(x) for x in ans]
        print(f"{ans=}")
        return ans