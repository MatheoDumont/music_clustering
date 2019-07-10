import numpy as np
import librosa as l

import csv
import os
from concurrent.futures import ProcessPoolExecutor
import time

"""
multi-processes features extract

benchmarks:
    340.38 sec avec chunksize =  len(os.listdir('.'))//4 soit environ 16
    467.27 avec chunksize par défaut = 1
"""



path_to_music = "E:/music/"
working_path = "E:/python/music_classification/"

features = "filename zero_cr spectral_centroid spectral_rollof chroma_frequency".split()


def extract_features(music):

    y, sr = l.load(music)
    zero_cr = np.mean(l.feature.zero_crossing_rate(y))
    spectral_centroid = np.mean(l.feature.spectral_centroid(y, sr=sr))
    spectral_rollof = np.mean(l.feature.spectral_rolloff(y, sr=sr))
    chroma_frequency = np.mean(l.feature.chroma_stft(y, sr=sr))
    mfccs = [np.mean(el) for el in l.feature.mfcc(y, sr=sr)]

    return np.append([music, zero_cr, spectral_centroid,
                                       spectral_rollof, chroma_frequency], mfccs)

if __name__ == '__main__':
    t = time.time()
    os.chdir(path_to_music)

    with open(working_path+"data_2.csv", "w", encoding="utf8") as data:
        writer = csv.writer(data, delimiter=' ',)

        # mfccs headers
        for i in range(20):
            features.append(f'mfcc{i}')

        # writes headers
        writer.writerow(features)

        i = 1

        with ProcessPoolExecutor() as executor:
            for music_features in executor.map(extract_features, os.listdir('.')): # chunksize=len(os.listdir('.'))//4
                writer.writerow(music_features)
                print(f"{i} -- {music_features[0]}")
                i += 1
    print(time.time() - t)

