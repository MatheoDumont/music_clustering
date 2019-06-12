import numpy as np
import math
import pandas as pd


def euclidean(x1, x2):
    """
    x1 et x2 sont des vecteur de meme taille
    """
    sum = 0
    for elem_x1, elem_x2 in zip(x1, x2):
        sum += math.pow(elem_x2 - elem_x1, 2)

    return math.sqrt(sum)


def distance(elements):
    """
    Compute enclidean distance between each element 
    and return a len(elements) * len(elements) matrice
    """
    pass


def index_of_min(array):
    lower = 0

    for i in range(1, len(array)):
        if array[lower] > array[i]:
            lower = i

    return lower


def get_playlist(linkage, labels, starting_point, size=10):

    playlist = []
    playlist.append(
        labels[index_of_min(np.delete(linkage[starting_point], starting_point))])

    for i in range(1, size):
        playlist.append(
            labels[index_of_min(np.delete(linkage[starting_point], starting_point))])

    return playlist


if __name__ == '__main__':
    datas = pd.read_csv('data.csv', engine='python',
                        delimiter=' ', header=0, encoding="utf8")

    features = "filename zero_cr spectral_centroid spectral_rollof chroma_frequency".split()

    # print(datas[features[1:]])
    data_to_use = datas[features[1:]]

    songs = [datas[['filename']].iloc[i].filename
             for i in range(len(datas[['filename']]))]

    print(songs)
