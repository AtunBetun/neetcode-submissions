import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.user_feed = defaultdict(list)
        self.time = 0
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_feed[userId].append((self.time, tweetId))
        self.time += 1
        print(f"post feed: {userId=} : {self.user_feed[userId]}")
        
    def getNewsFeed(self, userId: int) -> List[int]:
        print(f"getFeed: {userId=}")
        print(f"getFeed follows: {userId=} : {self.follows[userId]=}")
        h = []
        tweets = set()

        for t in self.user_feed[userId]:
            t = (-t[0], t[1]) # revert so heap becomes max heap
            tweets.add(t)
        
        for f in self.follows[userId]:
            for t in self.user_feed[f]:
                t = (-t[0], t[1]) # revert so heap becomes max heap
                tweets.add(t)
        print(f"tweets: {tweets=}")
        for t in tweets:
            heapq.heappush(h, t)

        feed = []
        l = 0
        while h and l < 10:
            t = heapq.heappop(h)[1]
            feed.append(t)
            l += 1
        print(f"feed: {feed=} {len(feed)=}")
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        print(f"follow: {followerId=} {followeeId=} {self.follows=}")
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print(f"unfollow: {followerId=} {followeeId=} {self.follows=}")
        print(f"{self.follows[followerId]=}")
        self.follows[followerId].discard(followeeId)
        
