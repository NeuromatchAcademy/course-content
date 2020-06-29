
x=np.arange(-5, 5, 0.01)

ExpectedLoss_MSE = np.zeros_like(x)

for idx in np.arange(x.shape[0]):
    estimate = x[idx]

    MSELoss = mse(estimate, x)
    ExpectedLoss_MSE[idx] = np.sum(MSELoss * posterior)

min_MSE = x[np.argmin(ExpectedLoss_MSE)]

print(f"Minimum of MSE is : {min_MSE:.2f}")

# Plotting snippet
with plt.xkcd():
  loss_plot(x, ExpectedLoss_MSE, min_MSE, "Mean Squared Error")