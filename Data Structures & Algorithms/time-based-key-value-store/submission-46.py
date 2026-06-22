from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value)) # sorted array by timestamp

# ["TimeMap", "set", ["key1", "value1", 10], "get", ["key1", 1], "get", ["key1", 10], "get", ["key1", 11]]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        arr = self.d[key]
        if arr == []:
            return ""
        if len(arr) == 1 and arr[0][0] <= timestamp:
            return arr[0][1]

        l, r = 0, len(arr) - 1
        print(f"{l=} {r=} {arr=} {key=} {timestamp=}")
        while l < r:
            # m = (l+r) // 2
            m = (r + l + 1) // 2 
            x: tuple[int, str] = arr[m]
            print(f"{l=} {m=} {r=}")
            if x[0] <= timestamp: # can be part of solution, keep looking right
                l = m
            else: # too big, look left, not a part of the solution
                r = m - 1
        if arr[l][0] <= timestamp:
            return arr[l][1]
        return ""