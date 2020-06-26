tsne_model = TSNE(n_components=2,perplexity=30,random_state=1) 
embed = tsne_model.fit_transform(X)

with plt.xkcd():
  visualize_components(embed[:,0],embed[:,1],labels)