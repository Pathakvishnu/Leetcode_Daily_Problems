from ast import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = dict()
        for idx, val in enumerate(order):
            mapping[val] = idx

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # below condition is for the case like "apple" and "app"
                if j >= len(words[i + 1]): return False

                if words[i][j] != words[i + 1][j]:
                    if mapping[words[i][j]] > mapping[words[i + 1][j]]: return False
                    break

        return True

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"

obj = Solution()
obj.isAlienSorted(words,order)