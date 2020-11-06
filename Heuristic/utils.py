s# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:05:17 2019

@author: DELL
"""
import numpy as np
import os
import random as r
from math import sqrt

def get_distance():
    locations = np.loadtxt('location.txt')
    num_city = len(locations)
    distance_mat = [[0 for _ in range(num_city)] for _ in range(num_city)]
    for i in range(num_city):
        for j in range(i+1,num_city):
            distance_mat[i][j] = distance_mat[j][i] = sqrt((locations[i][0]-locations[j][0])**2 + \
                        (locations[i][1]-locations[j][1])**2)
    return distance_mat

def gen_location(location_num=30):
    locations = set()
    assert location_num > 5
    while len(locations) < location_num:
        x, y = r.randint(0,100), r.randint(0,100)
        locations.add((x,y))
    print(locations)
    
    filename = 'location.txt'
    file = open(filename, 'w')
    
    for location in locations:
        x, y = location
        file.write(str(x)+'\t'+str(y)+'\n')
    file.close()

def gen_init_solution(num_solution, num_cities):
    init_solutions = []
    for i in range(num_solution):
        solution = [i for i in range(num_cities)]
        r.shuffle(solution)
        while solution in init_solutions:
            r.shuffle(solution)
        init_solutions.append(solution)
    return init_solutions

def main():
    distance_mat = get_distance()
    # print(distance_mat)
    init_solutions = gen_init_solution(100,5)
    print(init_solutions)

if __name__=='__main__':
    main()
        
    

