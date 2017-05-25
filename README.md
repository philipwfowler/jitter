# jitter
Simple python for adding jitter to a list of values to help plotting beeswarm/jitter plots 

The first few lines of the file test.dat looks like this

        f99y   10   1.884   0.000  -0.909   0.000   2.793   0.000 102.485   0.000
        f99y   10   1.466   0.000  -1.066   0.000   2.533   0.000  67.124   0.000
        f99y   10   0.885   0.000  -1.412   0.000   2.296   0.000  45.752   0.000
        f99y   10   1.915   0.000  -1.028   0.000   2.943   0.000 130.686   0.000

Let's say we want to plot column 2 (remember is 0-based). If you do this naively, many of the points will lie on top of one another. To see where they all are, we can add some jitter.

    ./jitter.py --filename test.dat --column 2 --x_step 0.2 --y_step 0.2 --x_centre 0.0 > jittered.dat
    
Now the graph looks something like this. 



If you play around with the x_step and y_step values and pointsize you can pack the points closer together. And, yes, I know MatPlotLib and Seaborn etc can do this. I wanted something I could use with gnuplot v4.6 (not 5).
