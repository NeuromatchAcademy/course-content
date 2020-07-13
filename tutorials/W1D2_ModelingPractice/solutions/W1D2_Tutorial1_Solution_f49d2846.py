

def my_threshold(selfmotion_vel_est, threshold):
  """
  This function should calculate proportion self motion
  for both conditions and the overall proportion
  correct classifications.

  Args:
      selfmotion_vel_est (numpy.ndarray): A sequence of floats
      indicating the estimated self motion for all trials.

      threshold (float): A threshold for the estimate of self motion when
      the brain decides there really is self motion.

  Returns:
      self-motion: yes or no.
  """

  ##############################################################
  # Compare the self motion estimates to the threshold:
  # Replace 'True' with the proper code:

  is_move = (selfmotion_vel_est > threshold)  # should return true or false.

  ##############################################################

  return is_move