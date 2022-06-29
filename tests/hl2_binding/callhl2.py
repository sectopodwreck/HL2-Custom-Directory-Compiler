"""
Testing out the ctypes library
"""

import ctypes

hldll = ctypes.CDLL("/usr/lib/libgtk-3.so")

print("Imported in HL2's Client DLLs.")

print(hldll.gtk_get_debug_flags())