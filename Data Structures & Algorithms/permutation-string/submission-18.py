class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        i = 0
        j = n - 1
        counter = Counter(s1)
        print(f"{s1=} {s2=} {i=} {j=}")
        while j != len(s2):
            print(f"{i=} {j=}")
            sub = ""
            currCount = {}
            for x in range(i, j + 1):
                print(f"{x=}")
                sub = sub + s2[x]
            currCount = Counter(sub)
            print(f"{i=} {j=} {counter=} {currCount=} {sub=}")

            if currCount == counter:
                return True
            i += 1
            j += 1
            print("end")
        return False
            