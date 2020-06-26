embed = tsne_model.fit_transform(X)

with plt.xkcd():
  visualize_components(embed[:,0],embed[:,1],labels)
  plt.show()