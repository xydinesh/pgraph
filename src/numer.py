#!/usr/bin/python
# Dinesh Weerapurage
# 02/23/2010
# numer.py script convert labeled graph into a graph with 0 to n-1
#

import sys

if len(sys.argv) < 2:
    print "./numer.py filename"
    sys.exit(0)
i = 0
j = 0
table = {}
f = open(sys.argv[1])

nodes = 5000
if len(sys.argv) > 2:
    nodes = int(sys.argv[2])
    
chunk = f.readline()
while (chunk):
    chunk = chunk.strip('\n')
    label = chunk.split('\t')

    if label[0] not in table:
        table[label[0]] = i
        i = i + 1

    if label[1] not in table:
        table[label[1]] = i
        i = i + 1
    
    if not label[0] == label[1]:
        if (table[label[0]] < nodes and table[label[1]] < nodes):
            print str(table[label[0]])+"\t"+str(table[label[1]])
            j += 1
    chunk = f.readline()

f.close ();
print "nodes: %d edges: %d" % (nodes, j)
