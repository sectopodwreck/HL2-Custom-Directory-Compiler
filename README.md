# HL2 Custom Compiler
## A Q.O.L. script

## What is this

Throughout developing my [custom map browser](https://github.com/sectopodwreck/HL2-Custom-Map-Browser-And-Tool) for HL2, I've came across a "limitation" of the Source Engine. There are some files which the level developer must overwrite in order to include certain features into their map (particles, choreography, soundscapes, titles). Usually, during the average user's experience, this isn't a problem as most level developers don't use these in their level. But, it only takes two different addons to completely screw up one entire map. The original way I went about fixing this issue was by [displaying a warning](https://github.com/sectopodwreck/HL2-Custom-Map-Browser-And-Tool#overwriting-error) on the game's startup. This allows the end user to know what map will for sure be functional, but in order to allow other maps to hopefully be playable, they must: exit out of the game, move the conflicting addon to some other directory, restart the game. Ruining the entire purpose of this map browser.

This tool helps to go through all of your addons and merge all conflicting files, allowing for the player to not need to worry about micromanaging their addons in-between installing new ones.

## What files do we need to merge?

First off, we have all the files which use [Valve's Data Format](https://developer.valvesoftware.com/wiki/KeyValues):
* `scripts/game_sounds_manifest.txt`
* `scripts/soundscapes_manifest.txt`
* `particles/particles_manifest.txt`

There is an instance of a file which has an ambiguous file structure:
* `scripts/titles.txt`

Then, there is a serialized binary file, created from plaintext:
* `scenes/scenes.image`

## How do we merge these files?

### VDF Formatted

It's best to convert the file into a hash map, iterate over the file adding any new keyvals to a hardcoded hashmap of the default values. After going over all of the available addons, we should now have a manifest which includes all of the custom dependancies.

### Ambiguous File

We should try and find/use a string diff library. Like before, we have a hardcoded default file, then append any differences between the two files.

### scenes.image

This one's going to be a doozy, and take up most of our development time. As we have researched before, Valve uses Google's protobuf. I have absolutely no idea how that works, nor if the [specs we came across](https://developer.valvesoftware.com/wiki/Scenes.image#Technical_information) earlier are helpful for this. But, we can at least set up everything beforehand.

In order for this to work, we must assume that the level developer is kind enough to leave the plain text `.vcd` files in the `scenes/` directory of their addon.

~~We start off by looping through all addons, like before. When we come across a `scenes/` directory, we then do a recursive search through all subdirs for the `.vcd`s.~~ Unsure about this yet.

I went dumpster diving through the Source Engine codebase and may of found a good starting point. Of course it's still abstracted since it's missing it's dependencies but it can give us a hint on where to start.
