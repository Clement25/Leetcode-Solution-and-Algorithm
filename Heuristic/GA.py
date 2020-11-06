# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:42:57 2019

@author: DELL
"""

from utils import *

num_city=30
num_solution=100
mutate_ratio=0.05
cross_ratio=0.20

# 生成地图
gen_location(num_city)

# 获得初始解
distance_mat = get_distance()
solution = gen_init_solution()