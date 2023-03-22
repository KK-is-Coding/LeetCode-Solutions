# Best Poker Hand

from collections import Counter


class Solution:
    def bestHand(self, ranks, suits):
        count = Counter(ranks)
        if len(set(suits)) == 1:
            return "Flush"
        elif max(count.values()) >= 3:
            return "Three of a Kind"
        elif max(count.values()) == 2:
            return "Pair"
        else:
            return "High Card"
