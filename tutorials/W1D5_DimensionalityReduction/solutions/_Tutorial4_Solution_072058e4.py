

def explore_perplexity(values):
  """
  Plots a 2D representation of the data for visualization with categories
  labelled as different colors using different perplexities.

  Args:
    values (list of floats) : list with perplexities to be visualized

  Returns:
    Nothing.

  """

  for perp in values:
    ###################################################################
    # Insert your code here to:
    # redefine the t-SNE "model" while setting perplexity
    # perform t-SNE on the data and plot the results
    # for perplexity = 50, 5, and 2 (set random_state to 2020)
    ###################################################################

    # perform t-SNE
    tsne_model = TSNE(n_components=2, perplexity=perp, random_state=2020) 

    # Comment these lines when you complete the function
    # raise NotImplementedError("Student Exercise! Explore t-SNE with different perplexity")

    embed = tsne_model.fit_transform(X)
    visualize_components(embed[:, 0], embed[:, 1], labels, show=False)
    plt.title(f"perplexity: {perp}")
    plt.show()


# Uncomment when you complete the function
values = [50, 5, 2]
with plt.xkcd():
  explore_perplexity(values)