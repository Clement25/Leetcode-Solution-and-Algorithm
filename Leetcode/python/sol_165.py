class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        v1 = list(map(int, v1))
        v2 = list(map(int, v2))
        
        while v1[-1] == 0 and len(v1) > 1:
            v1 = v1[:-1]
        
        while v2[-1] == 0 and len(v2) > 1:
            v2 = v2[:-1]
        
        if v1 == v2:
            return 0 
        
        comp = min(len(v1), len(v2))
        for i in range(comp):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return  -1
            
        return -1 if len(v1) == comp else 1
    
