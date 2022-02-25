"""
Addon Compiler

By: Zach Wallace (BP)

This script, given the path to a valid "/custom" directory in the mod of a source engine, will iterate through all addons and gather any conflicting files.
After, it will create a new addon file with the conflicted files that will load in before everything else.
"""

import os
import defaultKeyvals as dk
import vkvParser as vk
import binascii as ba

"""
The bread and butter of the operation
Takes in a path string, then sets everything up from there.
"""
def mainMergeAddons(strPath):

    #Load Addons
    arrAddons = mainGetAddons(strPath)
    #Load Defaults
    dictSounds, dictParticles, dictSoundscapes, dictSurfaceprop = kvLoadDefault(strPath)

    #Merge the keyvals.
    addonMergeKvFiles(dictSounds, "scripts/game_sounds_manifest.txt", arrAddons)
    addonMergeKvFiles(dictParticles, "particles/particles_manifest.txt", arrAddons)
    addonMergeKvFiles(dictSoundscapes, "scripts/soundscapes_manifest.txt", arrAddons)
    addonMergeKvFiles(dictSurfaceprop, "scripts/surfaceproperties_manifest.txt", arrAddons)

    #Get the merger addon directory we will use.
    strMergeDir = mainGetMergeAddon(strPath)

    #Create any relavant subdirs just in case.
    os.makedirs(f"{strMergeDir}/scripts", exist_ok=True)
    os.makedirs(f"{strMergeDir}/particles", exist_ok=True)
    os.makedirs(f"{strMergeDir}/resource", exist_ok=True)

    #Save the merged keyvals to the addon.
    with open(f"{strMergeDir}/scripts/game_sounds_manifest.txt", "w+") as pFile:
        vk.save(dictSounds, pFile)
        pFile.close()

    with open(f"{strMergeDir}/particles/particles_manifest.txt", "w+") as pFile:
        vk.save(dictParticles, pFile)
        pFile.close()

    with open(f"{strMergeDir}/scripts/soundscapes_manifest.txt", "w+") as pFile:
        vk.save(dictSoundscapes, pFile)
        pFile.close()

    with open(f"{strMergeDir}/scripts/surfaceproperties_manifest.txt", "w+") as pFile:
        vk.save(dictSurfaceprop, pFile)
        pFile.close()

    #Update the localization file.

    with open(f"{strMergeDir}/resource/gameui_english.txt", "wb+") as pFile:
        pFile.seek(0)
        pFile.truncate()
        strAddons = addonStringNames(arrAddons)
        pFile.write(ba.unhexlify("FFFE"))
        pFile.write(dk.GAME_OVERWRITE_STRING.format(strAddons).encode("utf-16-le"))
        pFile.write(ba.unhexlify("0D000A00"))
        pFile.close()

    print(f"Merged {len(arrAddons)} addons!")

    return
    


"""
Loads in HL2's stock

game_sounds_manifest
particles_manifest
soundscapes_manifest
surfaceproperties_manifest

strPath: Path to directory with default files
"""
def kvLoadDefault(strPath):
    
    dictSounds = dictParticles = dictSoundscapes = dictSurfaceprop = None
    
    strMod = mainGetMod(strPath)

    if(strMod == "hl2"):
        dictSounds = dk.hl2GetGameSounds()
        dictParticles = dk.hl2GetParticles()
        dictSoundscapes = dk.hl2GetSoundscapes()
        dictSurfaceprop = dk.hl2GetSurfaceprops()
    elif(strMod == "episodic"):
        dictSounds = dk.episodicGetGameSounds()
        dictParticles = dk.episodicGetParticles()
        dictSoundscapes = dk.episodicGetSoundscapes()
        dictSurfaceprop = dk.hl2GetSurfaceprops()
    elif(strMod == "ep2"):
        dictSounds = dk.ep2GetGameSounds()
        dictParticles = dk.ep2GetParticles()
        dictSoundscapes = dk.ep2GetSoundscapes()
        dictSurfaceprop = dk.ep2GetSurfaceprops()
    else:
        raise LookupError(f"The mod, {strMod}, isn't a valid mod for this script.")
    
    return dictSounds, dictParticles, dictSoundscapes, dictSurfaceprop

"""
Get the mod of the custom directory we are in.

strPath: custom directory

Outputs the name of the mod directory (hl2, episodic, ep2)
"""
def mainGetMod(strPath):
    #Mod is one directory above custom
    return os.path.basename(os.path.abspath(f"{strPath}/.."))

"""
Given a path to custom, return an array of paths inside of the directory, ignoring the merge addon.

strPath: Custom directory root.
"""
def mainGetAddons(strPath):
    arrAddons = []
    for addon in os.listdir(strPath):
        strFullPath = f"{strPath}/{addon}"
        if os.path.exists(f"{strFullPath}/addonignore.txt"):
            continue
        arrAddons.append(strFullPath)

    return arrAddons

"""
Finds the alphabetically first addon and checks to see if it's a merger addon.
If it is, it'll return the path to its root.
If it's not, it'll create a name which comes alphabetically before the fist addon, then return the path to that new directory.

merger addon is indicated by a simple addonignore.txt file in the root of the addon directory.

strPath: Custom directory root.
"""
def mainGetMergeAddon(strPath):
    strFirstAddon = None
    try:
        strFirstAddon = sorted(os.listdir(strPath))[0]
        strFirstAddonDir = f"{strPath}/{strFirstAddon}"

    except IndexError:
        print("There are no addons in the custom directory!")
        return None
    
    if not os.path.exists(f"{strFirstAddonDir}/addonignore.txt"):
        #The first addon in the directory is a normal addon, not a merger.
        #Create a new directory that comes before it, and set our addon to that.
        strFirstAddon = f"a{strFirstAddon}addonmerge"
        strFirstAddonDir = f"{strPath}/{strFirstAddon}"
        
        #Makedir and add in the ignore, along with default cfgs
        os.makedirs(f"{strFirstAddonDir}/cfg")

        with open(f"{strFirstAddonDir}/addonignore.txt", "x") as pFile:
            pFile.write("This addon was created by a merging script to resolve any conflicting issues.\nPlease delete this addon or re-merge if you are experiencing any issues in-game.")
            pFile.close()

        with open(f"{strFirstAddonDir}/cfg/game.cfg", "x") as pFile:
            pFile.write(dk.GAME_CFG)
            pFile.close()
        
        with open(f"{strFirstAddonDir}/cfg/modsettings.cfg", "x") as pFile:
            pFile.write(dk.MODSETTINGS_CFG)
            pFile.close()

    #The current path is a valid merge directory.

    return strFirstAddonDir


"""
Converts an array of addon paths to only the addon name.

arrAddons: Array of paths to addons.
"""
def addonPathToName(arrAddons):
    arrAddonNames = []
    for addon in arrAddons:
        arrAddonNames.append(os.path.basename(addon))
    return arrAddonNames

"""
Take an array of addons then return a string with all names broken with newlines.

arrAddons: Array of paths to addons.
"""
def addonStringNames(arrAddons):
    strOutput = ""
    if len(arrAddons) > 5:
        strOutput = f"A total of {len(arrAddons)} have been merged!"
    else:
        for addon in arrAddons:
            strOutput = f"{strOutput}\\n{os.path.basename(addon)}"
    #Got all the addons.
    return strOutput

"""
Iterates over all given addon paths, checking and merging all keyval files of the same name.

dictBaseKeyvals: Original keyvals, this will be added onto.
strFilePath: Path to the target file we are merging relative to the addon's root directory.
arrAddons: Array of all addon paths.
"""
def addonMergeKvFiles(dictBaseKeyvals, strFilePath, arrAddons):
    #Iterate over all addon directories
    for strAddon in arrAddons:
        strTargetFile = f"{strAddon}/{strFilePath}"
        #Check to see if it doesn't exist
        if not os.path.isfile(strTargetFile):
            #Addon doesn't have it, thank god the developer was compitent.
            continue
        #Addon does have it, time to fix the dev's mistakes.
        pFile = open(strTargetFile, "r")
        
        try:
            kvMergeFile(pFile, dictBaseKeyvals)
        except AttributeError:
            print(f"Had a problem merging addon \"{os.path.basename(strAddon)}\" into \"{os.path.basename(strTargetFile)}\".")

        pFile.close()

    #All addon conflicting files have been merged, time to exit.

    return

"""
Takes in a file instance to a Valve Keyval file, along with an array of keyvals, and merges into the array.

pFile: File instance
arrCurKeyvals: The current array of key values
"""

def kvMergeFile(pFile, dictCurKeyvals):

    #Get the only key in the first dictionary
    strManifestType = list(dictCurKeyvals.keys())[0]

    dictNewKeyvals = vk.load(pFile)
    
    strNewManifestType = list(dictNewKeyvals.keys())[0]
    #Check to see if the only key for both dictionaries are the same.
    if(not strManifestType == strNewManifestType):
        #Do one last check to make sure it's not dumbass Valve being dumbass Valve.
        if not strNewManifestType in ["soundscapes_manifest", "soundscaples_manifest"]:
            #We should not be merging these files.
            raise AttributeError(f"File associated with {list(dictNewKeyvals.keys())[0]} is trying to merge into the {strManifestType} dictionary.")

    #We are good to merge, iterate over all keys in the new keyvals, then iterate over all entries.

    for key, arrVals in dictNewKeyvals[strNewManifestType].items():
        #Check to see if the key exists
        if not key in dictCurKeyvals[strManifestType].keys():
            #Key doesn't exist, create it.
            dictCurKeyvals[strManifestType]["key"] = list()

        for item in arrVals:
            arrCurKey = dictCurKeyvals[strManifestType][key]
            if not item in arrCurKey:
                #Item doesn't exist, we can add it w/o any problems.
                arrCurKey.append(item)
        #Done iterating over all items in the given key.
    #Done iterating over all keys in the dictionary.

    #We don't need to return the dictionary as it's already passed by reference.
    return


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
        strDir = os.path.abspath(args.path)
    else:
        print("Path argument required.")
        exit(1)

    arrAddonPaths = mainMergeAddons(strDir)

