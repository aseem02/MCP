#!/bin/python

import math
import os
import random
import re
import sys
chop = 0
def global_warming(tree, curr):
    global chop
    output = 1;
    if curr not in tree:
        return output     
    for i in tree[curr]:
        temp = global_warming(tree, i)
        if (temp % 2 == 0):
            chop += 1
        else:
            output += temp
    return output

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    tree = {}
    for i in range(len(t_from)):
        if (t_to[i] in tree):
            tree[t_to[i]].append(t_from[i])
        else:
            tree[t_to[i]] = [t_from[i]]
    global_warming(tree, 1)
    return chop

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, raw_input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in xrange(t_edges):
        t_from[i], t_to[i] = map(int, raw_input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
