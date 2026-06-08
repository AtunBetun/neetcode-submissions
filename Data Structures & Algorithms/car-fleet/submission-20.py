class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        print(f"{position=} {speed=}")
        n = len(position)
        s = []
        f = []
        for x in range(0, n):
            a = (position[x], speed[x])
            s.append(a)
        s.sort(key=lambda x: x[0], reverse=True)
        print(f"{s=}")
        # 10 miles   #
        # ---------- #
        #  1   4     #
        # 10m        X
        # 60m        1hr


        for x in s:
            timeT = (target - x[0]) / x[1]
            print(f"{x=} {timeT=} {f=}")
            # no fleet yet
            if f == []:
                f.append((timeT, x[0]))
                continue

            fleetCar = f[-1][0]
            # car is slower than fleet
            if timeT > fleetCar:
                f.append((timeT, x[0]))
                remain = f[-1]
            # car takes longer, new fleet
            else:
                continue
        print(f"{f=}")
        return len(f)

        