
#. 1) The conditional probability distribution is using a measurement to restrict the likely value of
#.    one of the variables. If there is correlation, this will also affect what we know (conditionally)
#.    about the other! However, the marginal probability *only* depends on the direction along
#.    which we are marginalizing. So, when the conditional probability is based on a measurement at the
#.    means, it is the same as marginalization, as there is no additional information. A further note
#.    is that we can also marginalize along other directions (e.g. a diagonal), but we are not exploring
#.    this here.

#. 2) The larger the correlation, the more shared information. So the more we gain about the
#.    second variable (or hidden state) by measuring a value from the other.

#. 3) The variable (hidden state) with the lower variance will produce a narrower
#.    conditional probabilty for the other variable! As you shift the correlation, you will see
#.    small changes in the variable with the low variance shifting the conditional mean of the
#.    variable with the large variance! (So, if X has low variance, changing CY has a big effect.)