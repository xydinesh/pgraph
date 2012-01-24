#!/usr/bin/python
import sys
import GraphException
import logging
#import argparse

"""
This Graph library will build an object for undirected graphs from DIMACS files.
"""
class Graph:

    def __init__ (self, file):
        self._file = file
        self._buf = []
        self._n = 0
        self._e = 0
        #self._parser = argparse.ArgumentParser(description="Process CMD options")
        logging.basicConfig(filename="graph.log", filemod="a+", level=logging.DEBUG)
        #__addOptions__()

    """
    Method to populate options
    """
    def __addOptions__(self):
        self._parser.add_argument('integers', metavar='N', type=int, nargs='+',
                            help='an integer for the accumulator')
        self._parser.add_argument('--sum', dest='accumulate', action='store_const',
                            const=sum, default=max,
                            help='sum the integers (default: find the max)')
        args = self._parser.parse_args()
        print args

    """
    Reading graph from a DIMACS file
    """
    def read (self):
        f = open(self._file, "r")
        (n, e) = f.readline().strip().split()
        self._n = n = int(n)
        self._e = e = int(e)

        ecount = 0;
        for i in xrange(n):
            self._buf.append([])
            self._buf[i] = [0]*(n)

        for i in f:
            a = i.strip().split()
            if len(a) > 1:
                self._buf[int(a[0])][int(a[1])] = 1

    """
    Check whether graph is a simple one
    1. No multiple edges
    2. No self edges (loops)

    While reading the graph we already ignored
    self edges therefore looking for multiple edges now 
    """
    def isSimple(self):
        ecount = 0;
        for i in xrange(self._n):
            for j in xrange(self._n):
                if (self._buf[i][j] == 1) and (self._buf[i][j] == self._buf[j][i]):
                    x = "Duplicate edges : "+str(i)+" "+str(j)
                    raise GraphException.GraphException(x);
                elif (self._buf[i][j] == 1):
                    ecount += 1
                    
        if ecount != self._e:
            x = "Wrong edge count: "+str(self._e)+", correct: "+str(ecount)
            raise GraphException.GraphException(x)

    def makeSimple(self):
        ecount = 0;
        for i in xrange(self._n):
            for j in xrange(self._n):
                if (j > i) and (self._buf[i][j] == 1):
                    self._buf[j][i] = 0
                    ecount += 1
        self._e = ecount

    def writeGraph(self, name):
        f = open(name, "w")
        sys.stdout = f
        print("%d\t%d") %(self._n, self._e)
        for i in xrange(self._n):
            for j in xrange(self._n):
                if (j > i) and (self._buf[i][j] == 1):
                    print("%d\t%d") %(i, j)
        
                
        

if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            print("%s filename outputname") % (sys.argv[0])
            sys.exit(-1)
        g = Graph(sys.argv[1])
        logging.info("Reading graph")
        g.read()

        #logging.info("check whether graph is a simple graph")
        #g.isSimple()

        logging.info("making graph simple")
        g.makeSimple()

        logging.info("writing new graph"+sys.argv[2])
        g.writeGraph(sys.argv[2]);

        g.isSimple()


    except GraphException.GraphException, e:
        print e.value
        logging.debug(e.value)
                

        

