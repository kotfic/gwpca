from .rest import PCA

def load(info):
    info['apiRoot'].pca = PCA()
