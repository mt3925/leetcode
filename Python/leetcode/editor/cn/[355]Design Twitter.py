# Design a simplified version of Twitter where users can post tweets, follow/unf
# ollow another user and is able to see the 10 most recent tweets in the user's ne
# ws feed. Your design should support the following methods: 
# 
#  
#  
#  postTweet(userId, tweetId): Compose a new tweet. 
#  getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news
#  feed. Each item in the news feed must be posted by users who the user followed 
# or by the user herself. Tweets must be ordered from most recent to least recent.
#  
#  follow(followerId, followeeId): Follower follows a followee. 
#  unfollow(followerId, followeeId): Follower unfollows a followee. 
#  
#  
# 
#  Example:
#  
# Twitter twitter = new Twitter();
# 
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
# 
# // User 1 follows user 2.
# twitter.follow(1, 2);
# 
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
# 
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# 
# twitter.getNewsFeed(1);
# 
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
#  
#  Related Topics 堆 设计 哈希表 
#  👍 206 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import time
import heapq
from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.posts_map = {}
        self.follow_map = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts_map.setdefault(userId, []).append((time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        pq = []
        for followee in self.follow_map.get(userId, set()) | {userId}:
            posts = self.posts_map.get(followee)
            if posts:
                ts, tid = posts[-1]
                heapq.heappush(pq, (-ts, tid, posts[:-1]))
        rst = []
        if not pq:
            return rst
        for _ in range(10):
            _, tid, posts = heapq.heappop(pq)
            rst.append(tid)
            if posts:
                ts, tid = posts[-1]
                heapq.heappush(pq, (-ts, tid, posts[:-1]))
            if not pq:
                break
        return rst

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follow_map.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        try:
            self.follow_map.get(followerId, set()).remove(followeeId)
        except KeyError:
            pass


# Your Twitter object will be instantiated and called as such:
# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     obj = Twitter()
#     obj.postTweet(1, 5)
#     param_2 = obj.getNewsFeed(1)
#     obj.follow(1, 2)
#     obj.postTweet(2, 6)
#     print(obj.getNewsFeed(1))
#     obj.unfollow(1, 2)
