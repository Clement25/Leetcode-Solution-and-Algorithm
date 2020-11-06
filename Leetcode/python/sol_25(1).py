def threesumclosest(nums, target):
    '''
    type nums:List[int]
    type target:int
    rtype:int
    '''
    min = 100000
    for i, n in enumerate(nums[:-2]):
        for j, m in enumerate(nums[i+1:-1]):
            for k, l in enumerate(nums[i+j+2:]):
                dis = abs(m+n+l-target)
                res = m + n + l
                if dis == 0:
                    return res
                if dis < min:
                    min = dis
    return res


print(threesumclosest([-1, 2, 1, -4], 1))
print(12)
