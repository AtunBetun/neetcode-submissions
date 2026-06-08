class TimeMap:

    def __init__(self):
        self.key_times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_times:
            self.key_times[key] = [(0, "")] 
        self.key_times[key].append((timestamp, value))
        print(f"SET: {key=} {value=} {timestamp=} {self.key_times=}")
        

    def get(self, key: str, timestamp: int) -> str:
        print(f"GET: {key=} {timestamp=} {self.key_times=}")
        if key not in self.key_times:
            return ""
        values = self.key_times[key]
        prev_timestamp = values[-1][0] # most recent element O(1)

        if prev_timestamp <= timestamp:
            return values[-1][1] # most recent value
        left = 0
        right = len(values) - 1
        # bisect right, left => first element > target
        while left < right:
            mid = (left+right) // 2
            print(f"{left=} {mid=} {right=}")
            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        print(f"{left=} {right=}")
        
        return values[left-1][1]
