"""

Scenes.Image Compiler

By: Zachary Wallace

With a given array of vcd files, create a final scenes.image product.

"""

import ctypes as c
from zlib import crc32

"""
Structs
"""

class SceneImageSummary(c.LittleEndianStructure):
    _fields_ = [
            ("length",  c.c_uint32),
            ("sound_cnt", c.c_uint32)
        ]

class SceneImageEntry(c.LittleEndianStructure):
    _fields_ = [
            ("hash", c.c_uint32),
            ("offset", c.c_uint32),
            ("length", c.c_uint32),
            ("summary_offset", c.c_uint32)
        ]

class SceneImageHeader(c.LittleEndianStructure):
    _fields_ = [
            ("id", c.c_uint32),
            ("version", c.c_uint32),
            ("scenes_cnt", c.c_uint32),
            ("strings_cnt", c.c_uint32),
            ("scenes_offset", c.c_uint32)
        ]

"""
String Pool
"""

"""
    Strings are stored in a dictionary, the key is the string itself, the value is the offset
"""
class StringPool():
    def __init__(self, offset = 0):
        self.strings = dict()
        self.offset = offset

    def add(self, strEntry):
        #Check to see if it's already been entered.
        if strEntry in self.strings:
            #Already exists, use the existing idx.
            return self.strings[strEntry]
        #Doesn't exist
        self.strings[strEntry] = -1
        return

    def __add__(self, strEntry):
        return self.add(strEntry)

    """
    With the offset to the beginning of the string pool, set the offsets for all entries.
    """
    def update_offsets(self):
        arrStrings = list(self.strings)
        #Get the beginning offset for the literal strings.
        iStrOffset = c.sizeof(c.c_uint32) * len(arrStrings) + self.offset
        #Iterate over all string entries, setting their index.
        for strEntry in arrStrings:
            self.strings[strEntry] = iStrOffset
            iStrOffset += len(strEntry) + 1 #Extra index needed for \x00
        return

    """
    Get the index of a string

    Returns -1 if it doesn't exist.'
    """
    def get_offset(self, strEntry):
        try:
            return self.strings[strEntry]
        except KeyError:
            return -1

    """
    Write out the string pool to the given file.

    MUST BE OPEN FOR BINARY WRITING!
    """
    def write(self, pFile):
        #Update all of the offsets.
        self.update_offsets()
        #Write out the offsets first.
        for iOffset in sorted(self.strings.values()):
            pFile.write(c.c_uint32(iOffset))
        #Write out the strings now.
        for strString in list(self.strings):
            pFile.write(bytes(strString + "\x00", "utf-8"))
        return

    def get_string_count(self):
        return len(self.strings.keys())

if __name__ == "__main__":
    pTestHeader = SceneImageHeader()
    pTestHeader.id = 1179210582 #VSIF
    pTestHeader.version = 2
    pTestHeader.scenes_cnt = 10
    pTestHeader.strings_cnt = 10
    pTestHeader.scenes_offset = 1024

    pPool = StringPool(c.sizeof(SceneImageHeader))
    pPool + "This is my first ever string added"
    pPool + "Go Beavs!"
    pPool + "We should now be able to add as many strings as we'd like"
    pPool + "Go Beavs!"
    pPool + "There should not be an extra \"Go Beaves!\" at all."

    pTestHeader.strings_cnt = pPool.get_string_count()

    pfile = open("./test.bin", "wb")

    pfile.write(pTestHeader)
    pPool.write(pfile)
    pfile.close()
