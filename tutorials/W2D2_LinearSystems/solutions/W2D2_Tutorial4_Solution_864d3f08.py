
# Solution
r = 5 # remove later
x1, x2, p = AR_model(x, r) # remove later
print(p) # remove later

# Plot the Training data fit
#  a small gitter to the horizontal axis for visualization purposes
with plt.xkcd():
  plot_training_fit(x1, x2, p)