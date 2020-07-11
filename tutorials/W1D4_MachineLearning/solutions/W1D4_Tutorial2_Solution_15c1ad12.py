def model_selection(X, y, C_values):
  """Compute CV accuracy for each C value.

  Args:
    X (2D array): Data matrix
    y (1D array): Label vector
    C_values (1D array): Array of hyperparameter values.

  Returns:
    accuracies (1D array): CV accuracy with each value of C.

  """
  accuracies = []
  for C in C_values:

    # Initialize and fit the model
    model = LogisticRegression(penalty="l2", C=C, max_iter=5000)

    # Get the accuracy for each test split
    accs = cross_val_score(model, X, y, cv=8)

    # Store the average test accuracy for this value of C
    accuracies.append(accs.mean())

  return accuracies

C_values = np.logspace(-4, 4, 9)
accuracies = model_selection(X, y, C_values)
with plt.xkcd():
  plot_model_selection(C_values, accuracies)
