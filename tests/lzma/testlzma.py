"""
Implementing LZMA to attempt to read a single, isolated data entry. The data is taken from the first entry in chaseville.
"""

import lzma
import sys
import codecs

# pWrite = lzma.open("./testcompress.lzma", "w")
# pWriting = str.encode("Hello world!, I am a compressed string!")
# print(pWriting)
# pWrite.write(pWriting)
# pWrite.close()

# pFile = open("./entry.lzma", "rb")
# bData = pFile.read()
# strOutput = lzma.decompress(bData, format=lzma.FORMAT_RAW)
# print("Decompressed Data:\n")
# print(strOutput)

fh = open(sys.path[0] +'/lzma_test_src.lzma', 'rb')
ba = b'' + fh.read()
decompressed = lzma.decompress(ba)
print(decompressed)
fh.close()

'''
    Method provided courtesy of https://stackoverflow.com/questions/37400583/python-lzma-compressed-data-ended-before-the-end-of-stream-marker-was-reached

    Used because I was getting error where end of encoded data occured before the EOF.

    End result looks like a .bvcd file. :)
'''
def decompress_lzma(data):
    results = []
    while True:
        decomp = lzma.LZMADecompressor(lzma.FORMAT_ALONE, None, None)
        try:
            res = decomp.decompress(data)
        except lzma.LZMAError:
            if results:
                break  # Leftover data is not a valid LZMA/XZ stream; ignore it.
            else:
                raise  # Error on the first iteration; bail out.
        results.append(res)
        data = decomp.unused_data
        if not data:
            break
        if not decomp.eof:
            raise lzma.LZMAError("Compressed data ended before the end-of-stream marker was reached")
    return b"".join(results)


fh = open(sys.path[0] +'/entry.lzma', 'rb')
ba = b'' + fh.read()
decompressed = decompress_lzma(ba)
print(decompressed)



