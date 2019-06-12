from pydub import AudioSegment
import librosa
import winsound

import matplotlib.pyplot as plt
import librosa.display as ld
import numpy as np


"""
Test des librairies librosa, pydub et autre
"""


if __name__ == '__main__':
	path = "E:/music/"
	metal = "Alestorm - You are a Pirate.m4a"
	ang = "Angele-Balancetonquoi.wav"
	
	# song = AudioSegment.from_file(path + metal)

	# winsound.PlaySound(path, winsound.SND_FILENAME)
	# wave_song = song.export(metal, format="wav")

	
	x, sr = librosa.load(metal)
	y, sr2 = librosa.load(ang)

	print(sum(librosa.zero_crossings(x)))
	print(sum(librosa.zero_crossings(y)))

	# X = librosa.stft(x)
	# Xdb = librosa.amplitude_to_db(np.abs(X))

	"""
	plt.figure(figsize=(14, 5))
	plt.plot(x[9000:9100])
	plt.show()
	print(sum(librosa.zero_crossings(x[9000:9100])))

	plt.figure(figsize=(14, 5))
	librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log') # log ou hz
	plt.colorbar()
	plt.show()

	print(x.shape, sr)

	# plt.figure(figsize=(14, 5))
	librosa.display.waveplot(x, sr=sr)

	plt.show()
	"""
