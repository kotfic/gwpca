import os
import tempfile

from girder_worker.app import app
from girder_worker.utils import girder_job


@girder_job("Principal Component Analysis")
@app.task
def gw_pca(name, csv_path, output_path=None):

    if output_path is None:
        output_path = os.path.join(tempfile.mkdtemp(), 'pca.png')

    import matplotlib
    matplotlib.use('Agg')

    import matplotlib.pyplot as plt
    import pandas as pd

    from sklearn.decomposition import PCA


    iris = pd.read_csv(csv_path)

    X = iris.iloc[:,:-2]
    y = iris.iloc[:,-1]
    target_names = y.unique()

    pca = PCA(n_components=2)
    X_r = pca.fit(X).transform(X)

    plt.figure()
    colors = ['navy', 'turquoise', 'darkorange']
    lw = 2

    for color, target_name in zip(colors, target_names):
        plt.scatter(X_r[y == target_name, 0], X_r[y == target_name, 1],
                    color=color, alpha=.8, lw=lw,
                    label=target_name)
    plt.legend(loc='best', shadow=False, scatterpoints=1)

    plt.title('PCA of {}'.format(name))

    plt.savefig(output_path)

    meta = {"x_var": pca.explained_variance_ratio_[0],
            "y_var": pca.explained_variance_ratio_[1]}

    return meta, output_path
