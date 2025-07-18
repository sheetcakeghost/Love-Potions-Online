# Dealing with Problems

## Dealing With Display Problems

### On Startup

Ren'Py requires that your computer has functioning graphics acceleration hardware, such as a GPU or a CPU with integrated graphics. Ren'Py will automatically choose between the following renderers, in order.

These are the classic renderers that were used from Ren'Py 6.13 to Ren'Py 7.4. These may not be available in 7.4 and later games that require model-based rendering.

1.  gl: OpenGL 2.0 or greater.
    
2.  angle: Windows, DirectX 9 or DirectX 11.
    
3.  gles: OpenGL ES 3.0.
    

These are model-based renderers present in Ren'Py 7.4 and later. These currently exist to enable new features, and are expected to become the default renderer in the future.

4.  gl2: OpenGL 2.0 or greater.
    
5.  angle2: Windows, DirectX 9 or DirectX 11.
    
6.  gles2: OpenGL ES 3.0.
    

Older versions of Ren'Py supported a software renderer, but this has been removed.

A small fraction of systems may experience problems when running hardware accelerated Ren'Py games. These problems are often due to buggy graphics drivers, and so your first step to fixing them should be to check for an update to your graphics card drivers.

If upgrading your video drivers does not fix the problem, you should consider switching video renderers, using the following steps.

1.  Hold down Shift while starting Ren'Py, or press Shift+G once Ren'Py has started.
    
2.  From the "Graphics Acceleration" menu that appears, choose the renderer to use.
    
3.  Choose "Quit", then restart Ren'Py.
    

We suggest trying the GL and ANGLE renderers. The GLES renderers may not function on desktop hardware.

### On Suspend/Resume

We have had reports of systems that lose textures when a computer is suspened and resumed. This is likely a problem with the computer or its device drivers, but it is possible to force Ren'Py to reload the textures by resizing the window, or pressing the F key to toggle fullscreen mode.

## Windows Encoding Problems

Ren'Py will fail to start on Windows if it's placed in a directory with a full path that isn't representable in the current system language. For example, if Ren'Py is in the directory:

C:��ジュアルノベルenpy\-6.16.0\-sdk

and the system is set to use the English language, Ren'Py will be unable to start. To fix this problem, start the control panel, select "Region and Language Options", "Advanced", and change the Language for non-Unicode programs.

## 64-Bit Linux Problems

Ren'Py 6.14.x and 6.15.0-3 were compiled incorrectly, and will often fail to operate on 64-bit Linux computers. The best way to work around this is to download Ren'Py 6.15.4 or later, and use it to run the game:

/path/to/renpy\-6.15.4/renpy.sh /path/to/game\-with\-problems
