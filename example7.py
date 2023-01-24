# example7.py - this can be done with JSON format as well, using the
# jsonpickle class. The standard json class in the python standard library
# is not as convenient to use.
#
# Install jsonpickle with "pip install --user jsonpickle" .

from dataclasses import dataclass
import jsonpickle

@dataclass 
class City:
	name: str
	latitude: float
	longitude: float

# Create a City and save it to a file.
tempe = City( "Tempe", 33.40, -111.93 ),
with open('tempe.json','w') as ofs:
	ofs.write(jsonpickle.encode(tempe))

# Read the city back in and print it.
with open('tempe.json') as ifs:
	copy_of_tempe=jsonpickle.decode(ifs.read())
print("Copy of Tempe object:", copy_of_tempe)
