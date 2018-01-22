#! /usr/bin/env python

import numpy
import jitter

if __name__ == "__main__":

    import argparse, jitter

    parser = argparse.ArgumentParser()
    parser.add_argument("--y_step",default=0.2,type=float,help="the name of the gene")
    parser.add_argument("--x_step",default=0.2,type=float,help="the 3-letter name of the drug")
    parser.add_argument("--x_centre",default=0.0,help="the x-coordinate to jitter around")
    parser.add_argument("--filename",required=True,help="the name of the space-delimited textfile containing the y-values in a specified column")
    parser.add_argument("--column",type=int,default=0,help="the number of the column to read in (0-based)")
    options = parser.parse_args()

    # load in the list of values to jitter
    values=numpy.sort(numpy.loadtxt(options.filename,dtype=float,usecols=[options.column]))

    # create an array of zeros to store the (jittered) x-coordinates
    x=numpy.zeros(values.shape)

    X,Y=jitter.jitter_data(x,values,options.x_step,options.y_step)

    # write the list of (jittered) x and y values to STDOUT
    for (i,j) in zip(X,Y):
        print("%6.1f %7.3e" % (i,j))
