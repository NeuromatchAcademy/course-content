def fit_second_stage(T_hat, Y):
    """
    Estimates a scalar causal effect from 2-stage least squares regression using
    an instrument.

    Args:
        T_hat (np.ndarray): the output of the first stage regression
        Y (np.ndarray): our observed response (n, 1)

    Returns:
        beta (float): the estimated causal effect
    """
    # Initialize linear regression model
    stage2 = LinearRegression(fit_intercept=True)

    # Fit model to data
    stage2.fit(T_hat, Y)

    return stage2.coef_


# Uncomment below to test your function
T_hat = fit_first_stage(T, Z)
beta = fit_second_stage(T_hat, Y)
print("Estimated causal effect is: {:.3f}".format(beta[0, 0]))