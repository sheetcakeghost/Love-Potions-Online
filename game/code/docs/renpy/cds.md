# Creator-Defined Statements

Creator-Defined Statements (CDS) allow you to add your own statements to Ren'Py's scripting language. This makes it possible to add functionality that is not supported by the current syntax.

CDS can be more flexible than the direct Python code equivalent.

For example, picking a line of dialogue at random:

label introduction:
    python:
        greetings \= \['Hello.', 'Welcome.', 'Can I help you?'\]
        greeting \= renpy.random.choice(greetings)

    "\[greeting\]"

Ren'Py's parser does not know ahead of time what happens in the python block or how it should be executed. It does not do anything with this code until execution and triggers an error if an exception occurs.

Using a CDS allows you to:

*   Check the correctness of the parsed syntax (For example, check that the items in the list sent to renpy.random.choice have valid text)
    
*   Ignore incorrect data at execution (For non-critical functions, it is often better to skip the execution than to throw an exception)
    
*   Predict Displayables (If the function uses them)
    
*   Give you addition information during  (If at runtime an error was ignored you can have a report here).
    

For example, the above behaviour, but written as a CDS:

python early:
    def parse\_random(lexer):
        subblock\_lexer \= lexer.subblock\_lexer()
        choices \= \[\]

        while subblock\_lexer.advance():
            with subblock\_lexer.catch\_error():
                statement \= subblock\_lexer.renpy\_statement()
                choices.append(statement)

        return choices

    def next\_random(choices):
        return renpy.random.choice(choices)

    def lint\_random(parsed\_object):
        for i in parsed\_object:
                check \= renpy.check\_text\_tags(i.block\[0\].what)
                if check:
                    renpy.error(check)

    renpy.register\_statement(
        name\="random",
        block\=True,
        parse\=parse\_random,
        next\=next\_random,
        lint\=lint\_random,
    )

`random` is now available as a statement:

label introduction:
    random:
        "Hello."
        "Welcome."
        "Can I help you?"

Using a CDS does not guarantee that the execution will be successful, but the better you code your statement, the better Ren'Py can "understand" what you expect from it.

## Usage

Creator-Defined Statements (CDS) must conform to the following rules:

*   They must be defined in a `python early` block.
    
*   They cannot be used in the same file in which they are defined.
    
*   The file containing the CDS must be loaded earlier than any file that uses it. (Since Ren'Py loads files in the Unicode sort order of their path, it generally makes sense to prefix the name of any file containing a CDS with 01 or some other small number.)
    

Creator-Defined Statements are registered using the  function. This functions takes other functions that perform operations on the content of the CDS.

For example, a new statement named `line` that allows lines of text to be specified without quotes.

line e "These quotes will show up," Eileen said, "and don't need to be backslashed."

The parse function will be sent the lexed content for parsing. The execute function should run an operation on the parsed content. The lint function should report any errors in the parsed content.

python early:
    def parse\_smartline(lexer):
        who \= lexer.simple\_expression()
        what \= lexer.rest()
        return (who, what)

    def execute\_smartline(parsed\_object):
        who, what \= parsed\_object
        renpy.say(eval(who), what)

    def lint\_smartline(parsed\_object):
        who, what \= parsed\_object
        try:
            eval(who)
        except Exception:
            renpy.error("Character not defined: {}".format(who))

        tte \= renpy.check\_text\_tags(what)
        if tte:
            renpy.error(tte)

    renpy.register\_statement(
        "line",
        parse\=parse\_smartline,
        execute\=execute\_smartline,
        lint\=lint\_smartline,
    )

## API Reference

renpy.register\_statement(_name_, _parse\=None_, _lint\=None_, _execute\=None_, _predict\=None_, _next\=None_, _scry\=None_, _block\=False_, _init\=False_, _translatable\=False_, _execute\_init\=None_, _init\_priority\=0_, _label\=None_, _warp\=None_, _translation\_strings\=None_, _force\_begin\_rollback\=False_, _post\_execute\=None_, _post\_label\=None_, _predict\_all\=True_, _predict\_next\=None_, _execute\_default\=None_, _reachable\=None_)

This registers a user-defined statement.

name

This is either a space-separated list of names that begin the statement, or the empty string to define a new default statement (the default statement will replace the say statement).

block

This may be one of:

*   False, to indicate that the satement does not expect a block.
    
*   True, to indicate that the statement expects a block and will parse that block.
    
*   "possible", to indicate that the statement may or may not take a block.
    
*   "script" to indicate that the block shopuld be interpreted as a block of Ren'Py script language statements. See next for how to implement control flow using this.
    
*   "script-possible" is treated like "script" if a block is present, and False otherwise.
    
*   "atl" to indicate that the block should be interpreted as an ATL transsform. This is passed as an additional argument to execute.
    
*   "atl-possible" is treated like "atl" if a block is present, and and False otherwise.
    

parse

This is a function that takes a Lexer object. This function should parse the statement, and return an object. This object is passed as an argument to all the other functions.

lint

This is called to check the statement. It is passed a single argument, the object returned from parse. It should call renpy.error to report errors.

execute

This is a function that is called when the statement executes. It is passed a single argument, the object returned from parse. If there is an ATL block, the keyword argument atl is passed with an ATL transform.

execute\_init

This is a function that is called at init time, at priority 0. It is passed a single argument, the object returned from parse.

predict

This is a function that is called to predict the images used by the statement. It is passed a single argument, the object returned from parse. It should return a list of displayables used by the statement.

next

This is a function that is called to determine the next statement.

If block is not "script", this is passed a single argument, the object returned from the parse function. If block is "script", an additional argument is passed, an object that names the first statement in the block.

The function should return either a string giving a label to jump to, the second argument to transfer control into the block, or None to continue to the statement after this one. It can also return the result of  or  when called in the parse function.

label

This is a function that is called to determine the label of this statement. If it returns a string, that string is used as the statement label, which can be called and jumped to like any other label.

warp

This is a function that is called to determine if this statement should execute during warping. If the function exists and returns true, it's run during warp, otherwise the statement is not run during warp.

scry

Used internally by Ren'Py.

init

True if this statement should be run at init-time. (If the statement is not already inside an init block, it's automatically placed inside an init block.)

You probably don't want this if you have an execute\_init function, as wrapping the statement in an init block will cause the execute\_init and execute functions to be called at the same time.

translatable

If set to true, the statement will be included in a translation block, generally the block containing the succeding say statement. This may only be set to true for one-line statements. It's used for statements like `nvl clear` and `voice`, which may need to be changed with dialogue.

init\_priority

An integer that determines the priority of initialization of the init block created by init and execute\_init function.

translation\_strings

A function that is called with the parsed block. It's expected to return a list of strings, which are then reported as being available to be translated.

force\_begin\_rollback

This should be set to true on statements that are likely to cause the end of a fast skip, similar to `menu` or `call screen`.

post\_execute

A function that is executed as part the next statement after this one. (Adding a post\_execute function changes the contents of the RPYC file, meaning a Force Compile is necessary.)

post\_label

This is a function that is called to determine the label of this the post execute statement. If it returns a string, that string is used as the statement label, which can be called and jumped to like any other label. This can be used to create a unique return point.

predict\_all

If True, then this predicts all sub-parses of this statement and the statement after this statement.

predict\_next

This is called with a single argument, the label of the statement that would run after this statement.

This should be called to predict the statements that can run after this one. It's expected to return a list of of labels or SubParse objects. This is not called if predict\_all is true.

execute\_default

This is a function that is called at the same time the default statements are run - after the init phase, but before the game starts; when the a save is loaded; after rollback; before lint; and potentially at other times.

This is called with a single argument, the object returned from parse.

reachable

This is a function that is called to allow this statement to customize how it participates in lint's reachability analysis.

By default, a statement's custom block, sub-parse blocks created with Lexer.renpy\_block(), and the statement after the statement are reachable if the statement itself is reachable. The statement is also reachable if it has a label function.

This can be customized by providing a reachable function. This is a function that takes five arguments (in the following, a "label" may be a string or an opaque object):

*   The object returned by the parse function.
    
*   A boolean that is true if the statement is reachable.
    
*   The label of the statement.
    
*   The label of the next statement, or None if there is no next statement.
    
*   If block is set to "script", the label of the first statement in the block, or None if there is no block.
    

It's expected to return a set that may contain:

*   A label or subparse object of a statement that is reachable.
    
*   True, to indicate that this statement should not be reported by lint, but is not intrinsically reachable. (It will become reachable if it is reported reachable by another statement.)
    
*   None, which is ignored.
    

This function may be called multiple times with both value of is\_reachable, to allow the statement to customize its behavior based on whether it's reachable or not. (For example, the next statement may only be reachable if this statement is.)

Warning

Using the empty string as the name to redefine the say statement is usually a bad idea. That is because when replacing a Ren'Py native statement, its behavior depends on the . In the case of the say statement, these equivalents do not support the id and translation systems. As a result, a game redefining the default statement will not be able to use these features (short of reimplementing them entirely).

### Lexer object

A custom statement's parse function takes an instance of a Lexer object.

_class_ Lexer

error(_msg_)

Parameters:

**msg** (_str_) -- Message to add to the list of detected parsing errors.

Add msg (with the current position) to the list of detected parsing errors. This interrupts the parsing of the current statement, but does not prevent further parsing.

require(_thing_, _name\=None_)

Try to parse thing and report an error if it cannot be done.

If thing is a string, try to parse it using .

Otherwise, thing must be another method on this lexer object which is called without arguments.

If name is not specified, the name of the method will be used in the message (or thing if it's a string), otherwise name will be used.

eol()

Returns:

True if the lexer is at the end of the line, else False.

Return type:

bool

expect\_eol()

If not at the end of the line, raise an error.

expect\_noblock(_stmt_)

Called to indicate this statement does not expect a block. If a block is found, raise an error. stmt should be a string, it will be added to the message with an error.

expect\_block(_stmt_)

Called to indicate that the statement requires that a non-empty block is present. stmt should be a string, it will be added to the message with an error.

has\_block()

Returns:

True if the current line has a non-empty block, else False.

Return type:

bool

match(_re_)

Match an arbitrary regexp string.

All of the statements in the lexer that match things are implemented in terms of this function. They first skip whitespace, then attempt to match against the line. If the match succeeds, the matched text is returned. Otherwise, None is returned, and the state of the lexer is unchanged.

keyword(_s_)

Match s as a keyword.

name()

Match a name. This does not match built-in keywords.

word()

Returns:

The text of the matched word.

Return type:

str

Match any word, including keywords.

image\_name\_component()

Match an image name component. Unlike a word, an image name component can begin with a number.

string()

Match a Ren'Py string.

integer()

Returns:

String containing the found integer.

Return type:

str

Match an integer.

float()

Returns:

String containing the found floating point number.

Return type:

str

Match a floating point number.

label\_name(_declare\=False_)

Match a label name, either absolute or relative. If declare is true, then the global label name is set. (Note that this does not actually declare the label - the statement is required to do that by returning it from the label function.)

simple\_expression()

Match a simple Python expression, returns it as a string. This is often used when you expect a variable name. It is not recommended to change the result. The correct action is to evaluate the result in the future.

delimited\_python(_delim_)

Match a Python expression that ends in a delim, for example ':'. This is often used when you expect a condition until the delimiter. It is not recommended to change the result. The correct action is to evaluate the result in the future. This raises an error if end of line is reached before the delimiter.

arguments()

This must be called before the parentheses with the arguments list, if they are not specified returns None, otherwise returns an object representing the arguments to a function call. This object has an `evaluate` method on it that takes an optional scope dictionary, and returns a tuple in which the first component is a tuple of positional arguments, and the second component is a dictionary of keyword arguments.

rest()

Skip whitespace, then return the rest of the line.

checkpoint()

Return an opaque object representing the current state of the lexer.

revert(_o_)

When o is the object returned from checkpoint(), reverts the state of the lexer to what it was when checkpoint() was called. (This is used for backtracking.)

subblock\_lexer()

Returns:

A Lexer for the block associated with the current line.

advance()

In a subblock lexer, advance to the next line. This must be called before the first line, so the first line can be parsed. Return True if we've successfully advanced to a line in the block, or False if we have advanced beyond all lines in the block.

renpy\_statement()

When called, this parses the current line as a Ren'Py script statement, generating an error if this is not possible. This method returns an opaque object that can be returned from the next function passed to , or passed to  or . This object should not be stored except as part of the parse result of the statement.

When the statement returned from this completes, control is transferred to the statement after the creator-defined statement. (Which might be the statement created using post\_execute).

renpy\_block(_empty\=False_)

Parse all of the remaining lines in the current block as Ren'Py script, and return a SubParse corresponding to the first statement in the block. The block is chained together such that all statements in the block are run, and then control is transferred to the statement after this creator-defined statement.

Note that this parses the current block. In the more likely case that you'd like to parse the subblock of the current statement, the correct way to do that is:

def mystatement\_parse(l):

    l.require(':')
    l.expect\_eol()
    l.expect\_block("mystatement")

    child \= l.subblock\_lexer().renpy\_block()

    return { "child" : child }

empty

If True, allows an empty block to be parsed. (An empty block is equivalent to a block with a single `pass` statement.)

If False, an empty block triggers an error.

catch\_error()

This is a context decorator, used in conjunction with the with statement, that catches and reports lexer errors inside its context block, then continues after the block.

Here's an example of how it can be used to report multiple errors in a single subblock.

def mystatement\_parse(l):

    l.require(':')
    l.expect\_eol()
    l.expect\_block("mystatement")

    strings \= \[ \]
    ll \= l.subblock\_lexer()

    while ll.advance():
        with ll.catch\_error():
            strings.append(ll.require(ll.string))
            ll.expect\_noblock("string inside mystatement")
            ll.expect\_eol()

    return { "strings" : strings }

### Lint Utility Functions

These functions are useful when writing lint functions.

renpy.check\_text\_tags(_s_, _check\_unclosed\=False_)

Checks the text tags in s for correctness. Returns an error string if there is an error, or None if there is no error.

renpy.error(_msg_)

Reports msg, a string, as as error for the user. This is logged as a parse or lint error when approprate, and otherwise it is raised as an exception.

renpy.try\_compile(_where_, _expr_, _additional\=None_)

Tries to compile an expression, and writes an error to lint.txt if it fails.

where

A string giving the location the expression is found. Used to generate an error message of the form "Could not evaluate expr in where."

expr

The expression to try compiling.

additional

If given, an additional line of information that is addded to the error message.

renpy.try\_eval(_where_, _expr_, _additional\=None_)

Tries to evaluate an expression, and writes an error to lint.txt if it fails.

where

A string giving the location the expression is found. Used to generate an error message of the form "Could not evaluate expr in where."

expr

The expression to try evaluating.

additional

If given, an additional line of information that is addded to the error message.
