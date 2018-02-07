#! /usr/bin/env python

import pandas,numpy

def jitter_data(filename,sep="\t",x_step=0.5,y_step=0.5,columns=[0,1],x_centre=0):
    '''
    jitters data
    '''

    # read in the plain text data file as a pandas dataframe
    df=pandas.read_csv(filename,sep="\t",names=["label","y"],usecols=columns)

    # assuming it has a fileextension
    tmp=filename.split('.')
    file_stem=tmp[:-1][0]
    file_ending=tmp[-1]

    # sort the dataset in descending order
    df.sort_values(by=['y'],ascending=False,inplace=True)

    # add an extra column to record the x values
    df['x'] = pandas.Series(numpy.zeros(len(df)), index=df.index)

    # determine the minimum and maximum number of y_steps that encapsulates the data
    ymin=int(df.y.min()/y_step)
    ymax=int(df.y.max()/y_step)+2

    # now step through the bands of data
    for iy in range(ymin,ymax):

        # create an array of Booleans identifying which points lie in the current range
        points_in_range=((df.y > (iy*y_step)) & (df.y <= (iy+1)*y_step))

        # count the number of points in the current range
        num_points = numpy.sum(points_in_range)

        if num_points>1:
            if (num_points % 2)==0:

                # if there are an even number create the positive side (which here is [1,2])
                a=numpy.arange(1,(num_points/2)+1,1)

            else:

                # otherwise if there are an odd number create the positive side (which here is [0,1,2])
                a=numpy.arange(0,int(num_points/2.)+1,1)

            # then the negative side which is [-1,-2]
            b=numpy.arange(-1,int(num_points/-2.)-1,-1)

            # now create a new array that can hold both,
            c=numpy.empty((a.size + b.size,), dtype=a.dtype)

            # ..and interweave them
            c[0::2] = a
            c[1::2] = b

            df.loc[points_in_range,'x']=(c*x_step)+x_centre

    # finally save it all to disc
    df.to_csv(file_stem+"-jittered."+file_ending,header=False,index=False,sep=sep)
