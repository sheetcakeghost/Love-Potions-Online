# Building Distributions

Ren'Py includes support for building game distributions. Upon choosing "Build Distributions" in the launcher, Ren'Py will scan itself and the project to determine the files to include in the distribution, will create any archives that are necessary, and will build package and update files.

With no configuration, Ren'Py is able to build the following kinds of packages:

PC: Windows and Linux

A zip file targeting Windows x86\_64 and Linux x86\_64

Linux

A tar.bz2 file targeting Linux x86\_64. This will also include the 32-bit and 64-bit ARM version of Ren'Py, if present. (These are found in the sdkarm Ren'Py package.)

Macintosh

A zip file containing a Macintosh application targeting macOS OS X on Intel and Apple Silicon processors. Game data will be included inside the application, which appears to the user as a single file. The updater does not work with this package.

Windows

A zip file targeting Windows x86\_64.

Windows, Mac, and Linux for Markets

A distribution that contains the information required to run on software markets like itch.io and Steam. This isn't meant to be run directly (and probably won't work on the Mac), but should be fed to the app store upload process.

Warning

The zip and tar.bz2 files that Ren'Py produces contain permissions information that must be present for Ren'Py to run on Linux and Macintosh.

Unpacking and re-packing a zip file on Windows and then running it on Linux or Macintosh is not supported.

## Basic Configuration

The build process can be configured by setting variables and calling function that live in the build namespace. This must be done from inside an `init python` block. The default settings for these configurations are set in `options.rpy`.

There are a few basic variables and functions that many games will use.

build.name \= "..."

This is used to automatically generate build.directory\_name and build.executable\_name, if neither is set. This should not contain spaces, colons, or semicolons.

build.directory\_name \= "..."

This is used to create the names of directories in the archive files. For example, if this is set to "mygame-1.0", the Linux version of the project will unpack to "mygame-1.0-linux".

This is also used to determine the name of the directory in which the package files are placed. For example, if you set build.directory\_name to mygame-1.0, the archive files will be placed in mygame-1.0-dists in the directory above the base directory.

This variable should not contain special characters like spaces, colons, and semicolons. If not set, it defaults to , a dash, and the version. The version is taken from , if set, or .

build.executable\_name \= "..."

This variable controls the name of the executables that the user clicks on to start the game.

This variable should not contain special characters like spaces, colons, and semicolons. If not set, it defaults to .

For example, if this is set to "mygame", the user will be able to run mygame.exe on Windows, mygame.app on Macintosh, and mygame.sh on Linux.

## Special Files

There are two files that can be included in your game's base directory to customize the build.

`icon.ico`

The icon that is used on Windows.

`icon.icns`

The icon that is used on Macintosh.

These icon files must be in specific formats. You'll need to use a program or web service (such as  and  ) to convert them.

## Classifying and Ignoring Files

The build process works by first classifying files in the Ren'Py distribution and your game into file lists. These file lists are then added to package files.

The classification is done by the build.classify function. It takes a patterns and a space-separated list of filenames. Patterns are matched from first to last, with the first match taking precedence (even if a more-specific pattern follows.) Patterns are matched with and without a leading /. Patterns may include the following special characters:

/

The directory separator.

\*

Matches all characters except for the directory separator.

\*\*

Matches all characters.

For example:

\*\*.txt

Matches all txt files.

game/\*.txt

Matches txt files in the game directory.

There are seven file lists that files can be classified into by default. (Ren'Py places its own files into the first six of these.)

all

These files will be included in all packages, and in Android builds.

linux

These files will be included in packages targeting Linux.

mac

These files will be included in packages targeting Macintosh.

windows

These files will be included in packages targeting Windows.

renpy

These files will be included in packages that require the Ren'Py engine files. (Linux, Macintosh, and Windows.)

android

These files will be included in Android builds.

This set of valid file lists can be expanded by passing  new names as its `file_list` argument.

Files can also be classified in archives. By default, the "archive" archive is declared:

archive

These files will be included in the archive.rpa archive.

The set of archives can also be expanded, using the  function.

Files that are not otherwise classified are placed in the "all" file list.

To exclude files from distribution, classify them as None or the empty string. In this case, \* and \*\* at the end of the pattern must match at least one character.

For example:

\# Include README.txt
build.classify("README.txt", "all")

\# But exclude all other txt files.
build.classify("\*\*.txt", None)

\# Add png and jpg files in the game directory into an archive.
build.classify("game/\*\*.png", "archive")
build.classify("game/\*\*.jpg", "archive")

## Documentation

Calling the build.documentation function with patterns marks files matching those patterns as documentation. Documentation files are included twice in a Macintosh application – both inside and outside of the application itself.

For example, to mark all txt and html files in the base directory as documentation, call:

build.documentation("\*.txt")
build.documentation("\*.html")

## Packages

It's also possible to add new types of packages to the Ren'Py build process. This is done by calling the build.package function with a package name, type, and a string containing the file lists to include.

Say we wanted to build a normal version of our game, and one containing bonus material. We could classify the bonus files in to a "bonus" file list, and then declare an all-premium package with:

\# Declare a new archive belonging to a new "bonus" file list.
build.archive("bonus\_archive", "bonus")

\# Put the bonus files into the new archive.
build.classify("game/bonus/\*\*", "bonus\_archive")

\# Declare the package.
build.package("all-premium", "zip", "windows mac linux renpy all bonus")

Supported package types are "zip" and "tar.bz2" to generate files in those formats, and "directory" to create a directory filled with files.

## Archives

Ren'Py supports combining files into a simple archive format. While not very secure, this protects files from casual copying.

By default, all files classified into the "archive" file list will be placed in an archive.rpa archive, which is included in the all file list.

By calling build.archive, it's possible to declare a new archives and the file lists they will be included in. (It's rare to use anything but the all file list, however.) To use an archive, classify files into a list with its name.

For example, the following will archive images in `images.rpa`, and game scripts into `scripts.rpa`:

\# Declare two archives.
build.archive("scripts", "all")
build.archive("images", "all")

\# Put script files into the scripts archive.
build.classify("game/\*\*.rpy", "scripts")
build.classify("game/\*\*.rpyc", "scripts")

\# Put images into the images archive.
build.classify("game/\*\*.jpg", "images")
build.classify("game/\*\*.png", "images")

If an archive file is empty, it will not be built.

Please think twice about archiving your game. Keeping files open will help others run your game on future platforms – platforms that may not exist until after you're gone.

## The Old-game Directory

When making multiple releases, like when a game is distributed through early access or platforms like Patreon, it's necessary to keep the old .rpyc files around. The .rpyc files contain information that is necessary to ensure that saves can be loaded, and omitting these files can cause problems.

At the same time, Ren'Py will update the .rpyc files in the game directory when these files are changed, making the files unsuitable for inclusion in version control.

To solve this problem, Ren'Py allows you to place the .rpyc files from a previous distribution into the old-game directory, which is alongside the game directory. The directory structure of `old-game/` should match the directory structure of `game/`. For example, `game/scripts/day1.rpyc` should be moved to `old-game/scripts/day1.rpyc`. Files in old-game that are not .rpyc files are ignored.

The advantage of using old-game is that the old-game .rpyc files can be checked in, and that Ren'Py will always start from a known source when generating .rpyc files. While this might not be necessary for a single-developer game with minor changes, old-game is useful for large multiple developer games.

More information about how .rpyc files help with loading saves into changed games can be found at:

*   
    
*   
    

## Requirements

Some stores ask the requirements for Ren'Py applications to run. While this varies from game to game, here's a set of minimums for a generic visual novel.

**Windows**

*   Version: Windows 7 or higher.
    
*   CPU: 2.0 Ghz 64-bit Intel-compatible
    
*   RAM: 2.0 GB
    
*   Graphics: OpenGL 3.0 or DirectX 11
    

**macOS**

*   Version: 10.10+
    
*   CPU: 2.0 Ghz 64-bit Intel-compatible (Apple silicon supported through Rosetta 2)
    
*   RAM: 2.0 GB
    
*   Graphics: OpenGL 3.0
    

**Linux**

*   Version: Ubuntu 16.04+
    
*   CPU: 2.0 Ghz 64-bit Intel-compatible
    
*   RAM: 2.0 GB
    
*   Graphics: OpenGL 3.0
    

The amount of disk space required is entirely determined by the assets in your game, and the amount of CPU and RAM needed may also vary. Ren'Py will also run under OpenGL 2 with certain extensions available.

## Build Functions

build.archive(_name_, _file\_list\='all'_)

Declares the existence of an archive, whose name is added to the list of available archive names, which can be passed to .

If one or more files are classified with name, name.rpa is built as an archive, and then distributed in packages including the file\_list given here.

build.archive("secret", "windows")

If any file is included in the "secret" archive using the  function, the file will be included inside the secret.rpa archive in the windows builds.

As with the  function, if the name given as file\_list doesn't exist as a file list name, it is created and added to the set of valid file lists.

build.classify(_pattern_, _file\_list_)

Classifies files that match pattern into file\_list, which can also be an archive name.

If the name given as file\_list doesn't exist as an archive or file list name, it is created and added to the set of valid file lists.

build.clear()

Clears the list of patterns used to classify files.

build.documentation(_pattern_)

Declares a pattern that matches documentation. In a mac app build, files matching the documentation pattern are stored twice - once inside the app package, and again outside of it.

build.executable(_pattern_)

Adds a pattern marking files as executable on platforms that support it. (Linux and Macintosh)

build.package(_name_, _format_, _file\_lists_, _description\=None_, _update\=True_, _dlc\=False_, _hidden\=False_, _update\_only\=False_)

Declares a package that can be built by the packaging tool.

name

The name of the package.

format

The format of the package. A string containing a space separated list of:

zip

A zip file.

tar.bz2

A tar.bz2 file.

directory

A directory containing the files.

dmg

A Macintosh DMG containing the files.

app-zip

A zip file containing a macintosh application. This format doesn't support the Ren'Py updater.

app-directory

A directory containing the mac app. This format doesn't support the Ren'Py updater.

app-dmg

A macintosh drive image containing a dmg. (Mac only.) This format doesn't support the Ren'Py updater.

bare-zip

A zip file without  prepended.

bare-tar.bz2

A zip file without  prepended.

null

Used to produce only updates, without the main package.

The empty string will not build any package formats (this makes dlc possible).

file\_lists

A list containing the file lists that will be included in the package.

description

An optional description of the package to be built.

update

If true and updates are being built, an update will be built for this package.

dlc

If true, any zip or tar.bz2 file will be built in standalone DLC mode, without an update directory.

hidden

If true, this will be hidden from the list of packages in the launcher.

## Build Info

There are two variables that can be used to provide information about the build. This information is used to generate the game/cache/build\_info.json file, which is loaded as Ren'Py starts.

build.time \= None

This variable defaults to None, but if your game has been built, it will be set to the time the game was built, in seconds since January 1, 1970.

build.info \= { }

This variable lets you store information that will be placed into the game/cache/build\_info.json file in the built game. When the built game starts, game/cache/build\_info.json is loaded and the contents placed into this variable.

Generally, you'll want to check that a field does not exist, and set it, using setdefault.

For example, this stores the name of the computer that built the game in the build\_info.json file:

python hide:
    import socket
    build.info.setdefault("build\_host", socket.gethostname())

The information in this variable needs to be of types that can be placed in JSON files. (That is, None, booleans, strings, numbers, lists, and dictionaries)

## Advanced Configuration

The following variables provide further control of the build process:

build.allow\_integrated\_gpu \= True

Allows Ren'Py to run on the integrated GPU on platforms that have both integrated and discrete GPUs. Right now, this is only supported on Mac OS X.

build.destination \= "{directory\_name}-dists"

Gives the path to the directory the archive files will be placed in. This may be an absolute or a relative path. A relative path is considered to be relative to the projects directory.

The following values are substituted in using Python's `str.format` function.

`{directory_name}`

The value of build.directory\_name.

`{executable_name}`

The value of build.executable\_name.

`{version}`

The value of build.version.

build.change\_icon\_i686 \= True

If True, and icon.ico exists, the icon of the 32-bit Windows executable will be changed. If False, the icon will not be changed. Setting this to False may prevent some antivirus programs from producing a false positive for your game.

build.exclude\_empty\_directories \= True

If true, empty directories (including directories left empty by file archiving) will be removed from generated packages. If false, empty directories will be included.

build.game\_only\_update \= False

If true,  is enabled, and the "Game-Only Update for Mobile" package becomes available.

build.include\_i686 \= True

If true, files necessary to run on 32-bit x86 processors will be included in the Linux and Mac builds. If False, these files will not be included.

build.include\_old\_themes \= True

When true, files required to support themes that existed before Ren'Py 6.99.9 will be included in the build. When false, such files are excluded.

This is set to False when  is called.

build.include\_update \= False

When true, Ren'Py will produce the files required for the  to work.

build.itch\_project \= None

Setting this allows the Ren'Py launcher to upload your project to itch.io. This should be set to the name of a project registered with itch. (For example, "renpytom/the-question").

Once this is set, after the distributions have been built, you can click "Build distributions", "Upload to itch.io" to cause an upload to occur.

build.itch\_channels \= { ... }

This maps a filename pattern (such as "\*-win.zip") to a string giving the itch channel the file should be uploaded to. This defaults to:

{
    "\*-all.zip" : "win-osx-linux",
    "\*-market.zip" : "win-osx-linux",
    "\*-pc.zip" : "win-linux",
    "\*-win.zip" : "win",
    "\*-mac.zip" : "osx",
    "\*-linux.tar.bz2" : "linux",
    "\*-release.apk" : "android",
}

build.mac\_info\_plist \= { }

This is a dictionary mapping strings to strings, that can be used to add or override keys in the mac's Info.plist file.

build.update\_formats \= \

This is a list of formats that the updater will build. The default, "rpu" is supported from Ren'Py 7.7 and 8.2 on. If you need to support updating using the earlier zsync-based updates, add "zsync' to the list.

build.version \= None

Gives a version of the build used by the build process. If None, this defaults to config.version. The main use of this is to allow config.version to have characters that are not valid in file or directory names.
