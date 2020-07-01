def pcorrect(out, tilt):
  """Compute proportion of stimuli classified correctly from network output

  Args:
    out (torch.Tensor): output of network for each stimulus, i.e. the
      predicted probability of each stimulus being tilted right
    tilt (torch.Tensor): true tilt of each stimulus (1. for tilt right,
      0. for tilt left)
  
  Returns:
    float: proportion of stimuli classified correctly
  
  """
  out_tilt = (out > 0.5).type(torch.float)  # predicted tilt label: 1. for tilt right, 0. for tilt left (make sure to convert to float!)
  return (tilt == out_tilt).type(torch.float).mean().item()

# Sample 100 randomly oriented stimuli
stimuli, tilt = sample_stimuli(100)

# Initialize CNN and use it to predict tilt right probability of each stimulus
net = DeepCNN()
out = net(stimuli)

# Compute proportion correct
print(f'{100 * pcorrect(out, tilt): .2f}% percent correct')