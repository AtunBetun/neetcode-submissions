class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result[i] => number of days after ith before a warmer temp appears on future day      
        t = temperatures
        r = [0] * len(t)
        s = []
        
        # [30,38,30,36,35,40,28]
        # x = 1
        # s=[30]

        print(f"{t=}")
        for x in range(0, len(t)):
            print(f"{r=} {s=} {x=} {t[x]=}")
            if s == [] or t[x] <= s[-1][0]:
                s.append((t[x], x))
                print(f"adding {s=} {x=} {t[x]=}")
                continue
            
            if t[x] > s[-1][0]:
                y = x
                while s[-1][0] < t[x]:
                    print(f"{y=}")
                    r[s[-1][1]] = y - s[-1][1]
                    s.pop()
                    
                    if s == []:
                        break

                s.append((t[x], x))

        print(f"{s=} {r=}")
        return r
