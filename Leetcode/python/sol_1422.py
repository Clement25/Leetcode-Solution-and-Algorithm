class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        init_score = (s[0] == "0")+0
        for char in s[1:]:
            if char == "1":
                init_score += 1
        print(init_score)

        max_score = cur_score = init_score
        for ch in s[1:-1]:
            if ch == "0":
                cur_score += 1
            elif ch == "1":
                cur_score -= 1
            if cur_score > max_score:
                max_score = cur_score
        return max_score
