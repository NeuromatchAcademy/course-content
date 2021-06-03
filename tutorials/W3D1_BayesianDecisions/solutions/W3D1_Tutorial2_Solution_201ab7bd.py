
#.  1) Increasing the weight parameter makes the mixture distribution more closely
#.   resemble p(x). This makes sense because it is weighting p(x) in the sum of Gaussians.


#.  2) You can move the two bumps of the mixture model further apart by making the means
#.    u_1 and u_2 of the two Gaussians more different (having one at -4 and one at 4 for
#.    example)


#.  3) If you make the means of the two Gaussians very similar, the mixture will resemble
#.     a single Gaussian (u_1 = 0.25, u_2 = 0.3 for example)

#.  4) You can make a bunch of shapes if the two Gaussian components overlap at all.
#.     If they're completely separated, you'll just get two Gaussian looking bumps
#.