import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import math
import time


def euclidean(x1, x2):
    """
    x1 et x2 sont des vecteur de meme taille
    """
    sum = 0
    for elem_x1, elem_x2 in zip(x1, x2):
        sum += math.pow(elem_x2 - elem_x1, 2)

    return math.sqrt(sum)


def np_euclidean(x1, x2):
    arr = np.power(np.array(x2) - np.array(x1), 2)
    return np.sqrt(np.sum(arr))


def matrice_distance(data):
    """
    Compute enclidean distance between each element 
    and return a len(elements) * len(elements) matrice
    """
    size = len(data)
    res = np.zeros((size, size))

    for i in range(size):
        for j in range(i + 1, size):
            res[i][j] = euclidean(data[i], data[j])
            res[j][i] = res[i][j]

    return res


def get_playlist(linkage, starting_point, size=10):
    playlist = []
    last_index = starting_point

    for nb in range(size):
        array = linkage[last_index]
        lower = None

        for i in range(0, len(array)):

            if i != last_index and i not in playlist:

                if lower is not None and array[lower] > array[i]:
                    lower = i
                elif lower is None:
                    lower = i
        last_index = lower
        playlist.append(last_index)

    return playlist


def plot(arr):
    plt.plot(arr)
    plt.show()


def perf(func, arr1, arr2, nb_test=50):
    res = []
    for el1, el2 in zip(arr1, arr2):
        t = time.time()

        for i in range(nb_test):
            func(el1, el2)

        res.append(time.time() - t)

    return np.array(res)


def test_perf():
    x1 = np.random.uniform(1, 15, (10000, 4))
    x2 = np.random.uniform(1, 15, (10000, 4))

    perf_eucl = perf(euclidean, x1, x2)
    perf_nb_eucl = perf(np_euclidean, x1, x2)

    print(sum(perf_eucl))
    print(sum(perf_nb_eucl))

    # print(euclidean([2, 3, 1], [2, 6, 4]))


if __name__ == '__main__':
    datas = pd.read_csv('data.csv', engine='python',
                        delimiter=' ', header=0, encoding="utf8")

    features = "filename zero_cr spectral_centroid spectral_rollof chroma_frequency".split()

    # print(datas[features[1:]])
    data_to_use = datas[features[1:]]
    # print(np.array(data_to_use))
    songs = [datas[['filename']].iloc[i].filename
             for i in range(len(datas[['filename']]))]

    # print(songs)
    print(datas)
    """
    On saute de 42 "manger c'est tricher" à  2 "presque rien" 
    alors qu'il n'y a pas de correspondance proche entre eux 
    """

    mat = matrice_distance(np.array(data_to_use))
    i_of_song = get_playlist(mat, 0)
    print(i_of_song)

    res = [songs[i] for i in i_of_song]

    print(res)
    
