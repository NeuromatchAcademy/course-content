
# hint: see np.diff()
inter_switch_intervals = np.diff(switch_times)

# plot inter-switch intervals
with plt.xkcd():
  plot_interswitch_interval_histogram(inter_switch_intervals)