"""
Addon Compiler

By: Zach Wallace (BP)

This script, given the path to a valid "/custom" directory in the mod of a source engine, will iterate through all addons and gather any conflicting files.
After, it will create a new addon file with the conflicted files that will load in before everything else.
"""

import os

"""
The bread and butter of the operation
Takes in a path string, then sets everything up from there.
"""
def mainMergeAddons(strPath):
    pass

"""
Loads in HL2's stock

game_sounds_manifest
particles_manifest
soundscapes_manifest
surfaceproperties_manifest

strPath: Path to directory with default files
"""
def kvLoadDefault(strPath):
    

"""
Get the mod of the custom directory we are in.

strPath: custom directory

Outputs the name of the mod directory (hl2, episodic, ep2)
"""
def mainGetMod(strPath):
    #Mod is one directory above custom
    return os.path.basename(os.path.abspath(f"{strPath}/.."))

"""
Takes in a file instance to a Valve Keyval file, along with an array of keyvals, and merges into the array.

pFile: File instance
arrCurKeyvals: The current array of key values
"""

def kvMergeFile(pFile, arrCurKeyvals):
    arrNewKeyvals = None

    try:
        arrNewKeyvals = ap.load(pFile)
    except:
        print(f"Failed to de-serialize {os.path.basename(pFile.name)} in order to merge.")
        return
    
    arrCyrKeyvals = list(set(arrCurKeyvals + arrNewKeyvals))
    #We now have any new, unique keyvals.

if __name__ == "__main__":
    import json as js
    import argparse as ap

    #Init necessary variables
    strDir = os.getcwd()

    parser = ap.ArgumentParser(description = "A Source addon compiler which gathers all conflicting files, merges, and places them all in a single addon which is loaded first.")

    parser.add_argument("-p", "--path", type=str, help="The path to the /custom's root directory. Default is your CWD.")

    args = parser.parse_args()

    if args.path:
        assert os.path.isdir(args.path), "Given path is not a valid directory!"
        strDir = args.path

    
