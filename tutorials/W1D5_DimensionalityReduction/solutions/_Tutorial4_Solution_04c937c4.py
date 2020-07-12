###################################################################
# Insert your code here to:
################################################################### 

# perform t-SNE
embed = tsne_model.fit_transform(X)

# Visualize the data
with plt.xkcd():
  visualize_components(embed[:, 0], embed[:, 1], labels)