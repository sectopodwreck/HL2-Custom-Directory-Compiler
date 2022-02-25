'''
Created on Feb 01, 2022

@author: Zach Wallace (BP)

Convert Valve's Keyval format to and from a dictionary element.

It's possible for the keyval to have the same keys, so the main value will be an array of keyvals.

'''

from os.path import isdir, abspath, basename, splitext

"""
Reads the given file, and turns it into a dictionary.

pFile: The file object of a Keyval file.
"""
def load(pFile):
    #Get its name.
    strFileName = pFile.name[:pFile.name.rfind("/") + 1]

    #Prepare the dictionary
    dictFile = {}
    strActiveKey = ""

    pFile.seek(0)

    while (strLine := pFile.readline()):
        """
        In this loop, we are on the highest level of the bns.
        It should only contain the names of the maps, and then their respective keyvals after.

        Format:
        "Map Name"
        {
            Keyvals
        }
        "Another Map"
        {
            Keyvals
        }
        """

        #First check to make sure we have a squirly bracket. They indicate the start of a keyval pair.
        if "{" in strLine:
            #We have a squirly! Start the recursive loop go get all keyvals.
            dictFile[strActiveKey] = getKeyVals(pFile)
            continue

        #If this does end up here, that's actually a problem. We will try and fix it while parsing though.
        if "}" in strLine:
            strLine = pFile.readline()
            continue

        #If we get through all of that, it's safe to assume we only have the name of the map.
        #Get both sides of the name.
        intFirstInstance = strLine.find("\"")
        intSecondInstance = strLine.rfind("\"")

        #Check to make sure we did get both sides.
        if (not intFirstInstance == -1 and not intSecondInstance == -1):
            strActiveKey = strLine[intFirstInstance + 1:intSecondInstance].strip()
        else:
            #Wasn't a key. We may have a problem.
            strActiveKey = strLine.strip()

        #Go back through the loop.
        continue

    pFile.close()

    return dictFile

"""
    While going through a file, iterate over everything inside of the current level of {}
    and return a dictionary of the found keyvals.
"""
def getKeyVals(pFile):
    #When we first enter, pFile should be on the "{". So reading the line should give us the first keyval pair.
    dictKeyVal = dict()
    while not "}" in (strLine := pFile.readline()):
        #Find each pair through their use of quotation marks.
        intFirstInstance = strLine.find("\"")
        intSecondInstance = strLine.find("\"", intFirstInstance + 1)
        if(intFirstInstance == -1):
            continue

        strKey = strLine[intFirstInstance + 1 : intSecondInstance]

        intFirstInstance = strLine.find("\"", intSecondInstance + 1)
        intSecondInstance = strLine.find("\"", intFirstInstance + 1)
        strVal = strLine[intFirstInstance + 1 : intSecondInstance]

        addVal(dictKeyVal, strKey, strVal)

    #We hit a }! Time to return what we got!
    return dictKeyVal

"""
    Checks to see if a key exists, and appends.
    Creates a new array and appends if it doesn't exist
"""
def addVal(dictKeyVal, key, val):
    if not key in dictKeyVal:
        #new key
        dictKeyVal[key] = list()
    #Append to key's array
    if val in dictKeyVal[key]:
        return
    dictKeyVal[key].append(val)
    return

def save(dictData, pFile):
    """
    pFile: open() instance.
    rData: Array of map info.

    Writes to pFile in KeyVal format.
    """

    #Clear the file of previous data.
    pFile.seek(0)
    pFile.truncate()

    for main, mainKeyVals in dictData.items():
        
        pFile.write(f"{main}\n{{\n")

        #value is a dictionary
        
        for key, vals in mainKeyVals.items():
            #One last iteration of an array
            for val in vals:
                pFile.write(f"\t\"{key}\"\t\"{val}\"\n")

        pFile.write("}\n")

if __name__ == "__main__":
    """
        Running the Python script by itself.
        Allow the user to either compile into vdf or json.
    """

    import argparse as ap
    import json as js

    parser = ap.ArgumentParser(description="A Keyvals/dictionary/.JSON converter.\nUsed as a module, allows you to convert Valve Keyval files to dictionaries.")

    parser.add_argument("-v", "--valve", type=ap.FileType("r", encoding="utf-8"), help="The file path to a Valve Keyval file.")
    parser.add_argument("-j", "--json", type=ap.FileType("r", encoding="utf-8"), help="The file path to a json file containing Keyval information.")
    parser.add_argument("-o", "--output", type=str, help="The file path for where the converted data should go.")
    parser.add_argument("-p", "--print", action="store_true", help="Prints out the contents of the bonus map.")

    args = parser.parse_args()

    #First check to make sure both json and bns are not being used at once.
    if args.valve and args.json:
        print("ERROR: Can't have both --bns and --json flags!")
        exit(1)

    #Now to see if they are inputting in nothing.
    if not (args.valve or args.json):
        parser.print_help()
        exit(1)

    #BNS file.
    if args.valve:
        #Parse keyvals
        dictData = load(args.valve)

        #Check to see if the user wants us to print.
        if(args.print):
            print(js.dumps(dictData, indent=4))

        #User wants to output as a json.
        if(args.output):
            if(isdir(args.output)):
                args.output = f"{abspath(args.output)}/{splitext(basename(args.valve.name))[0]}.json"
            pOutputFile = open(args.output, "w+")
            js.dump(dictData, pOutputFile, indent=4)
            pOutputFile.close()

        #Exit out before fucking anything else up.
        exit(0)

    #JSON file.
    if args.json:
        #Parse JSON
        dictData = js.load(args.json)

        #Check to see if the user wants us to print.
        if(args.print):
            print(js.dumps(dictData, indent=4))

        #User wants to output as a keyval.
        if(args.output):
            if(isdir(args.output)):
                args.output = f"{abspath(args.output)}/{splitext(basename(args.json.name))[0]}.txt"
            pOutputFile = open(args.output, "w+")
            save(dictData, pOutputFile)
            pOutputFile.close()

        #Exits out before fucking anything else up.
        exit(0)
