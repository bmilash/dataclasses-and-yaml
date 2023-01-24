# example4.py - nested classes.
from dataclasses import dataclass
import yaml

@dataclass
class Contact:
	name: str
	address: str
	city: str
	state: str
	zipcode: int

@dataclass
class Organization:
	name: str
	ceo: Contact

yoyodyne = Organization( name="Yoyodyne Inc.", 
	ceo = Contact("Brett Milash", "123 4th St.", "SLC", "UT", 84103) )

# Save it.
yaml.dump( yoyodyne, open("yoyo.yaml","w") )

# Read it back in.
copy_of_yoyo = yaml.load( open("yoyo.yaml","r"), Loader=yaml.Loader )

print(copy_of_yoyo)
