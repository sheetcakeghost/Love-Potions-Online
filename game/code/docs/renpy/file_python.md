# File Access

These Python functions allow you to access asset files, which may be found in the game directory, RPA archives, or as Android assets.

renpy.file(_fn_, _encoding\=None_)

An alias for , for compatibility with older versions of Ren'Py.

renpy.list\_files(_common\=False_)

Lists the files in the game directory and archive files. Returns a list of files, with / as the directory separator.

common

If true, files in the common directory are included in the listing.

renpy.loadable(_filename_, _directory\=None_, _tl\=True_)

Returns True if the given filename is loadable, meaning that it can be loaded from the disk or from inside an archive. Returns False if this is not the case.

directory

If not None, a directory to search in if the file is not found in the game directory. This will be prepended to filename, and the search tried again.

tl

If True, a translation subdirectory will be considered as well.

renpy.open\_file(_fn_, _encoding\=None_, _directory\=None_)

Returns a read-only file-like object that accesses the file named fn. The file is accessed using Ren'Py's standard search method, and may reside in the game directory, in an RPA archive, or as an Android asset.

The object supports a wide subset of the fields and methods found on Python's standard file object, opened in binary mode. (Basically, all of the methods that are sensible for a read-only file.)

encoding

If given, the file is open in text mode with the given encoding. If False, the file is opened in binary mode. If None, the default, the encoding is taken from . In most cases, None will open a file in binary mode.

directory

If not None, a directory to search in if the file is not found in the game directory. This will be prepended to filename, and the search tried again.

This returns an io.BufferedReader object if encoding is None, and an io.TextIOWrapper object if encoding is not None.

## Rarely Used

These functions are used more rarely.

renpy.exists(_filename_)

Returns true if the given filename can be found in the searchpath. This only works if a physical file exists on disk. It won't find the file if it's inside of an archive.

You almost certainly want to use  in preference to this function.

renpy.fsdecode(_s_)

Converts s from filesystem encoding to unicode.

renpy.fsencode(_s_, _force\=False_)

Converts s from unicode to the filesystem encoding.

renpy.image\_size(_im_)

Given an image manipulator, loads it and returns a (`width`, `height`) tuple giving its size.

This reads the image in from disk and decompresses it, without using the image cache. This can be slow.
