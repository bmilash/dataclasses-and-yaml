# dataclasses-and-yaml

These are the course materials for the Python Data Classes and YAML presentation at the RMACC '23 Symposium.

A common programming task is to read small amounts of data from files, or 
format and write that data back to files. These data could be program 
parameters or configuration values for example. You can spend a significant 
amount of time writing custom code to parse configuration files, pass these 
values around in your program, format and write them back to files. All of 
that code requires maintenance - the addition of a new parameter can entail 
changing multiple places in your code.

A better solution is to leverage the **yaml** and **dataclasses** libraries to 
handle all of this for you.

## What is YAML?

YAML is "Yet Another Markup Language" (or "YAML Ain't Markup Language"), a 
simple, human-readable format for data that is "serialized" (i.e. suitable 
for storage and transmission).

https://en.wikipedia.org/wiki/YAML#History_and_name

The python [yaml](https://pyyaml.org/) library (contained in the [PyYAML 
package](https://pypi.org/project/PyYAML/)) is easy to install, and provides 
the translation for our objects into YAML and back.

## What is a data class?

A Data Class is a class that has been decorated with the **@dataclass** 
decorator, and that decoration provides nice \_\_init\_\_, \_\_repr\_\_, 
\_\_eq\_\_, and other useful "dunder" methods. Data classes were added to the 
Python Standard Library in version 3.7.

Data classes were designed as a convenient way to hold related data values. 
They were *not* intended as a mechanism for rigorous data type and value 
validation (although we can do some validation).

https://docs.python.org/3/library/dataclasses.html

## What is a decorator?

A decorator is a python function that enhances an object (e.g. a class or 
a function) with useful behavior **for free** that you don't need to code. 
Decorators use a convenient **@sign** syntax to simplify this. The 
@dataclass decorator is a good example.

Here is a good introduction to decorators: https://realpython.com/primer-on-python-decorators/

Writing your own decorators can be tricky, but using decorators is really simple.

## Examples

1. Define a data class, create an instance of that type, save it as YAML, 
and read it back from YAML.

2. Maintenance. Add an attribute to a data class.

3. Define a data class in an external file, define a list of instances 
of that data class, save as YAML, and read it back in.

4. Nested data classes.

5. Recursive data classes.

6. Validation

7. Using JSON instead of YAML.

## Run this in JupyterLite

https://home.chpc.utah.edu/~u0424091/Python/lab?path=dataclasses-and-yaml%2Fintroduction.ipynb

## Run this on mybinder.org

https://mybinder.org/v2/gh/bmilash/dataclasses-and-yaml/HEAD?labpath=introduction.ipynb

## Background

Dataclasses introduced in python 3.7, first proposed in Python Enhancement
Proposal (PEP) 557: https://peps.python.org/pep-0557/ .
"Where is it not appropriate to use Data Classes?

    API compatibility with tuples or dicts is required.
    Type validation beyond that provided by PEPs 484 and 526 is required, or value validation or conversion is required."
