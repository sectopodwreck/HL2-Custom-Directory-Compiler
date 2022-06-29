"""
Implementing LZMA to attempt to read a single, isolated data entry. The data is taken from the first entry in chaseville.
"""

import lzma

pWrite = lzma.open("./testcompress.lzma", "w")

pWriting = str.encode("Hello world!, I am a compressed string!")

print(pWriting)

pWrite.write(lzma.compress(pWriting, format=lzma.FORMAT_ALONE))

pWrite.close()

pFile = open("./entry.lzma", "rb")

bData = pFile.read()

strOutput = lzma.decompress(bData, format=lzma.FORMAT_AUTO)

print("Decompressed Data:\n")

print(strOutput)
