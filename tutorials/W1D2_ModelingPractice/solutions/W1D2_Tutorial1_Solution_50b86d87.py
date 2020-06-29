

#### Then we define and implement the threshold 
# for various thresholds:
thresholds = np.arange(-.5,1.501,.001)
# as well as the proportion classified correctly:
prop_correct = np.empty(thresholds.shape)
pselfmove_nomove = np.empty(thresholds.shape)
pselfmove_move = np.empty(thresholds.shape)

def threshold_classify(thresholds,pselfmove_nomove,pselfmove_move):

  # this loops through all the threshold values we're investigating:
  for thr_i, threshold in enumerate(thresholds):

      ##############################################################
      # compare the two self motion estimates to the threshold:
        
      # 1: for v_nomove_est
      is_move = (v_nomove_est > threshold)  # should return true or false.
      pselfmove_nomove[thr_i] = np.sum(is_move)/nomove_n;
      
      # 2: for v_move_est
      is_move = (v_move_est > threshold)  # should return true or false.
      pselfmove_move[thr_i] = np.sum(is_move)/move_n;
      
      ##############################################################

      # calculate the proportion classified correctly: (1-pselfmove_nomove) + () 
      # Correct rejections:
      p_CR = (1-pselfmove_nomove[thr_i]);
      # correct detections:
      p_D = pselfmove_move[thr_i];
      
      # this is corrected for proportion of trials in each condition:
      prop_correct[thr_i] = ((p_CR * nomove_n) + (p_D * move_n)) / (nomove_n + move_n)
      # the simpler line might just be:
      #prop_correct[thr_i] = (p_CR + p_D) / 2

  return prop_correct

#call the function to get classification accuracy for various threshold
prop_correct = threshold_classify(thresholds,pselfmove_nomove,pselfmove_move)
# this plots the results for various thresholds:

with plt.xkcd():
  my_plot_thresholds(thresholds, pselfmove_nomove, pselfmove_move, prop_correct)