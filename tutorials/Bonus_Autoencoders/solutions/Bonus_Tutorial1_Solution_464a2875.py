# create the model
pca = decomposition.PCA(n_components=2)
# fit the model on training data
pca.fit(input_train)
# transformation on 2D space
pca_latent_test = pca.transform(input_test)

# Uncomment to test your code!
with plt.xkcd():
  plot_latent_generative(pca_latent_test, y_test, pca.inverse_transform,
                         image_shape=image_shape)