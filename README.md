# dataclasses-and-yaml

These are the course materials for the Python Dataclasses and YAML 
presentation at the RMACC '23 Symposium.

A common programming task is to read and validate small amounts of data from 
files, or format and write that data back to files. 
These data could be program parameters or configuration values for example. 
You can spend a significant amount of time writing code to parse 
configuration files, check data types, validate that data,
and pass these values around in your program. All of that requires
maintenance. The addition of a new parameter can entail changing multiple
places in your code.

A better solution is to leverage the dataclasses and pyyaml libraries to
handle all of this for you.

## What is a data class?
	A Data Class is a decorated class, and that decoration provides a 
	nice __init__, __repr__, and other useful "dunder" methods.
	This is part of the Python Standard Library since version 3.7.
	https://docs.python.org/3/library/dataclasses.html

## What is a decorator?
	A decorator is a bit of python shorthand that takes an
	object (e.g. a class or a function) and enhances it with
	useful behavior for free that you don't need to write.
	The @dataclass decorator is a good example.
	(Reference a good pycon talk)

## What is YAML?
	YAML is "Yet Another Markup Language", 
	( or "YAML Ain't Markup Language")
	https://en.wikipedia.org/wiki/YAML#History_and_name
	a simple, human-readable way to "serialize" data (ie make it storable
	and transmittable).

Example 1: define a data class, create an instance of that type, save it 
as YAML, and read it back from YAML.

Example 1b: Maintenance. Add an attribute to a data class.
Don't need to update the code that initializes the variable, saves it, reads
it back in, or passes that variable to functions.

Example 2: define a data class in an external file, define a list of instances 
of that data class, save as YAML, and read it back in.

Example 3: Nested data classes.

Example 4: Recursive data classes.

Example 5: program configuration data class, read it in from YAML, and
override some settings on the command line.

Example 6: Using JSON instead of YAML.
