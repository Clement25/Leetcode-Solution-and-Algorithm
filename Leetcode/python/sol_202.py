class Solution:
    def __init__(self):
        self.path = []
    
    def isHappy(self, n: int) -> bool:
        sqsum = self.sqsum(n)
        # print(sqsum)
        if sqsum in self.path:
            return False
        self.path.append(sqsum)
        return sqsum == 1 or self.isHappy(sqsum)

    def sqsum(self, n: int) -> int:
        sum = 0
        while n != 0:
            sum = sum + (n % 10)**2
            n = n // 10
        return sum