def cross_validate(x_train,y_train,max_order,n_splits):

  # Initialize the split method
  kfold_iterator = KFold(n_splits)

  # Initialize np array mse values for all models for each split
  mse_all = np.zeros((n_splits, max_order+1))

  for i_split, (train_indices, val_indices) in enumerate(kfold_iterator.split(x_train)):
      
      # Split up the overall training data into cross-validation training and validation sets
      x_cv_train = x_train[train_indices]
      y_cv_train = y_train[train_indices]
      x_cv_val = x_train[val_indices]
      y_cv_val = y_train[val_indices]

      # Fit models
      theta_hat = solve_poly_reg(x_cv_train, y_cv_train, max_order)

      # Compute MSE
      mse_this_split = np.zeros((max_order+1))
      for order in range(0, max_order+1):
        X_design= make_design_matrix(x_cv_val, order)
        y_hat = np.dot(X_design, theta_hat[order])
        mse_this_split[order] = np.mean((y_cv_val - y_hat) ** 2)

      mse_all[i_split] = mse_this_split

  #comment this line once you've filled in the function
  #raise NotImplementedError("Student excercise: implement cross-validation")
  return mse_all
