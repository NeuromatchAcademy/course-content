
"""
You should only be updating the V[state] once the conditioned stimulus appears.

If you remove this term the Value Function becomes periodic, dropping towards zero
right after the reward and gradually rising towards the end of the trial. This
behavior is actually correct, because the model is learning the time until the
*next* reward, and State 37 is closer to a reward than State 21 or 22.

In an actual experiment, the animal often just wants rewards; it doesn't care about
/your/ experiment or trial structure!
""";