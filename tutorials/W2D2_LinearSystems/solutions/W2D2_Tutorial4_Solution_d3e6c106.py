
# define the model order, and use AR_model() to generate the model and prediction
r = 5 # remove later
x1, x2, p = AR_model(x, r)

# Plot the Training data fit
# Note that this adds a small amount of jttter to horizontal axis for visualization purposes
with plt.xkcd():
  plot_training_fit(x1, x2, p)