"""
In Exercise 1.2, you should have noticed the following:

* No control (blue): the dynamics parameter D controls how fast the dynamics decay
  towards 0. For -1<D<1, the system is stable and therefore approaches zero quickly.
  However, D>1 produces an unstable system, causing , you should have
  noticed that the 'no control' state (blue curve) rapidly explodes
  (i.e., heads off to infinity)

* Open-loop control: While the open-loop state (green curve) often reachs the goal
  quickly, it may not stay there. Under high noise conditions, it tends to
  drift away from the goal, though you may not see this in every simulation.

* Closed-loop control: The closed-loop state (red curve) reaches the goal and
  stays there even in the presence of noise. It converges especially quickly for
  Ls around 0.45

  Remember that in closed-loop control,
  we have a[t]=L[t] * s[t] $. Note that with a constant control gain $L[t]=L,
  the state evolution equations can be rearranged to show that the stability of
  the closed-loop system now depends on the value of D+BL. (See Equation 2, below).

  If $|D+BL|<1$, our closed-loop system will be stable. More generally, you can
  view the role of a closed-loop control input as changing the system *dynamics*
  in an optimal way to reach the goal.
""";