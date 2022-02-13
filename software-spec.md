# HL2 Custom Compiler
### Goals and Expectations

## Overview

The HL2 Custom Compiler is a simple, straightforward script designed to be used with the [custom map browser](//github.com/sectopodwreck/HL2-Custom-Map-Browser-And-Tool) to resolve the most common of conflicts which can arrise when a user imports multiple custom maps. The program should be contained in a single binary file which is then placed in the `/custom` directory of whatever mod they'd like to use it in. When the file is ran, it will iterate over all entries in the `/custom` directory, searching for specific files which cause conflicts and adds the extra data to a pool. After all entries have been searched, the program shall then create a new directory which is alphabetically before all other entries, then convert the pool of data collected back into the respective files.

## Front-End

As our goal is only to automate a task that can be done by a human, without any need for customization by the user, there will be no GUI for this program. The most feedback the end user shall recieve should be a console window printing out all of their addons which have been added to the merge, along with a new directory being formed inside the same directory the binary is located.
