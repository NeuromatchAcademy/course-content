
# 1) The fisherperson is on the left side so:
#       - P(m = catch fish | s = left) = 0.7 because they have a 70% chance of catching
#         a fish when on the same side as the school
#       - P(m = no fish | s = left) = 0.3 because the probability of catching a fish
#         and not catching a fish for a given state must add up to 1 as these
#         are the only options: 1 - 0.7 = 0.3
#       - P(m = catch fish | s = right) = 0.2
#       - P(m = no fish | s = right) = 0.8

# 2) If the fisherperson catches a fish, you would guess the school of fish is on the
#     left side. This is because the probability of catching a fish given that the
#    school is on the left side (0.7) is higher than the probability given that
#    the school is on the right side (0.2).

# 3) If the fisherperson does not catch a fish, you would guess the school of fish is on the
#     right side. This is because the probability of not catching a fish given that the
#    school is on the right side (0.8) is higher than the probability given that
#    the school is on the right side (0.3).