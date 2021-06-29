
# 1) P is transforming from all of 2D space to all of 2D space. The range of P is
#.  all of 2D space so the rank is 2. Q is squishing space from 2D to a 1D line.
#.  The range of Q is that 1D line so the rank is 1.

# 2) The null space is the patterns of retinal activity that result in 0 firing for the
#.   LGN neurons. The dimensionality of the null space of P is 0 (only the origin would
#.   be mapped to the origin). The dimensionality of the null space of Q is 1: when we
#.   squish 2D space onto the 1D line, a full 1D line would be squished onto the origin.


# 3) The intrinsic dimensionality of the responses of neurons in population p is 2
#  (the possible response pairs span all of 2D space). For population q, the intrinsic dimensionality
#.  is 1: the possible response pairs lie along a 1D line. These neural responses could be fully described by just
#.  1 number if we switched to a basis for that line.

# 4) We could completely recover the retinal neural activity given the LGN activities in population
#.  p as the matrix P is full rank and invertible. There is no information loss from the
#.  two retinal neurons to the two LGN neurons. We cannot recover retinal activity given population
#.  q since we lose a dimension. There is information loss between retinal neurons and population q
#. LGN neurons.