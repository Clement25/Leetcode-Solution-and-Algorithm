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


#print(threesumclosest([-55, -24, -18, -11, -7, -3, 4, 5, 6, 9, 11, 23, 33], 0))
#print(threesumclosest([-1,2,1,-4], 1))
#print(threesumclosest([-1,0,1,1,55], 3))
print(
    threesumclosest([
        13, 2, 0, -14, -20, 19, 8, -5, -13, -3, 20, 15, 20, 5, 13, 14, -17, -7,
        12, -6, 0, 20, -19, -1, -15, -2, 8, -2, -9, 13, 0, -3, -18, -9, -9,
        -19, 17, -14, -19, -4, -16, 2, 0, 9, 5, -7, -4, 20, 18, 9, 0, 12, -1,
        10, -17, -11, 16, -13, -14, -3, 0, 2, -18, 2, 8, 20, -15, 3, -13, -12,
        -2, -19, 11, 11, -10, 1, 1, -10, -2, 12, 0, 17, -19, -7, 8, -19, -17,
        5, -5, -10, 8, 0, -12, 4, 19, 2, 0, 12, 14, -9, 15, 7, 0, -16, -5, 16,
        -12, 0, 2, -16, 14, 18, 12, 13, 5, 0, 5, 6
    ], -59))
a = [1,2,3,4]
print(a[0:len(a)])