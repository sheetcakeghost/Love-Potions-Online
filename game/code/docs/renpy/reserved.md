# Reserved Names

Ren'Py reserves filenames that are do not begin with a letter or number, and filenames that begin with "00". Very specifically, filenames that start with "00" and "\_" are used by Ren'Py internally.

Ren'Py reserves all names beginning with a single underscore (\_). Do not use names beginning with an underscore, as that may cause your game to break in future versions of Ren'Py.

The following is a list of names that are used by Python. Re-using these names can lead to obscure problems.

*   ArithmeticError
    
*   AssertionError
    
*   AttributeError
    
*   BaseException
    
*   BaseExceptionGroup
    
*   BlockingIOError
    
*   BrokenPipeError
    
*   BufferError
    
*   BytesWarning
    
*   ChildProcessError
    
*   ConnectionAbortedError
    
*   ConnectionError
    
*   ConnectionRefusedError
    
*   ConnectionResetError
    
*   DeprecationWarning
    
*   EOFError
    
*   Ellipsis
    
*   EncodingWarning
    
*   EnvironmentError
    
*   Exception
    
*   ExceptionGroup
    
*   False
    
*   FileExistsError
    
*   FileNotFoundError
    
*   FloatingPointError
    
*   FutureWarning
    
*   GeneratorExit
    
*   IOError
    
*   ImportError
    
*   ImportWarning
    
*   IndentationError
    
*   IndexError
    
*   InterruptedError
    
*   IsADirectoryError
    
*   KeyError
    
*   KeyboardInterrupt
    
*   LookupError
    
*   MemoryError
    
*   ModuleNotFoundError
    
*   NameError
    
*   None
    
*   NoneType
    
*   NotADirectoryError
    
*   NotImplemented
    
*   NotImplementedError
    
*   OSError
    
*   OverflowError
    
*   PPP
    
*   PendingDeprecationWarning
    
*   PermissionError
    
*   ProcessLookupError
    
*   RecursionError
    
*   ReferenceError
    
*   ResourceWarning
    
*   RuntimeError
    
*   RuntimeWarning
    
*   StopAsyncIteration
    
*   StopIteration
    
*   SyntaxError
    
*   SyntaxWarning
    
*   SystemError
    
*   SystemExit
    
*   TabError
    
*   TimeoutError
    
*   True
    
*   TypeError
    
*   UnboundLocalError
    
*   UnicodeDecodeError
    
*   UnicodeEncodeError
    
*   UnicodeError
    
*   UnicodeTranslateError
    
*   UnicodeWarning
    
*   UserWarning
    
*   ValueError
    
*   Warning
    
*   ZeroDivisionError
    
*   abs
    
*   aiter
    
*   all
    
*   anext
    
*   any
    
*   ascii
    
*   bin
    
*   bool
    
*   breakpoint
    
*   bytearray
    
*   bytes
    
*   callable
    
*   chr
    
*   classmethod
    
*   compile
    
*   complex
    
*   copyright
    
*   credits
    
*   delattr
    
*   dict
    
*   dir
    
*   divmod
    
*   enumerate
    
*   eval
    
*   exec
    
*   exit
    
*   filter
    
*   float
    
*   format
    
*   frozenset
    
*   getattr
    
*   globals
    
*   hasattr
    
*   hash
    
*   help
    
*   hex
    
*   id
    
*   input
    
*   int
    
*   isinstance
    
*   issubclass
    
*   iter
    
*   len
    
*   license
    
*   list
    
*   locals
    
*   map
    
*   max
    
*   memoryview
    
*   min
    
*   next
    
*   object
    
*   oct
    
*   open
    
*   ord
    
*   pow
    
*   print
    
*   property
    
*   quit
    
*   range
    
*   repr
    
*   reversed
    
*   round
    
*   set
    
*   setattr
    
*   slice
    
*   sorted
    
*   staticmethod
    
*   str
    
*   sum
    
*   super
    
*   tuple
    
*   type
    
*   vars
    
*   zip
    

The following is a list of names that are used by Ren'Py. While in some cases it makes sense to redefine these names, one should be aware that doing so can cause obscure problems.

*   ADVCharacter
    
*   ADVSpeaker
    
*   Action
    
*   
    
*   Alpha
    
*   
    
*   
    
*   
    
*   
    
*   Animation
    
*   
    
*   
    
*   
    
*   
    
*   Bar
    
*   
    
*   
    
*   
    
*   Button
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   ColorMatrix
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   DictEquality
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   DynamicCharacter
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   FactorZoom
    
*   
    
*   FieldEquality
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   ImageButton
    
*   
    
*   ImageReference
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   Input
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   LiveComposite
    
*   LiveCrop
    
*   LiveTile
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   Motion
    
*   
    
*   
    
*   Move
    
*   MoveFactory
    
*   MoveIn
    
*   MoveOut
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   NVLCharacter
    
*   NVLSpeaker
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   OldMoveTransition
    
*   
    
*   
    
*   
    
*   PY2
    
*   Pan
    
*   
    
*   Particles
    
*   
    
*   
    
*   
    
*   
    
*   Play
    
*   
    
*   Position
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   Revolve
    
*   RevolveInOut
    
*   
    
*   
    
*   
    
*   
    
*   RotoZoom
    
*   RoundRect
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   Set
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   SizeZoom
    
*   
    
*   
    
*   
    
*   
    
*   Speaker
    
*   SplineMatrix
    
*   SplineMotion
    
*   
    
*   
    
*   
    
*   
    
*   Stop
    
*   
    
*   
    
*   SubTransition
    
*   
    
*   
    
*   TextButton
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   TransformMatrix
    
*   
    
*   
    
*   
    
*   
    
*   Viewport
    
*   VoiceInfo
    
*   
    
*   Window
    
*   
    
*   
    
*   
    
*   Zoom
    
*   ZoomInOut
    
*   
    
*   absolute\_import
    
*   
    
*   
    
*   adv\_narrator
    
*   
    
*   anim
    
*   audio
    
*   basestring
    
*   bchr
    
*   
    
*   bord
    
*   `bubble`
    
*   `build`
    
*   
    
*   centered
    
*   color
    
*   `config`
    
*   default
    
*   default\_transition
    
*   
    
*   `define`
    
*   `director`
    
*   dissolve
    
*   division
    
*   
    
*   easeinbottom
    
*   easeinleft
    
*   easeinright
    
*   easeintop
    
*   easeoutbottom
    
*   easeoutleft
    
*   easeoutright
    
*   easeouttop
    
*   extend
    
*   
    
*   
    
*   
    
*   hyperlink\_function
    
*   hyperlink\_sensitive
    
*   hyperlink\_styler
    
*   
    
*   icon
    
*   
    
*   incdir
    
*   
    
*   irisout
    
*   
    
*   layout
    
*   
    
*   library
    
*   
    
*   
    
*   
    
*   
    
*   moveinbottom
    
*   moveinleft
    
*   
    
*   moveintop
    
*   moveoutbottom
    
*   moveoutleft
    
*   
    
*   moveouttop
    
*   
    
*   
    
*   nvl
    
*   
    
*   nvl\_clear\_next
    
*   nvl\_erase
    
*   
    
*   nvl\_list
    
*   
    
*   nvl\_narrator
    
*   
    
*   nvl\_show\_core
    
*   nvl\_variant
    
*   nvl\_window
    
*   
    
*   
    
*   os
    
*   
    
*   
    
*   
    
*   predict\_menu
    
*   predict\_say
    
*   
    
*   print\_function
    
*   pushdown
    
*   pushleft
    
*   
    
*   pushup
    
*   pygame\_sdl2
    
*   pystr
    
*   python\_dict
    
*   python\_list
    
*   python\_object
    
*   python\_set
    
*   raw\_input
    
*   
    
*   renpy\_json
    
*   
    
*   
    
*   
    
*   
    
*   shaderdoc
    
*   slideawaydown
    
*   
    
*   slideawayright
    
*   slideawayup
    
*   slidedown
    
*   
    
*   slideright
    
*   slideup
    
*   
    
*   srcdir
    
*   store
    
*   
    
*   suppress\_overlay
    
*   sv
    
*   swing
    
*   sys
    
*   textshader
    
*   theme
    
*   tobytes
    
*   toggle\_skipping
    
*   top
    
*   
    
*   
    
*   
    
*   
    
*   unicode
    
*   unicode\_literals
    
*   
    
*   vcentered
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   wipedown
    
*   
    
*   wiperight
    
*   wipeup
    
*   with\_statement
    
*   xrange
    
*   
    
*   
    
*   
    

- - -

Built with  using a  provided by .

jQuery(function () { SphinxRtdTheme.Navigation.enable(false); });