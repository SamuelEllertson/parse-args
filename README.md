# ParseArgs

parseArgs acts as a wrapper for the argparse module, allowing you to use json-like syntax to define each argument and the parser setup.

Examples: 

```python
argSkip = {
    "flags": ["--skip"],
    "options": {
        "default": 1,
        "dest": "skip",
        "type": int,
        "metavar": "int",
        "help": "Sets line skip value. (eg: 2 = every other line) default=1"
    }
}
argKeepEmpty = {
    "flags": ["-k", "--keep-empty"],
    "options": {
        "dest": "keepEmpty",
        "action": "store_true",
        "help": "Keep empty lines / dont filter input"
    }
}

parserSetup = {
    "description": "Appends string to value(s). If no input is specified, it reads values from stdin",
    "args": [
        argSkip,
        argKeepEmpty,
    ]
}

args = parseArgs(parserSetup)
```

You can also quickly specify that a set of arguments are mutually exclusive by placing them in their own list like this:

```python
parserSetup = {
    "description": "Rounds a value, default behavior is rounding to nearest integer.\
    If no input is specified, it reads values from stdin",
    "args": [
        argInput,
        [argCeiling, argFloor]
    ],
    "epilog":"The behavior of round for floats can be surprising: for example, \
    round -p 2 2.675 gives 2.67 instead of the expected 2.68. This is not a bug, \
    see https://docs.python.org/3/library/functions.html#round for details"
}
```
