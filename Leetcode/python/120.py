class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==1:
            return triangle[0][0]
        
        minimum = [[0]*i for i in range(1,len(triangle)+1)]
        minimum[0][0] = triangle[0][0]
        
        for i in range(1,len(triangle)):
            for j in range(i+1):
                if j==0:
                    minimum[i][0] = minimum[i-1][0]+triangle[i][0]
                elif j==i:
                    minimum[i][i] = minimum[i-1][i-1]+triangle[i][i]
                else:
                    minimum[i][j] = min(minimum[i-1][j]+triangle[i][j],
                                        minimum[i-1][j-1]+triangle[i][j])
        
        return min(minimum[len(triangle)-1])