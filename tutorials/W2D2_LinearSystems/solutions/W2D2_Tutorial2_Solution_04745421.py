"""
Discussion: 
Which of the eigenvalues corresponds to the stable solution?
What is the eigenvector of this eigenvalue?
How does that explain the equilibrium solutions in Section 2?

Recommendation: 
Ask the students to work in small groups (of 2 or 3) to discuss these questions.


Answers:
Whichever eigenvalue is 1 is the stable solution. There should be another
eigenvalue that is <1, which means it is decaying and goes away after the
transient period.

The eigenvector corresponding to this eigenvalue is the stable solution. 
To see this, we need to normalize this eigenvector so that its 2 elements
sum to one, then we would see that the two numbers correspond to
[P(open), P(closed)] at equilibrium -- hopefully these are exactly the
equilibrium solutions observed in Section 2.


""";


# whichever eigenvalue is 1, the other one makes no sense
print(eigenvector1 / eigenvector1.sum())
print(eigenvector2 / eigenvector2.sum())