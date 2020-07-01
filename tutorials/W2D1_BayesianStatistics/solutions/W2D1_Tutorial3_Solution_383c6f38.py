
x=np.arange(-5,5,0.01)

mean, median, mode = moments_myfunc(x, posterior)
print(f"Posterior mean is : {mean:.2f}, Posterior median is : {median:.2f}, Posterior mode is : {mode:.2f}")

expected_loss = np.zeros_like(x)

for idx in np.arange(x.shape[0]):
    estimate = x[idx]

    loss = zero_one_loss(estimate, x) # or mse or zero_one_loss
    expected_loss[idx] = np.sum(loss * posterior)

min_loss_location = x[np.argmin(expected_loss)]

print(f"Minimum of Abs_error is : {min_loss_location:.2f}")

with plt.xkcd():
  loss_and_pmoments_plot(x, expected_loss, min_loss_location, "Absolute Error", posterior)