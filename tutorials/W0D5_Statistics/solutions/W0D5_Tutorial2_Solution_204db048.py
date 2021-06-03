
Pw1r1s1 = 0.999  # the probability of wet grass given rain and sprinklers on
Pw1r1s0 = 0.99   # the probability of wet grass given rain and sprinklers off
Pw1r0s1 = 0.9    # the probability of wet grass given no rain and sprinklers on
Pw1r0s0 = 0.001  # the probability of wet grass given no rain and sprinklers off
Ps = 0.25  # the probability of the sprinkler being on
Pr = 0.1   # the probability of rain that day

# Uncomment once variables are assigned above
A= Ps * (Pw1r1s1 * Pr + (Pw1r0s1) * (1 - Pr))
B= (1 - Ps) * (Pw1r1s0 *Pr + (Pw1r0s0) * (1 - Pr))
print("Given that the grass is wet, the probability the sprinkler was on is: " +
      str(A/(A + B)))