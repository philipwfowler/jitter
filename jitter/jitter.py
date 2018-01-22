#! /usr/bin/env python

import numpy

def jitter_data(x,y,x_step,y_step):

    # determine the minimum and maximum number of y_steps that encapsulates the data
    ymin=int(numpy.min(y)/y_step)
    ymax=int(numpy.max(y)/y_step)+2

    # now step through the bands of data
    for iy in range(ymin,ymax):

        # create an array of Booleans identifying which points lie in the current range
        points_in_range=((iy*y_step) < y) & (y <= (iy+1)*y_step)

        # count the number of points in the current range
        num_points = numpy.sum(points_in_range)

        # if there are no points or just one, keep the x coordinate (this is redundant, but makes the logic obvious)
        if num_points in [0,1]:
            x[points_in_range] = 0.
        else:

            # first, pick out the y values in the current range
            y_values=y[points_in_range]

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
            x[points_in_range]=c*x_step

    return(x,y)
