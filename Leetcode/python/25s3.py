def threesumclosest(nums, target):
    '''
    type nums:List[int]
    type target:int
    rtype:int
    '''
    mind = 100000
    nums.sort()
    for i, v in enumerate(nums[:-2]):
        ntgt1 = target - v
        for j, u in enumerate(nums[i + 1:-1]):
            ntgt2 = ntgt1 - u
            if ntgt2 in nums[i + j + 2:]:
                return target
            for k, w in enumerate(nums[i + j + 2:]):
                if w > ntgt2:
                    break
            l = i + j + k + 1
            dis1 = abs(w - ntgt2)
            dis2 = abs(ntgt2 - nums[l]) if k != 0 else dis1
            dis = min(dis1, dis2)
            if dis < mind:
                mind = dis
                res = u + v + w if dis1 <= dis2 else u + v + nums[l]
    return res
