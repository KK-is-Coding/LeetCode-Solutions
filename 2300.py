# Successful Pairs of Spells and Potions

import bisect


class Solution:
    def successfulPairs(self, spells, potions, success):
        # pairs = [0]*len(spells)
        # for i in range(len(spells)):
        #     count = 0
        #     for j in range(len(potions)):
        #         if (potions[j]*spells[i]) >= success:
        #             count += 1

        #     pairs[i] = count

        # return pairs

        pairs = []
        potions.sort()
        for a in spells:
            count = len(potions) - bisect.bisect_left(potions,(success + a - 1) // a)
            pairs.append(count)
        return pairs
