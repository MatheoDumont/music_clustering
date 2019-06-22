import numpy as np
import matplotlib.pyplot as plt
import wave



if __name__ == '__main__':
    f = wave.open('Alestorm - You are a Pirate.m4a')
    frec = 44100
    data = f.readframes(-1)
    signal = np.fromstring(data, 'int32')
    print(signal)

    time = (np.asanyarray(range(len(signal)))) / float(frec)

    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)

    lin = ax.plot(time, signal)
    
    ax.set_yscale('linear')
    plt.show()

    """
    OR
    arr = np.memmap(file, dtype='i', mode='r')
    time = np.array(range(0, len(arr)))/44100
    plt.plot(time, arr)
    plt.show()
    """


