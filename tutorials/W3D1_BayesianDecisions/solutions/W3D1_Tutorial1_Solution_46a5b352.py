
# 1. Using Bayes rule, we know that P(s = left | m = catch fish) = P(m = catch fish | s = left)P(s = left) / P(m = catch fish)
#.   Let's first compute P(m = catch fish):
#.   P(m = catch fish) =  P(m = catch fish | s = left)P(s = left) +  P(m = catch fish | s = right)P(s = right)
#                      = 0.5 * 0.3 + .1*.7
#                      = 0.22
#.   Now we can plug in all parts of Bayes rule:
#    P(s = left | m = catch fish) = P(m = catch fish | s = left)P(s = left) / P(m = catch fish)
#                                 = 0.5*0.3/0.22
#                                 = 0.68

# 2. Using Bayes rule, we know that P(s = right | m = no fish) = P(m = no fish | s = right)P(s = right) / P(m = no fish)
#.   Let's first compute P(m = no fish):
#.   P(m = no fish) =  P(m = no fish | s = left)P(s = left) +  P(m = no fish | s = right)P(s = right)
#                      = 0.5 * 0.3 + .9*.7
#                      = 0.78
#.   Now we can plug in all parts of Bayes rule:
#    P(s = right | m = no fish) = P(m = no fish | s = right)P(s = right) / P(m = no fish)
#                                 = 0.9*0.7/0.78
#                                 = 0.81