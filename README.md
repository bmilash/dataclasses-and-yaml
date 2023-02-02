# dataclasses-and-yaml

These are the course materials for the Python Dataclasses and YAML 
presentation at the RMACC '23 Symposium.

A common programming task is to read and validate small amounts of data from 
files, or format and write that data back to files. 
These data could be program parameters or configuration values for example. 
You can spend a significant amount of time writing code to parse 
configuration files, validate that data, pass these values around in your 
program, format and write them back to files, and all of that requires
maintenance. The addition of a new parameter can entail changing multiple
places in your code.

A better solution is to leverage the dataclasses and yaml libraries to
handle all of this for you.

## What is a data class?

A Data Class is a class that has been decorated with the __@dataclass__ 
decorator, and that decoration provides nice \__init__, \__repr__, and other 
useful "dunder" methods. This has been part of the Python Standard Library 
since version 3.7.

[https://docs.python.org/3/library/dataclasses.html](https://docs.python.org/3/library/dataclasses.html "python data class docs")

## What is decoration / what is a decorator?

A decorator is a bit of python shorthand that takes an
object (e.g. a class or a function) and enhances it with
useful behavior __for free__ that you don't need to write.
The @dataclass decorator is a good example.

(Reference a good tutorial on decorators)

## What is YAML?

YAML is "Yet Another Markup Language" (or "YAML Ain't Markup Language"),
a simple, human-readable format for data that is "serialized" (i.e. suitable 
for storage and transmission).  

[https://en.wikipedia.org/wiki/YAML#History_and_name](https://en.wikipedia.org/wiki/YAML#History_and_name)

The python [__yaml__](https://pyyaml.org) library (contained in the 
[PyYAML package](https://pypi.org/project/PyYAML/)) is easy to install, 
and provides the translation for our objects to YAML and back.

## Examples

1. Define a data class, create an instance of that type, save it as YAML, 
and read it back from YAML.

2. Maintenance. Add an attribute to a data class.

3. Define a data class in an external file, define a list of instances 
of that data class, save as YAML, and read it back in.

4. Nested data classes.

5. Recursive data classes.

6. Program configuration data class. Read it in from YAML, and override 
some settings on the command line.

7. Using JSON instead of YAML.


## Background

Dataclasses introduced in python 3.7, first proposed in Python Enhancement
Proposal (PEP) 557: https://peps.python.org/pep-0557/ .
"Where is it not appropriate to use Data Classes?

    API compatibility with tuples or dicts is required.
    Type validation beyond that provided by PEPs 484 and 526 is required, or value validation or conversion is required."
