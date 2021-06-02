
#' 1. When the correlation is zero, the two properties are completely independent.
#' This means you don't gain any information about one variable from observing the other.
#' Importantly, the marginal distribution of one variable is therefore independent of the other.

#' 2. The correlation controls the distribution of probability across the joint probabilty table.
#' The higher the correlation, the more the probabilities are restricted by the fact that both rows
#' and columns need to sum to one! While the marginal probabilities show the relative weighting, the
#' absolute probabilities for one quality will become more dependent on the other as the correlation
#' goes to 1 or -1.

#' 3. The correlation will control how much probabilty mass is located on the diagonals. As the
#' correlation goes to 1 (or -1), the probability of seeing the one of the two pairings has to goes
#' towards zero!

#' 4. If we think about what information we gain by observing one quality, the intution from (3.) tells
#' us that we know more (have more information) about the other quality as a function of the correlation.