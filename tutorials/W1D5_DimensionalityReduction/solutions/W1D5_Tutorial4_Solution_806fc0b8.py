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

    # Perform t-SNE
    tsne_model = TSNE(n_components=2, perplexity=perp, random_state=2020)

    embed = tsne_model.fit_transform(X)
    visualize_components(embed[:, 0], embed[:, 1], labels, show=False)
    plt.title(f"perplexity: {perp}")
    plt.show()


# Visualize
values = [50, 5, 2]
with plt.xkcd():
  explore_perplexity(values)