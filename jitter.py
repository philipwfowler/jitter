#! /usr/bin/env python

import numpy

if __name__ == "__main__":

    import argparse

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

    # determine the minimum and maximum number of y_steps that encapsulates the data
    ymin=int(numpy.min(values)/options.y_step)
    ymax=int(numpy.max(values)/options.y_step)+2


    # now step through the bands of data
    for y in range(ymin,ymax):

        # create an array of Booleans identifying which points lie in the current range
        points_in_range=((y*options.y_step) < values) & (values <= (y+1)*options.y_step)

        # count the number of points in the current range
        num_points = numpy.sum(points_in_range)

        # if there are no points or just one, keep the x coordinate (this is redundant, but makes the logic obvious)
        if num_points in [0,1]:
            x[points_in_range] = 0.
        else:

            # first, pick out the y values in the current range
            y=values[points_in_range]

            if (num_points % 2)==0:

                # if there are an even number create the positive side
                #  which here is [1,2]
                a=numpy.arange(1,(num_points/2)+1,1)
            else:

                # otherwise if there are an odd number create the positive side
                #  which here is [0,1,2]
                a=numpy.arange(0,int(num_points/2.)+1,1)

            # then the negative side which is [-1,-2]
            b=numpy.arange(-1,int(num_points/-2.)-1,-1)

            # now create a new array that can hold both, and interweave them
            c=numpy.empty((a.size + b.size,), dtype=a.dtype)
            c[0::2] = a
            c[1::2] = b

            # lastly scale by the specified dx
            x[points_in_range]=c*options.x_step

    # write the list of (jittered) x and y values to STDOUT
    for i in range(len(values)):
        print "%6.1f %7.3f" % (x[i],values[i])
