def expected_loss_calculation(x, posterior):
  
  ExpectedLoss_MSE = np.zeros_like(x)
  ExpectedLoss_ABSE = np.zeros_like(x)
  ExpectedLoss_01 = np.zeros_like(x)

  for idx in np.arange(x.shape[0]):
    estimate = x[idx]

    ###################################################################
    ## Insert code below to find the expected loss under each loss function
    ## 
    ## remove the raise when the function is complete
    #raise NotImplementedError("Calculate the expected loss over all x values!")
    ################################################################### 

    MSELoss = mse(estimate, x)
    ExpectedLoss_MSE[idx] = np.sum(MSELoss * posterior)

    ABSELoss = abs_err(estimate, x)
    ExpectedLoss_ABSE[idx] = np.sum(ABSELoss * posterior)

    ZeroOneLoss = zero_one_loss(estimate, x)
    ExpectedLoss_01[idx] = np.sum(ZeroOneLoss * posterior)

  ###################################################################
  ## Now, find the `x` location that minimizes expected loss
  ## 
  ## remove the raise when the function is complete
  # raise NotImplementedError("Finish the Expected Loss calculation")
  ################################################################### 

  min_MSE = x[np.argmin(ExpectedLoss_MSE)]
  min_ABSE = x[np.argmin(ExpectedLoss_ABSE)]
  min_01 = x[np.argmin(ExpectedLoss_01)]

  return (ExpectedLoss_MSE, ExpectedLoss_ABSE, ExpectedLoss_01, 
          min_MSE, min_ABSE, min_01)

## Uncomment the lines below to plot the expected loss as a function of the estimates
ExpectedLoss_MSE, ExpectedLoss_ABSE, ExpectedLoss_01,  min_MSE, min_ABSE, min_01 = expected_loss_calculation(x, posterior)

with plt.xkcd():
  loss_plot(x, ExpectedLoss_MSE, min_MSE, f"Mean Squared Error = {min_MSE:.2f}")
  loss_plot(x, ExpectedLoss_ABSE, min_ABSE, f"Absolute Error = {min_ABSE:.2f}")
  loss_plot(x, ExpectedLoss_01, min_01, f"Zero-One Error = {min_01:.2f}")