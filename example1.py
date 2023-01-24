# example1.py - simple data class written to YAML file and read back in.
from dataclasses import dataclass
import yaml

@dataclass 
class City:
	name: str
	latitude: float
	longitude: float

# Create a City and save it to a file.
tempe = City( "Tempe", 33.40, -111.93 ),
yaml.dump( tempe, open("tempe.yaml","w") )

# Read the city back in and print it.
copy_of_tempe = yaml.load( open("tempe.yaml","r"), Loader=yaml.Loader )
print("Copy of Tempe object:", copy_of_tempe)
