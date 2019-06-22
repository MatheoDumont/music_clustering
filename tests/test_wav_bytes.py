import math
import struct
import winsound
from io import BytesIO
import codecs
import wave
import winsound

from tinytag import TinyTag
import numpy as np
import matplotlib.pyplot as plt

"""
Lis l'entête d'un ficher wav 
la fréquence est le nombre de sample par seconde 
BytePerSample est la taille d'un sample
BytePerBlock est BitsPerSample * nbrCanaux 
que l'on multiplie ensuite par frequence pour
obtenir BytePerSec.
"""


def test_from_tinytag():
    truc = TinyTag.get('Alestorm - You are a Pirate.m4a', image=True)
    print(truc)


if __name__ == '__main__':
    morceau = "Alestorm - You are a Pirate.m4a"

    wave_op = wave.open(morceau)
    print(wave_op.getsampwidth())

    with open(morceau, "rb") as file:

        # FileTypeBlocID
        byte = file.read(4)
        print(byte)

        # FileSize
        byte = file.read(4)
        print(struct.unpack_from('<I', byte)[0])

        # FileFormatID
        byte = file.read(4)
        print(byte)

        # FormatBlocID
        byte = file.read(4)
        print(struct.unpack_from('<I', byte)[0])

        # BlocSize
        byte = file.read(4)
        print(struct.unpack_from('<I', byte)[0])

        # AudioFormat
        byte = file.read(2)
        print(struct.unpack_from('h', byte)[0])

        # NbrCanaux
        nbcanaux = file.read(2)
        nbcanaux = struct.unpack_from('h', nbcanaux)[0]
        print(nbcanaux)

        # Fréquence
        frec = struct.unpack_from('<I', file.read(4))[0]
        print(frec)

        # BytePerSec
        bytePerSec = struct.unpack_from('<I', file.read(4))[0]
        print(bytePerSec)

        # BytePerBloc
        bytePerBlock = struct.unpack_from('h', file.read(2))[0]
        print(bytePerBlock)

        # BitsPerSample
        bitPerSample = struct.unpack_from('h', file.read(2))[0]
        print(bitPerSample)

        # Data
        byte = file.read(4)
        print(byte.decode('utf8'))

        # DataSize
        byte = file.read(4)
        print(struct.unpack_from('<I', byte)[0])


        
        

