X = X[:2000,:]
labels = labels[:2000]

score = pca_model.transform(X)

with plt.xkcd():
  visualize_components(score[:,0],score[:,1],labels)
  plt.show()