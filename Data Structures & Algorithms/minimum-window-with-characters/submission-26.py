from collections import deque, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        q = deque([])
        t_count = Counter(t)
        curr_count = Counter()
        ans = ""

        def is_valid(c: Counter, t: Counter) -> bool:
            a = c <= t
            # print(f"CHECK: {c=} {t=} {a=}")
            return c >= t

        for r in range(len(s)):
            q.append(s[r])
            curr_count[s[r]] += 1
            # print(f"{q=} {ans=}")
            while q and curr_count >= t_count: # found answer, start shrinking
                curr_ans = "".join(q)
                # print(f"FOUND: {curr_ans=}")
                if len(curr_ans) < len(ans) or ans == "":
                    print(f"NEW_MIN: {curr_ans=}")
                    ans = curr_ans
                popped = q.popleft()
                curr_count[popped] -= 1
        return ans