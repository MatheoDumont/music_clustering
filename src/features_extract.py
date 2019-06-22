import numpy as np
import librosa as l

import csv
import os


path_to_music = "E:/music/"
working_path = "E:/python/music_classification/"

features = "filename zero_cr spectral_centroid spectral_rollof chroma_frequency".split()

if __name__ == '__main__':

    os.chdir(path_to_music)

    with open(working_path+"data.csv", "w", encoding="utf8") as data:
        writer = csv.writer(data, delimiter=' ',)
        writer.writerow(features)

        # print(l.load(os.listdir('.')[0]))
        # print(os.listdir('.')[0])
        i = 1

        for music in os.listdir('.'):

            y, sr = l.load(music)
            zero_cr = np.mean(l.feature.zero_crossing_rate(y))
            spectral_centroid = np.mean(l.feature.spectral_centroid(y, sr=sr))
            spectral_rollof = np.mean(l.feature.spectral_rolloff(y, sr=sr))
            chroma_frequency = np.mean(l.feature.chroma_stft(y, sr=sr))

            print(f"{i} -- {music}")
            i += 1

            writer.writerow([music, zero_cr, spectral_centroid,
                             spectral_rollof, chroma_frequency])
