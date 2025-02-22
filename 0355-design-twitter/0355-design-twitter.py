class Twitter:
    def __init__(self):
        self.userPosts = defaultdict(list)
        self.timestamp = 0
        self.userFollowing = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userPosts[userId].append((self.timestamp,tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = []
        result = []
        feeds.extend(self.userPosts[userId])
        for followee in self.userFollowing[userId]:
            feeds.extend(self.userPosts[followee])
        recent_tweets = heapq.nlargest(10, feeds, key = lambda x : x[0])
        for _ , tweetid in recent_tweets:
            result.append(tweetid)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowing[followerId]:
            self.userFollowing[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)