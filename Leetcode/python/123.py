class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        elif len(prices) == 2:
            return (prices[-1]-prices[0]) if prices[-1]-prices[0]>0 else 0
        
        def maxProfit1deal(prices):
            # firstly find the maximum profits from day0 until 1,2,3,...,n-1, where opt[i] is the max 
            # profits of buying on day 0 and selling on day i+1
            opt1 = [0]*(len(prices)-1)
            buy = prices[0]
            opt1[0] = (prices[1] - buy) if prices[1]>buy else 0
            for i in range(len(opt1)):
                if prices[i+1]<buy:
                    buy=prices[i+1]
                if prices[i+1]-buy>opt1[i-1]:
                    opt1[i] = prices[i+1] - buy
                else:
                    opt1[i] = opt1[i-1]
            
            # secondly find the maximum profits from day 2,...,n-2 until n-1, where opt2[i] is the
            # max profits since day i+2 till day n-1
            opt2 = [0]*(len(prices)-3)
            i = 0
            while i <= len(prices)-4:
                max_profit = 0
                rbday = bday = i
                for j in range(i+1,len(prices)-2):
                    if prices[bday+2] > prices[j+2]:
                        bday = j
                    elif max_profit < prices[j+2]-prices[bday+2]:
                        max_profit = prices[j+2]-prices[bday+2]
                        rbday = bday
                opt2[i] = max_profit
                if rbday > i:
                    end = (rbday + 1) if rbday<len(opt2) else rbday
                    for k in range(i+1,end):
                        opt2[k]=opt2[k-1]
                i = rbday + 1
                if max_profit==0:
                    for k in range(i,len(opt2)):
                        opt2[k] = 0
                    break
            return opt1,opt2
           
        opt1,opt2 = maxProfit1deal(prices)
        max_profit = 0
        for i in range(1,len(prices)-2):
            if opt1[i]+opt2[i-1]>max_profit:
                max_profit = opt1[i]+opt2[i-1]
        
        if max_profit>opt1[-1]:
            return max_profit
        else:
            return opt1[-1]