import argparse

ArgumentParserParams = [
    'prog',
    'usage', 
    'description', 
    'epilog', 
    'parents', 
    'formatter_class', 
    'prefix_chars', 
    'fromfile_prefix_chars', 
    'argument_default', 
    'conflict_handler', 
    'add_help', 
    'allow_abbrev',
]

def handleArgList(parser, argList):
    for arg in argList:

        if type(arg) == dict:
            #arg is a proper argument object
            addArgument(parser, arg)

        elif type(arg) == list: 
            #arg is a list of mutually exclusive arguments
            addExclusiveArgs(parser, arg)

        else:
            raise TypeError("parseArgs: 'args' should consist only of args and arrays of args")

def addArgument(parser, arg):
    if "flags" not in arg:
        raise KeyError("all arguments must contain 'flags' attribute")

    #options are optional
    if "options" not in arg:
        arg["options"] = dict();

    #extract args and kwargs from the argument object
    args = arg["flags"]
    kwargs = arg["options"]

    #make args compatible for *args notation
    if type(args) == str:
        args = [args]

    parser.add_argument(*args, **kwargs)

def addExclusiveArgs(parser, argList):
    group = parser.add_mutually_exclusive_group()

    handleArgList(group, argList)

def parseArgs(parserSetup):
    if "args" not in parserSetup:
        raise KeyError("parseArgs: parserSetup must contain 'args'")
    
    #only pass in valid kwargs to argparse.ArgumentParser() 
    parserKwargs = {k: v for k, v in parserSetup.items() if k in ArgumentParserParams}
    parser = argparse.ArgumentParser(**parserKwargs)

    argList = parserSetup["args"]

    if type(argList) != list:
        TypeError("parseArgs: 'args' should be a list")

    handleArgList(parser, argList)

    return parser.parse_args();
