def fit_first_stage(T, Z):
    """
    Estimates T_hat as the first stage of a two-stage least squares.

    Args:
        T (np.ndarray): our observed, possibly confounded, treatment of shape (n, 1)
        Z (np.ndarray): our observed instruments of shape (n, 1)

    Returns
        T_hat (np.ndarray): our estimate of the unconfounded portion of T
    """

    # Initialize linear regression model
    stage1 = LinearRegression(fit_intercept=True)

    # Fit linear regression model
    stage1.fit(Z, T)

    # Predict T_hat using linear regression model
    T_hat = stage1.predict(Z)

    return T_hat


# Uncomment below to test your function
T_hat = fit_first_stage(T, Z)

T_C_corr = np.corrcoef(T.transpose(), C.transpose())[0, 1]
T_hat_C_corr = np.corrcoef(T_hat.transpose(), C.transpose())[0, 1]
print("Correlation between T and C: {:.3f}".format(T_C_corr))
print("Correlation between T_hat and C: {:.3f}".format(T_hat_C_corr))