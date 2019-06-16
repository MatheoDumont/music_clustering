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


def index_of_min(array):
    lower = 0
    start = 1

    for i in range(start, len(array)):
        if array[lower] > array[i]:
            lower = i

    return lower


def index_of_min_from_DM(linkage, index_of_null):
    """
    Minimum from distance matrix
    handy function 
    We remove the null part 

    Example : 
    [  76.40452126   27.15250606  790.82043787 2195.82013674  634.53927031
     2861.8727094   945.5546496   165.10467752 1327.35738748  502.36618609
     1546.52411759 1314.15742573  698.95166899 2322.41976264 2137.06747392
     1839.95454602 2886.78302875 2436.17694772 1012.67918238 1024.59936979
     1574.81609623 1275.95244111 1949.10356696  629.84900179  337.79728008
      459.45813377  587.74739383  352.54251952 2810.96059878  118.9961152
     2427.18393976 1401.22227827 3282.04422864 1998.56417317 2984.66106946
      128.20518552  236.46341387  624.78167395  288.26903998 1732.28904218
      363.11554251 1246.77704291    0.           62.07989792  835.51880053
      352.00792785  192.75568439  621.74554624 1487.87493271 1211.60807062
     4659.88262053 2611.27659548 3350.48309651  707.27039559  682.36297277
     2114.64450767 1080.01616356  269.61243    1671.09664584 3275.09611998
     1480.61788557 1645.61606249  181.57538167  197.96756636 2045.27697624]

     AFTER : 

     [  76.40452126   27.15250606  790.82043787 2195.82013674  634.53927031
     2861.8727094   945.5546496   165.10467752 1327.35738748  502.36618609
     1546.52411759 1314.15742573  698.95166899 2322.41976264 2137.06747392
     1839.95454602 2886.78302875 2436.17694772 1012.67918238 1024.59936979
     1574.81609623 1275.95244111 1949.10356696  629.84900179  337.79728008
      459.45813377  587.74739383  352.54251952 2810.96059878  118.9961152
     2427.18393976 1401.22227827 3282.04422864 1998.56417317 2984.66106946
      128.20518552  236.46341387  624.78167395  288.26903998 1732.28904218
      363.11554251 1246.77704291   62.07989792  835.51880053
      352.00792785  192.75568439  621.74554624 1487.87493271 1211.60807062
     4659.88262053 2611.27659548 3350.48309651  707.27039559  682.36297277
     2114.64450767 1080.01616356  269.61243    1671.09664584 3275.09611998
     1480.61788557 1645.61606249  181.57538167  197.96756636 2045.27697624]

     Then we can get the minimum
    """

    # We remove the null part
    array = np.delete(linkage[index_of_null], index_of_null)

    index = index_of_min(array)

    if index >= index_of_null:
        """
        without removing the null index
         0 1 2 3 4 5 6
        [1,2,3,6,0,4,9]
        
        when we remove the null index it give :
         0 1 2 3 4 5
        [1,2,3,6,4,9]

        so those before the null index remain the same
        but those after change (-1)

        so we make the logic on this side
        """
        return (index + 1)

    return index


def get_playlist(linkage, labels, starting_point, size=10):
    """
    Work with full matrice (not upper triang.)
    """
    playlist = []

    last_index = index_of_min_from_DM(linkage, starting_point) 
    playlist.append(labels[last_index])

    for i in range(1, size):

        last_index = index_of_min_from_DM(linkage, last_index)

        if(last_index >= len(linkage)):
            break

        playlist.append(labels[last_index])

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
    
    print(get_playlist(mat, songs, 0))
