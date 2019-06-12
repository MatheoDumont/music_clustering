import matplotlib.pyplot as plt

from scipy.cluster.hierarchy import dendrogram, linkage, ward, is_valid_linkage
# from scipy.spatial.distance import euclidean

import pandas as pd
from pandas.plotting import scatter_matrix


if __name__ == '__main__':
    datas = pd.read_csv('data.csv', engine='python',
                        delimiter=' ', header=0, encoding="utf8")

    features = "filename zero_cr spectral_centroid spectral_rollof chroma_frequency".split()

    # print(datas[features[1:]])
    data_to_use = datas[features[1:]]
    # scatter_matrix(data_to_use, figsize=(5, 5))
    # plt.show()

    x = linkage(data_to_use, method='ward', metric='euclidean')

    print(x)
    print(is_valid_linkage(x))
    print(datas[['filename']])

    dendrogram(x, color_threshold=0)

    plt.show()
