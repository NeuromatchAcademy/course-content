
"""
The output is shape 60 by 23589 where 60 is the number of stimulus bins and 23589
is the number of predicted neurons. The out_layer weights have shape 23589 by 480
where 23589 is the number of predicted neurons and 480 is the number of convolutional
units in the conv layer. There are 480 convolutional units because the stimulus
is length 60 and we used 8 $C^{out}$ convolutional channels.
""";