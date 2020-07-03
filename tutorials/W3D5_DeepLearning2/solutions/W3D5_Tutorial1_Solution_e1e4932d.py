
pca = sk.decomposition.PCA(n_components=2)

pca.fit(input_train)

pca_latent_test = pca.transform(input_test)

with plt.xkcd():
  plot_latent_generative(pca_latent_test, y_test, pca.inverse_transform, 
                      image_shape=image_shape, title='SAMPLE OUTPUT')