# HL2 Custom Compiler
### Goals and Expectations

## Overview

The HL2 Custom Compiler is a simple, straightforward script designed to be used with the [custom map browser](//github.com/sectopodwreck/HL2-Custom-Map-Browser-And-Tool) to resolve the most common of conflicts which can arrise when a user imports multiple custom maps. The program should be contained in a single binary file which is then placed in the `/custom` directory of whatever mod they'd like to use it in. When the file is ran, it will iterate over all entries in the `/custom` directory, searching for specific files which cause conflicts and adds the extra data to a pool. After all entries have been searched, the program shall then create a new directory which is alphabetically before all other entries, then convert the pool of data collected back into the respective files.

## Front-End

As our goal is only to automate a task that can be done by a human, without any need for customization by the user, there will be no GUI for this program. The most feedback the end user shall recieve should be a console window printing out all of their addons which have been added to the merge, along with a new directory being formed inside the same directory the binary is located.

## Functional Requirements

We must be able to:

* Read and write Valve's own Keyval filetype. (Separate script)
* Read and compile Valve's Choreography filetype. (Separate script)
* Merge the data within said files.
* Search through a directory tree recursively to find a specific file type.
* Create a new directory that mimics a standard `/custom` addon in order to apply the changes
* Allow for the *raw* python files to be easily imported and used in other project to allow other to include this functionality.
* For each script, allow them to be used independantly through the CLI.

# Non-Functional Requirements

* Compile the program into a single binary for ease of use and distribution.
* Prevent any malitious OS operations (Deleting a file which was not created by our own program.)
